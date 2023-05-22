import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from time import sleep
import pyautogui

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
class RegistrationTests(unittest.TestCase):
    def setUp(self):
        """Test preparation"""
        # Przygotowanie testu
        # 1. Otwarta strona główna
        # 1a) Tworzę instancję klasy Chrome() definiuję dla niej opcje.
        self.driver = webdriver.Chrome(options=chrome_options)
        # (definiuje obiekt z Poliskim dostawcą danych biblioteki Faker)
        self.fake = Faker("pl_Pl")
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        # (Przesuń kursor do lewego górnego rogu za pomocą "autogui" określając pozycję)
        pyautogui.moveTo(0, 0)
        # 1b) Otwieram stronę główną
        self.driver.get("https://www.filmweb.pl/")
        sleep(1)
        # ( "Wstrzymywanie" WEB DRIVER'A w celu oczekiwania na pojawienie się elementów na stronie)
        wait = WebDriverWait(self.driver, 10)
        # (Akceptuje cookie)
        cookie_accept = wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
        cookie_accept.click()
        sleep(1)
        wait = WebDriverWait(self.driver, 10)  # Maksymalny czas oczekiwania w sekundach
        # (przewija reklamę)
        skip_accept = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/button')))
        skip_accept.click()
        sleep(1)

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        sleep(1)
        wait = WebDriverWait(self.driver, 15)
        # Wyszukuję i klikam przycisk "zaloguj1"
        zaloguj_a = wait.until(EC.presence_of_element_located((By.ID, "main-header_login-link")))
        zaloguj_a.click()
        sleep(1)
        wait = WebDriverWait(self.driver, 15)
        # Klikam przycisk "zaloguj2"
        zaloguj_b = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[2]/div/div/div[1]/div/div/ul/li[2]/a/div[2]')))
        zaloguj_b.click()
        sleep(1)
        # Wprowadzanie danych(sztucznie generowanych) z wykorzystaniem biblioteki "FAKER"
        User_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[1]/input')
        User_input.send_keys(self.fake.email())
        sleep(1)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[2]/input')
        password_input.send_keys(self.fake.password())
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/ul/li[1]/button')
        login.click()
        sleep(10)
        ### test ###
        # Szukam wszystkich elementów (informacji o błędzie użytkownika)
        errors = self.driver.find_elements(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[3]')
        self.assertEqual(1, len(errors))
        self.assertEqual("błędny e-mail lub hasło", errors[0].text)
        sleep(10)
        self.driver.quit()