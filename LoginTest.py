import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui

# DANE TESTOWE
User = "tester284"
password = "Tester284wsb7"
search = "Pulp fiction"

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
class RegistrationTests(unittest.TestCase):
    def setUp(self):
        """Test preparation"""
        # Przygotowanie testu
        # 1a) Tworzę instancję klasy Chrome() definiuję dla niej opcje
        self.driver = webdriver.Chrome(options=chrome_options)
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        # (Przesuń kursor do lewego górnego rogu za pomocą "autogui" określając pozycję)
        pyautogui.moveTo(0, 0)
        # 1b) Otwieram stronę
        self.driver.get("https://www.filmweb.pl/")
        sleep(1)
        # (Akceptuje cookie)
        wait = WebDriverWait(self.driver, 10)
        cookie_accept = wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
        cookie_accept.click()
        sleep(1)
        # (przewija reklamę)
        wait = WebDriverWait(self.driver, 10)  # Maksymalny czas oczekiwania w sekundach
        skip_accept = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/button')))
        skip_accept.click()

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        sleep(1)
        wait = WebDriverWait(self.driver, 15)
        # 2.Wyszukuję i klikam przycisk "zaloguj1"
        zaloguj_a = wait.until(EC.presence_of_element_located((By.ID, "main-header_login-link")))
        zaloguj_a.click()
        sleep(1)
        # 2.Klikam przycisk "zaloguj2"
        zaloguj_b = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[2]/div/div/div[1]/div/div/ul/li[2]/a/div[2]')))
        zaloguj_b.click()
        sleep(1)
        # 3. Wprowadzanie danych
        # Odszukaj, wpisz
        User_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[1]/input')
        User_input.send_keys(User)
        # 4. Wpisz hasło
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[2]/input')
        password_input.send_keys(password)

        # 5. Zaloguj
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/ul/li[1]/button')
        login.click()
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        # 6. Przewijam "reklamę"
        OK = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[3]/button')))
        OK.click()
        sleep(2)
        # 7. Wyszukaj film
        wait = WebDriverWait(self.driver, 15)
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'inputSearch')))
        search_input.send_keys(search)
        ### TEST ####


        sleep(15)
        self.driver.quit()