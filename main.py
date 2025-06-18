# Importing necessary libraries
from flask import Flask
from flask_crontab import Crontab
from checker import checkDomains

# Initializing Flask app and Crontab
app = Flask(__name__)
crontab = Crontab(app)

@app.route('/')
def index():
    checkDomains()
    return "Domena sprawdzona!"

# Cron job - sprawdzanie domen codziennie o 9:00
@crontab.job(minute='0', hour='9')
def daily_domain_check():
    checkDomains()
    return "Domeny sprawdzone codziennie o 9:00!"

# Cron job - test co minutę (usuń w produkcji)
@crontab.job(minute='*')  # Co minutę
def test_cron():
    checkDomains()
    return "Test cron job executed!"
