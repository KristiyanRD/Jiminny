__author__ = 'Kristiyan Dimitrov'

"""
Тhe test is designed to verify the links from the page 
- Open the page
- Verify that the list with the links is the same like this from the page
"""

import unittest
from Tools.file_readers import FileReader
from Common.driver_init import BrowserSetup
from TodoApp.common.main_page import MainPage

browser_data = FileReader.yaml_reader('../../Config/browser_config.yaml')
test_data = FileReader.yaml_reader('../tests_data/link_verification.yaml')


class LinkVerification(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserSetup().browser_setup(url=browser_data['url'], browser=browser_data['browser'])

    def test_01_verify_all_links(self):
        print('\n\ntest_01_verify_all_links')
        global name, link, link_from_page, driver

        msg = ''
        for name, link in dict(test_data).items():
            link_from_page = MainPage(self.driver).get_links_from_page(name)
            if link == link_from_page:
                print(f'Name: {name}\nLink from source: {link}\nLink from page:   {link_from_page}\n')
            else:
                msg += f'Name: {name}\nLink from source: {link}\nLink from page:   {link_from_page}\n'

        if msg != '':
            self.driver.save_screenshot('screenshots\\test_01_verify_all_links.png')
            raise Exception('Link differences\n' + msg)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
