__author__ = 'Kristiyan Dimitrov'

"""
Тhe test is designed to check if it is possible to remove todo tasks
- Open the page
- Add multiple tasks
- Remove random todo task from the list
- Verify that particular task is removed
- Verify that the rest of the tasks are not being removed
- Remove all todo tasks
- Verify that list is empty
"""

import random
import unittest
from Tools.file_readers import FileReader
from TodoApp.common.main_page import MainPage
from Common.driver_init import BrowserSetup

browser_data = FileReader.yaml_reader('../../Config/browser_config.yaml')
test_data = FileReader.text_reader('../tests_data/test_add_todo_data.txt')


class RemoveTodo(unittest.TestCase):
    driver = None
    main_page = None
    random_choice = None

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserSetup().browser_setup(url=browser_data['url'], browser=browser_data['browser'])

    def test_01_add_list_of_todo(self):
        print('\n\ntest_01_add_list_of_todo')
        try:
            self.__class__.main_page = MainPage(self.driver)
            for data in test_data:
                self.__class__.main_page.enter_todo(data)
                if data != '':
                    # Check if the added todo tasks are visible
                    self.assertTrue(self.__class__.main_page.is_correct_todo_added(data), '# Added tasks is not displayed!')
        except:
            self.driver.save_screenshot('screenshots\\test_01_add_list_of_todo.png')
            raise Exception('# FAILED: test_01_add_list_of_todo')

    def test_02_remove_single_todo_task(self):
        print('\n\ntest_02_remove_single_todo_task')
        try:    # Chose one of the added tasks and verify if it's removed
            self.__class__.random_choice = random.choice(test_data)
            self.__class__.main_page.click_on_remove_single_todo_button(self.__class__.random_choice)
            self.assertFalse(self.__class__.main_page.is_correct_todo_added(self.__class__.random_choice), '# Added tasks is not displayed!')
            # Check if the rest ot the tasks are still there
            for data in test_data:
                # Check if the added todo tasks are visible
                if data != self.__class__.random_choice:
                    self.assertTrue(self.__class__.main_page.is_correct_todo_added(data), '# Added tasks is not displayed!')
            # Check if the todo list decrease
            self.assertEqual(len(test_data) - 1, self.__class__.main_page.get_todo_count(), '# Added tasks are not the same as expected!')
        except:
            self.driver.save_screenshot('screenshots\\test_02_remove_single_todo_task.png')
            raise Exception('# FAILED: test_02_remove_single_todo_task')

    def test_03_remove_all_todo_tasks(self):
        print('\n\ntest_03_remove_all_todo_tasks')
        try:
            for data in test_data:
                # Remove all added todo tasks
                if data != self.__class__.random_choice:
                    self.__class__.main_page.click_on_remove_single_todo_button(data)
                # Check if todo list is visible
            self.assertFalse(self.__class__.main_page.is_todo_list_displayed())
        except:
            self.driver.save_screenshot('screenshots\\test_03_remove_all_todo_tasks.png')
            raise Exception('# FAILED: test_03_remove_all_todo_tasks')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
