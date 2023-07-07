import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #web driver wait
import pyautogui

# DANE TESTOWE
User = "tester284"
password = "Tester284wsb7"
search = "Pulp fiction"
pyautogui.FAILSAFE = False
scroll_amount = 100  # Ilość pikseli do przewinięcia w jednym kroku
scroll_iterations = 4  # Ilość kroków przewijania
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

class LoginTest(unittest.TestCase):
    def setUp(self):
        """Test preparation"""
        # Przygotowanie testu
        # a) Tworzę instancję klasy Chrome() definiuję dla niej opcje
        self.driver = webdriver.Chrome(options=chrome_options)
        # (Zmaksymalizuj okno)
        self.driver.maximize_window()
        # (Przesuń kursor do lewego górnego rogu za pomocą "autogui" określając pozycję)
        pyautogui.moveTo(0, 0)
        # b) Otwieram stronę
        self.driver.get("https://www.filmweb.pl/")
        time.sleep(3)
        # (Akceptuje cookie)
        wait = WebDriverWait(self.driver, 10) #### opoźniam działanie sterownika WEB DRIVER - Maksymalny czas oczekiwania w sekundach
        cookie_accept = wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
        cookie_accept.click()
        time.sleep(3)
        # (przewija reklamę)

    def tearDown(self):
        # Wyłącz przeglądarkę
        self.driver.quit()

    def testNoNameEntered(self):
        # KROKI
        time.sleep(3)
        wait = WebDriverWait(self.driver, 10)
        # 1.Wyszukuję i klikam przycisk "zaloguj1"
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
        time.sleep(8)
        wait = WebDriverWait(self.driver, 10)
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'inputSearch')))
        search_input.send_keys(search, Keys.ENTER)
        time.sleep(5)
        for _ in range(scroll_iterations): ## opóźnienie scrolowania w postaci pętli
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount})")
            time.sleep(0.9)  # Odstęp między kolejnymi krokami

        ### TEST ####

        # a) sprawdź czy udało się wyszukać właściwy film.
        # Jeśli element nie jest widoczny, zostanie wywołany błąd z komunikatem "The results not visible".

        wait = WebDriverWait(self.driver, 10)
        next_results = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[2]/section/div/div')))
        self.assertTrue(next_results.is_displayed(), "The results not visible")

        # b) Sprawdź czy film jest pierwszy w kolejce wyszukiwania :

        search_bar = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[2]/section/div/div[1]/div[1]/div')))
        self.assertTrue(locate_with(By.XPATH, '//*[@id="site"]/div[3]/div[2]/div/div[2]/section/div/div').near(search_bar))

        # c) Sprawdź czy imię aktora "John Travolta" wystepuje i czy więcej niz raz :
        starring = self.driver.find_elements(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[2]/section/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/h3[1]/a/span')
        self.assertEqual("John Travolta", starring[0].text)
        self.assertEqual(1, len(starring))

        ###################################################################
        time.sleep(5)
        self.driver.quit()
