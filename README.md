# Project_selenium_webdriver


Aby uruchomić test korzystający z Selenium w Pythonie, potrzebujesz następujących bibliotek:

**Time**: Biblioteka do zarządzania czasem, która umożliwia oczekiwanie na określony czas w testach.

**Unittest**: Framework do tworzenia i uruchamiania testów jednostkowych w Pythonie.

**Selenium**: Główna biblioteka, która zapewnia interakcję z przeglądarką internetową. Potrzebujesz jej modułów webdriver, Keys i chrome.options.

**Selenium.webdriver.common.by**: Moduł umożliwiający identyfikację elementów na stronie za pomocą różnych strategii wyszukiwania, takich jak By.ID, By.CLASS_NAME, itp.

**Selenium.webdriver.support.relative_locator:** Moduł umożliwiający odnalezienie elementu względem innego elementu na stronie za pomocą metody locate_with.

**Selenium.webdriver.support.ui.WebDriverWait:** Klasa do oczekiwania na określone warunki (np. element widoczny, klikalny) na stronie internetowej.

**Selenium.webdriver.support.expected_conditions:** Moduł zawierający różne warunki, które można sprawdzać za pomocą WebDriverWait, np. EC.presence_of_element_located, EC.visibility_of_element_located, itp.

**Pyautogui:** Biblioteka do automatyzacji interakcji z klawiaturą i myszą. Może być przydatna w niektórych przypadkach, gdy standardowe metody Selenium są niewystarczające.
