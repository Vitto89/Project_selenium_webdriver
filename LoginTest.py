import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui

# DANE TESTOWE
User = "tester284"
password = "Tester284wsb7"
search = "Pulp fiction"
comment = "Super"

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
class RegistrationTests(unittest.TestCase):
    def setUp(self):
        """Test preparation"""
        # Przygotowanie testu
        # 1. Otwarta strona główna
        # 1a) Tworzę instancję klasy Chrome()
        self.driver = webdriver.Chrome(options=chrome_options)
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        pyautogui.moveTo(0, 0)
        # 1b) Otwieram stronę główną
        self.driver.get("https://www.filmweb.pl/")
        sleep(1)
        cookie_accept = self.driver.find_element(By.ID, "didomi-notice-agree-button")
        cookie_accept.click()
        wait = WebDriverWait(self.driver, 4)  # Maksymalny czas oczekiwania w sekundach
        skip_accept = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/button')))
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
        sleep(2)
        wait = WebDriverWait(self.driver, 5)
        OK = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[3]/button')))
        OK.click()
        # 6. Wyszukaj film
        wait = WebDriverWait(self.driver, 5)
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'inputSearch')))
        search_input.send_keys(search)
        sleep(1)
        wait = WebDriverWait(self.driver, 5)
        choose = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div/div/div[1]/div[1]/div[3]/div[2]/div[1]/a/div/img')))
        choose.click()
        self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0,3)")
        rate = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[4]/section/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/a[10]')))
        rate.click()
        sleep(2)
        comment = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[4]/section/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div/div/a')))
        sleep(2)
        comment.click()
        comment.send_keys(comment)
        comment.send_keys(Keys.RETURN)
        sleep(4)
        self.driver.quit()