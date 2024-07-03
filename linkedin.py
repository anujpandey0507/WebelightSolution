from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


class Linkedin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://in.linkedin.com/")
        time.sleep(5)

    def test_signup(self):
        self.driver.find_element(By.XPATH, "//a[@class='nav__button-tertiary btn-md btn-tertiary']").click()
        time.sleep(2)
        mail = self.driver.find_element(By.XPATH, "//input[@id='email-or-phone']")
        mail.click()
        mail.send_keys("john@mailinator.com")
        password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        password.click()
        password.send_keys("m2n1nm")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//button[@id='join-form-submit']").click()
        time.sleep(7)
        try:
            alt = self.driver.find_element(By.XPATH, "//p[@class='input-helper-error artdeco-inline-feedback__message']")
            if alt.is_displayed():
                print(alt.text)
        except NoSuchElementException :
            first_name = self.driver.find_element(By.XPATH, "//input[@id='first-name']")
            first_name.click()
            first_name.send_keys("John")
            last_name = self.driver.find_element(By.XPATH, "//input[@id='last-name']")
            last_name.click()
            last_name.send_keys("Deo")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//button[@id='join-form-submit']").click()
            time.sleep(7)
            try:
                alt_2 = self.driver.find_element(By.XPATH, "//p[@class='input-helper-error artdeco-inline-feedback__message']")
                if alt_2.is_displayed():
                    print(alt_2.text)
            except NoSuchElementException:
                time.sleep(15)
                print("Showing human verification which is not possible to automate.")


if __name__ == "__main__":
    unittest.main()

