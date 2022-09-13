__author__ = 'Kristiyan Dimitrov'

""" 
Тhe test is designed to check if it is possible to add new todo tasks
- Open the page
- Add multiple tasks
- Verify that every task is added successfully
- Verify todo items count 
"""

import unittest
from TodoApp.common.main_page import MainPage
from Tools.file_readers import FileReader
from Common.driver_init import BrowserSetup

browser_data = FileReader.yaml_reader('../../Config/browser_config.yaml')
test_data = FileReader.text_reader('../tests_data/test_add_todo_data.txt')


class AddTodo(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserSetup().browser_setup(url=browser_data['url'], browser=browser_data['browser'])

    def test_01_add_list_of_todo(self):
        print('\n\ntest_01_add_list_of_todo')
        try:
            main_page = MainPage(self.driver)
            for data in test_data:
                main_page.enter_todo(data)
                if data != '':
                    # Check if the added todo tasks are visible
                    self.assertTrue(main_page.is_correct_todo_added(todo_task=data), '# Added tasks is not displayed!')
            # Check if the todo list is the same is with the same len
            self.assertEqual(len(test_data), main_page.get_todo_count(), '# Added tasks are not the same as expected!')
        except:
            self.driver.save_screenshot('screenshots\\test_01_add_list_of_todo.png')
            raise Exception('# FAILED: test_01_add_list_of_todo')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
