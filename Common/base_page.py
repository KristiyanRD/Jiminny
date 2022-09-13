from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, *selector):
        return self.driver.find_element(*selector)

    def send_keys(self, selector, send_keys, press_enter=False):
        element = self.driver.find_element(*selector)
        element.clear()
        element.send_keys(send_keys)
        if press_enter:
            element.send_keys(Keys.ENTER)
        return element

    def visibility_of_element(self, selector):
        return self.wait.until(EC.visibility_of_element_located(selector))

    def clickable_element(self, selector):
        return self.wait.until(EC.element_to_be_clickable(selector))

    def navigate(self, url):
        self.driver.get(url)

    def click_on_element_by_script(self, element_name, *selector):
        try:
            elem = self.find_element(*selector)
            self.driver.execute_script("arguments[0].click();", elem)
            print(">> {} clicked.".format(element_name))
        except:
            print("# {} not clicked! ".format(element_name) + str(selector))
            raise

    def is_element_displayed(self, element_name, selector, msg=True):
        try:
            self.visibility_of_element(selector=selector)
            if msg:
                print(f">> {element_name} is displayed.")
        except:
            if msg:
                print(f"### {element_name, selector} is not displayed! ")
            return False
        return True

    def click_on_element(self, element_name, selector, msg=True):
        try:
            self.clickable_element(selector=selector).click()
            if msg:
                print(f">> {element_name} is clicked.")
        except:
            print(f"### {element_name, selector} is not clicked! ")
            raise