import smtplib
import os
import discord
from discord.ext import commands
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

def sendEmail(subject, message):
    load_dotenv(override=True)
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email, password)
            server.send_message(msg)
            print("Email sent successfully")
            return "Email sent successfully"
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return f"Failed to send email: {str(e)}"
    
def sendDiscordMessage(message):
    load_dotenv(override=True)
    discord_token = os.getenv('DISCORD_TOKEN')
    channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(message)
            print("Discord message sent successfully")
        else:
            print("Failed to find the Discord channel")
        await bot.close()

    try:
        bot.run(discord_token)
    except Exception as e:
        print(f"Failed to send Discord message: {str(e)}")
        return f"Failed to send Discord message: {str(e)}"
    