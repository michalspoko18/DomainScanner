import whois
from datetime import datetime, timedelta
from notifier import sendEmail

def getPolishMonthName(month_number):
    """Zwraca polską nazwę miesiąca na podstawie numeru (1-12)"""
    polish_months = {
        1: "styczeń",
        2: "luty", 
        3: "marzec",
        4: "kwiecień",
        5: "maj",
        6: "czerwiec",
        7: "lipiec",
        8: "sierpień",
        9: "wrześień",
        10: "październik",
        11: "listopad",
        12: "grudzień"
    }
    return polish_months.get(month_number, "nieznany")

def readDomains():
    try:
        with open('domain.txt', 'r') as file:
            domains = [line.strip() for line in file if line.strip()]
        return domains
    except FileNotFoundError:
        print(f"Plik {'domain.txt'} nie został znaleziony.")
        return []
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {str(e)}")
        return []

from datetime import datetime, timedelta

def checkDomains():
    domains = readDomains()
    message = []
    if not domains:
        return "Brak domen do sprawdzenia."

    one_month_from_now = (datetime.now() + timedelta(days=30)).replace(microsecond=0)

    for domain in domains:
        date_string = expirationDate(domain)  # teraz zwraca string
        # print(f"Sprawdzanie domeny: {domain} - {date_string}")
        # print(one_month_from_now)

        if date_string:
            try:
                # Próbujemy sparsować datę
                expiration_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")  # lub "%Y-%m-%d %H:%M:%S" jeśli z godziną
                # Porównanie dat
                if expiration_date <= one_month_from_now:
                    message.append(f"{domain} - {date_string}")
                    # print(f"Domena {domain} wygasa w ciągu miesiąca: {date_string}")
            except ValueError as e:
                print(f"Niepoprawny format daty dla domeny {domain}: {date_string} ({e})")

    if message:
        current_month = getPolishMonthName(datetime.now().month)
        subject = f"Domeny wygasające w ciągu miesiąca ({current_month} {datetime.now().year}) "
        sendEmail(subject, "\n".join(message))

def expirationDate(url):
    try:
        info = whois.whois(url)
        if info.expiration_date:
            return f"{info.expiration_date}"
        else:
            return None
    except Exception as e:
        return f"{url}: Błąd - {str(e)}"
