import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# DANE TESTOWE
User = "tester284"
password = "Tester284wsb7"
search = "Pulp fiction"
scroll_amount = 100  # Ilość pikseli do przewinięcia w jednym kroku
scroll_iterations = 10  # Ilość kroków przewijania
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
        time.sleep(3)
        # (Akceptuje cookie)
        wait = WebDriverWait(self.driver, 10)
        cookie_accept = wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
        cookie_accept.click()
        time.sleep(3)
        # (przewija reklamę)
        wait = WebDriverWait(self.driver, 10)  # Maksymalny czas oczekiwania w sekundach
        skip_accept = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/button')))
        skip_accept.click()

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        # 2.Wyszukuję i klikam przycisk "zaloguj1"
        zaloguj_a = wait.until(EC.presence_of_element_located((By.ID, "main-header_login-link")))
        zaloguj_a.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        # 2.Klikam przycisk "zaloguj2"
        zaloguj_b = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[2]/div/div/div[1]/div/div/ul/li[2]/a/div[2]')))
        zaloguj_b.click()
        # 3. Wprowadzanie danych
        # Odszukaj, wpisz
        time.sleep(1)
        User_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[1]/input')
        User_input.send_keys(User)
        # 4. Wpisz hasło
        time.sleep(1)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[2]/input')
        password_input.send_keys(password)
        # 5. Zaloguj
        time.sleep(1)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/ul/li[1]/button')
        login.click()
        # 7. Wyszukaj film
        time.sleep(6)
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'inputSearch')))
        search_input.send_keys(search, Keys.ENTER)
        time.sleep(5)
        for _ in range(scroll_iterations):
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount})")
            time.sleep(0.9)  # Odstęp między kolejnymi krokami
        ### TEST ####
        # a)
        wait = WebDriverWait(self.driver, 10)
        next_results = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[2]/section/div/div')))
        self.assertTrue(next_results.is_displayed(), "The results not visible")
        self.driver.quit()