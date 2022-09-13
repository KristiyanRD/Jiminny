from selenium import webdriver


class BrowserSetup:

    @staticmethod
    def browser_setup(url, browser='Chrome', windows_maximize=True):
        if browser.lower() in ('chrome', 'ch'):
            driver = webdriver.Chrome()
        elif browser.lower() in ('firefox', 'ff'):
            driver = webdriver.Firefox()
        else:
            raise Exception(f'Selected browser is incorrect: {browser}')

        if windows_maximize:
            driver.maximize_window()

        if url == '' or url is None:
            raise Exception(f'Wrong url provided: {url}')
        else:
            driver.get(url)
        print(f'Browser: {browser}\nURL: {url}')
        return driver
