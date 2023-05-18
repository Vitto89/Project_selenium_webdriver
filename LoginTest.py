import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from time import sleep

# DANE TESTOWE
User = "tester284"
email = "tester284@o2.pl"
password = "Tester284wsb7"
search = "Pulp fiction"
comment = "Super"


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
        sleep(1)
        cookie_accept = self.driver.find_element(By.ID, "didomi-notice-agree-button")
        cookie_accept.click()
        skip_accept = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/button')
        skip_accept.click()


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
        # 6. Wyszukaj film
        sleep(2)
        search_input = self.driver.find_element(By.ID, 'inputSearch')
        search_input.send_keys(search)
        sleep(2)
        choose = self.driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[1]/div[1]/div[3]/div[2]/div[1]/a/div/img')
        choose.click()
        rate = self.driver.find_element(By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[4]/section/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/a[10]')
        rate.click()
        comment = self.driver.find_element(By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[4]/section/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/a')
        comment.send_keys(comment)
        comment.send_keys(Keys.RETURN)
        sleep(2)
        driver.quit()
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

