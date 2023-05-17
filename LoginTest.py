import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep

# DANE TESTOWE
User = "tester284"
email = "tester284@o2.pl"
password = "Tester284wsb7"


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        """Test preparation"""
        # Przygotowanie testu
        # 1. Otwarta strona główna
        # 1a) Tworzę instancję klasy Chrome()
        self.driver = webdriver.Chrome()
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        # 1b) Otwieram stronę główną
        self.driver.get("https://www.filmweb.pl/")
        cookie_accept = self.driver.find_element(By.ID, "didomi-notice-agree-button")
        cookie_accept.click()
        skip_accept = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/button')
        skip_accept.click()
        sleep(1)

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        # 1. Kliknij „Zarejestruj”
        # 1a) Odszukaj przycisk Zarejestruj
        # 1b) Kliknij ten przycisk
        sleep(1)
        zaloguj_a = self.driver.find_element(By.ID, "main-header_login-link")
        zaloguj_a.click()
        sleep(1)
        zaloguj_b = self.driver.find_element(By.XPATH, '//*[@id="site"]/div[2]/div/div/div[1]/div/div/ul/li[2]/a/div[2]')
        zaloguj_b.click()
        sleep(1)
        # 2. Wpisz nazwisko
        # Odszukaj, wpisz
        User_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[1]/input')
        User_input.send_keys(User)
        # 4. Wpisz hasło
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[2]/input')
        password_input.send_keys(password)

    # 5. zaloguj
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/ul/li[1]/button')
        login.click()
        # 6. Akceptuj regulamin
        self.driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
        # (OSTROŻNIE!) 7. Kliknij Załóż konto, żeby wywołać informację o błędzie
        create_btn = self.driver.find_element(By.ID, "create-account")
        create_btn.click()
        sleep(4)
        # UWAGA! TU BĘDZIE TEST!
        # OCZEKIWANY REZULTAT
        # a) Szukam wszystkich elementów (informacji o błędzie użytkownika)
        errors = self.driver.find_elements(By.XPATH, '//span[@class="form-error"]')
        # b) Sprawdzam, czy jest tylko jeden taki element
        self.assertEqual(1, len(errors))
        # c) Sprawdzam poprawność treści tego komunikatu i jego widoczność
        self.assertEqual("To pole jest wymagane", errors[0].text)
        # d) Sprawdzam, czy komunikat jest pod polem imię (i nad innymi polami)
        imie_input = self.driver.find_element(By.ID, "firstname")
        errors2 = self.driver.find_elements(locate_with(By.XPATH, '//span[@class="form-error"]').near(imie_input))
        # e) Sprawdzam, czy element zawarty wewnątrz listy errors oraz errors2, to ten sam element
        self.assertEqual(errors[0].id, errors2[0].id)
        sleep(2)

