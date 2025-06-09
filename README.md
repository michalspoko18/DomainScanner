# Domain Scanner

Aplikacja Flask do monitorowania dat wygaśnięcia domen z automatycznym powiadamianiem e-mail.

## Opis

Domain Scanner to narzędzie, które:
- Sprawdza daty wygaśnięcia domen z pliku tekstowego
- Wysyła powiadomienia e-mail o domenach wygasających w ciągu 30 dni
- Umożliwia automatyczne sprawdzanie za pomocą zadań cron
- Zapewnia interfejs webowy do ręcznego uruchamiania sprawdzeń

## Funkcje

✅ Automatyczne sprawdzanie dat wygaśnięcia domen  
✅ Powiadomienia e-mail dla domen wygasających w ciągu miesiąca  
✅ Harmonogram cron dla regularnych sprawdzeń  
✅ Interfejs webowy Flask  
✅ Obsługa błędów i logowanie  
✅ Polskie nazwy miesięcy w powiadomieniach  

## Wymagania

- Python 3.7+
- Flask
- flask-crontab
- python-whois
- python-dotenv

## Instalacja

1. **Sklonuj repozytorium:**
```bash
git clone https://github.com/michalspoko18/DomainScanner.git
cd DomainScanner
```

2. **Utwórz środowisko wirtualne:**
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# lub
.venv\Scripts\activate     # Windows
```

3. **Zainstaluj zależności:**
```bash
pip install flask flask-crontab python-whois python-dotenv
```

4. **Skonfiguruj zmienne środowiskowe:**
Stwórz plik `.env` w głównym katalogu:
```env
SMTP_SERVER=smtp.twoj-serwer.pl
SMTP_PORT=587
EMAIL=twoj-email@domena.pl
PASSWORD=twoje-haslo
SENDER_EMAIL=twoj-email@domena.pl
RECEIVER_EMAIL=odbiorca@domena.pl
```

5. **Utwórz plik z domenami:**
Stwórz plik `domain.txt` z listą domen (jedna domena na linię):
```
example.com
test.pl
moja-domena.org
```

## Użycie

### Uruchomienie aplikacji

```bash
python main.py
```

Aplikacja będzie dostępna pod adresem: `http://localhost:5000`

### Konfiguracja zadań cron

1. **Dodaj zadania cron:**
```bash
export FLASK_APP=main.py
flask crontab add
```

2. **Sprawdź zadania:**
```bash
crontab -l
```

3. **Usuń zadania cron:**
```bash
flask crontab remove
```

### Ręczne sprawdzenie

Odwiedź `http://localhost:5000` w przeglądarce lub użyj:
```bash
curl http://localhost:5000
```

## Struktura plików

```
DomainScanner/
├── main.py          # Główna aplikacja Flask
├── checker.py       # Logika sprawdzania domen
├── notifier.py      # Obsługa wysyłania e-maili
├── domain.txt       # Lista domen do sprawdzenia
├── .env             # Konfiguracja SMTP
├── .gitignore       # Pliki ignorowane przez git
└── README.md        # Ten plik
```

## Harmonogram zadań

- **Codziennie o 9:00** - automatyczne sprawdzenie wszystkich domen
- **Co minutę** - zadanie testowe (usuń w produkcji)

## Konfiguracja

### Zmienne środowiskowe (.env)

| Zmienna | Opis |
|---------|------|
| `SMTP_SERVER` | Adres serwera SMTP |
| `SMTP_PORT` | Port SMTP (zwykle 587) |
| `EMAIL` | Adres email do logowania |
| `PASSWORD` | Hasło do konta email |
| `SENDER_EMAIL` | Adres nadawcy |
| `RECEIVER_EMAIL` | Adres odbiorcy powiadomień |

### Format pliku domain.txt

```
domena1.pl
domena2.com
domena3.org
```

## Przykład powiadomienia

```
Subject: Domeny wygasające w ciągu miesiąca (czerwca 2025)

example.com - 2025-06-15 12:30:45
test.pl - 2025-06-20 08:15:30
```

## Rozwiązywanie problemów

### Błąd SMTP
```
Failed to send email: [Errno 8] nodename nor servname provided
```
**Rozwiązanie:** Sprawdź konfigurację SMTP w pliku `.env`

### Błąd Flask aplikacji
```
Could not locate a Flask application
```
**Rozwiązanie:** 
```bash
export FLASK_APP=main.py
# lub użyj
flask --app main crontab add
```

### Brak domen
```
Plik domain.txt nie został znaleziony
```
**Rozwiązanie:** Utwórz plik `domain.txt` z listą domen

## Bezpieczeństwo

⚠️ **Ważne:**
- Nie commituj pliku `.env` do repozytorium
- Używaj silnych haseł do kont email
- Regularnie aktualizuj zależności
- W produkcji usuń zadania testowe

## Licencja

MIT License

## Autor

Michał Walczak - [kontakt@michalwalczak.pl](mailto:kontakt@michalwalczak.pl)

## Wkład

Pull requesty są mile widziane. W przypadku większych zmian, najpierw otwórz issue aby przedyskutować zmiany.