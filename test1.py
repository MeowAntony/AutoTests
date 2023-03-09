import time
import unittest
from win32api import GetSystemMetrics
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_src = '.\\driver\\chromedriver.exe'


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_src)

    def test_search_wikipedia(self):
        url = "https://www.wikipedia.org/"
        driver = self.driver
        driver.get(url)
        self.assertIn("Wikipedia", driver.title)  # проверка, что мы попали на вебсайт Wikipedia

        search_box = driver.find_element(value="searchInput")
        search_box.send_keys("Пушка")
        search_box.send_keys(Keys.ENTER)

        name_box = driver.find_element(by=By.CLASS_NAME, value="mw-page-title-main")
        self.assertIn("Пушка", name_box.text)  # проверка, что мы попали на нужную нам страницу

    def test_search_google(self):
        url = "https://www.google.com"

        driver = self.driver
        driver.get(url)

        self.assertIn("Google", driver.title)  # проверка, что мы попали на вебсайт Google

        search = driver.find_element(by=By.CLASS_NAME, value="gLFyf")
        search.send_keys("PSY - GANGNAM STYLE")
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        name_music = driver.find_element(by=By.CLASS_NAME, value="yKMVIe")
        self.assertIn("Gangnam Style", name_music.text)  # проверка, что мы попали на нужную страницу в гугле

    def test_account_log_out_stackoverflow(self):
        url = "https://stackoverflow.com/"
        username = ""  # вводить свои значения для входа
        password = ""  # вводить свои значения для входа
        driver = self.driver
        driver.get(url)
        driver.set_window_size(GetSystemMetrics(0), GetSystemMetrics(1))
        self.assertIn("Stack Overflow", driver.title)  # проверка, что мы попали на вебсайт Stack Overflow

        button_login = driver.find_element(by=By.XPATH, value="//a[@data-gps-track='login.click']")
        button_login.click()
        time.sleep(1)

        email_text = driver.find_element(value="email")
        email_text.send_keys(username)

        password_text = driver.find_element(value="password")
        password_text.send_keys(password)

        button_submit = driver.find_element(value="submit-button")
        button_submit.click()
        time.sleep(1)

        button_list = driver.find_element(by=By.XPATH, value="//a[@data-gps-track='site_switcher.show']")
        button_list.click()
        time.sleep(1)

        button_log_out = driver.find_element(by=By.XPATH, value="//div[@class='related-links']/a[3]")
        button_log_out.click()
        time.sleep(3)


        button_log_out2 = driver.find_element(by=By.XPATH, value="//button[text()='Log out']")
        time.sleep(1)
        button_log_out2.click()
        time.sleep(1)

        button_login = driver.find_element(by=By.XPATH, value="//a[@data-gps-track='login.click']")
        self.assertIn("Log in", button_login.text)  # проверка, что мы вышли и можем заново зайти

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
