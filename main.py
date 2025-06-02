import whois
from flask import Flask

import whois

def whoWeb():
    try:
        with open('pages.txt', 'r') as file:
            pages = [page.strip() for page in file.readlines() if page.strip()]
        
        results = []
        for page in pages:
            try:
                pageInfo = whois.whois(page)
                results.append({
                    'domain': page,
                    'expiration_date': pageInfo.expiration_date
                })
            except Exception as e:
                results.append({
                    'domain': page,
                    'error': str(e)
                })
        
        return results  # Zwraca wszystkie wyniki
        
    except FileNotFoundError:
        return "Błąd: Plik 'pages.txt' nie został znaleziony"
    except Exception as e:
        return f"Błąd: {str(e)}"

    
def test(url):
    info = whois.whois(url)

    return f"{url}: {info.expiration_date}"

app = Flask(__name__)

@app.route("/")
def showWhois():
    return whoWeb()