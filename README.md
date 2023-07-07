Automatyzacja przypadku testowego przy pomocy Selenium Webdriver

#Automatyczne testy logowania na stronie Filmweb.pl

Ten projekt zawiera automatyczne testy logowania na stronie Filmweb.pl przy użyciu narzędzia Selenium. Testy sprawdzają poprawność logowania oraz przeszukują stronę w poszukiwaniu filmu.

## Wymagania

Aby uruchomić te testy, należy mieć zainstalowane następujące biblioteki:
- Selenium (w wersji 3.141.0 lub nowszej)
- pyautogui (w wersji 0.9.52 lub nowszej)

Można je zainstalować, wykonując polecenie:

pip install -r requirements.txt

## Uruchomienie testów

1. Sklonuj repozytorium na swoje urządzenie:

git clone https://github.com/Vitto89/Project_selenium_webdriver

2. Przejdź do katalogu projektu: cd Project_selenium_webdriver
3. Wykonaj komędę : pip install -r requirements.txt
4. Uruchom testy: python test_login.py

## Opis testu

Test sprawdza poprawność logowania na stronie Filmweb.pl oraz wyszukuje film na podstawie podanego tytułu. Test sprawdza, czy film jest widoczny w wynikach wyszukiwania, czy jest pierwszy w kolejce wyników oraz czy zawiera określonego aktora.

## Oczekiwane rezultaty :
• Logowanie powiodło się, widnieje nazwa użytkownika w prawym górnym rogu.
• Wyszukiwarka odnajduje cel wyszukiwania film : „Pulp Fiction”
• Przedmiot wyszukiwania jest pierwszy na liście, zawiera odpowiednie inicjały w
obsadzie : „John Travolta” i nie powtarza się.

## Uwagi

- Przed uruchomieniem testów upewnij się, że masz zainstalowaną przeglądarkę Chrome oraz sterownik Chrome WebDriver w odpowiedniej wersji.

- Testy powinny być wykonywane na środowisku lokalnym. Niezalecane jest uruchamianie ich na produkcji lub środowiskach produkcyjnych.

- Testy mogą wymagać dostępu do Internetu.

















