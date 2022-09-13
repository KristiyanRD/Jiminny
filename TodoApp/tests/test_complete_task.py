__author__ = 'Kristiyan Dimitrov'

"""
Тhe test is designed to check if task is marked as Completed
- Open the page
- Add multiple tasks
- Mark some task as completed
- Verify that task does not appear in Active section
- Verify that respective task is marked and moved into complete section
- Mark all tasks using mark all button
- Verify that list is marked and moved into complete section
- Clear all completed tasks using Clear completed button
- Verify that todo list is empty and not visible
"""

import random
import unittest
from Tools.file_readers import FileReader
from TodoApp.common.main_page import MainPage
from Common.driver_init import BrowserSetup

browser_data = FileReader.yaml_reader('../../Config/browser_config.yaml')
test_data = FileReader.text_reader('../tests_data/test_add_todo_data.txt')


class CompleteTask(unittest.TestCase):
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
            todo_list = 0
            for data in test_data:
                self.__class__.main_page.enter_todo(data)
                if data != '':
                    # Check if the added todo tasks are visible
                    self.assertTrue(self.__class__.main_page.is_correct_todo_added(data), '# Added tasks is not displayed!')
                    todo_list += 1
        except:
            self.driver.save_screenshot('screenshots\\test_01_add_list_of_todo.png')
            raise Exception('# FAILED: test_01_add_list_of_todo')

    def test_02_mark_single_todo_task(self):
        print('\n\ntest_02_mark_single_todo_task')
        try:    # Mark completed task anv verify if it's displayed
            self.__class__.random_choice = random.choice(test_data)
            self.__class__.main_page.click_on_completed_checkbox(self.__class__.random_choice)
            self.assertTrue(self.__class__.main_page.is_marked_as_completed_displayed(self.__class__.random_choice), '# Added tasks is not marked!')
            # Check if the todo list is the same is with the same len
            self.assertEqual(len(test_data) - 1, self.__class__.main_page.get_todo_count(), '# Added tasks are not with the same count as expected!')
            # Navigate to active section and marked task should not appear
            self.__class__.main_page.click_on_active_button()
            self.assertFalse(self.__class__.main_page.is_marked_as_completed_displayed(self.__class__.random_choice), '# Added tasks is not marked!')
            # Navigate to complete section and check if added task appear
            self.__class__.main_page.click_on_complete_button()
            self.assertTrue(self.__class__.main_page.is_marked_as_completed_displayed(self.__class__.random_choice), '# Added tasks is not marked!')

        except:
            self.driver.save_screenshot('screenshots\\test_02_mark_single_todo_task.png')
            raise Exception('# FAILED: test_02_mark_single_todo_task')

    def test_03_mark_all_and_remove_todo_tasks(self):
        print('\n\ntest_03_mark_all_and_remove_todo_tasks')
        try:    # Mark all the tasks
            self.__class__.main_page.click_on_mark_all_button()
            for data in test_data:
                self.__class__.main_page.click_on_all_button()
                if data != self.__class__.random_choice:
                    self.assertTrue(self.__class__.main_page.is_marked_as_completed_displayed(data), '# Added tasks is not marked!')
                    # Navigate to complete section and check if added task appear
                    self.__class__.main_page.click_on_complete_button()
                    self.assertTrue(self.__class__.main_page.is_marked_as_completed_displayed(data), '# Added tasks is not marked!')
            # Clear all the elements from the button
            self.__class__.main_page.click_on_clear_completed_button()
            # Check if todo list is visible
            self.assertFalse(self.__class__.main_page.is_todo_list_displayed())
        except:
            self.driver.save_screenshot('screenshots\\test_03_mark_all_and_remove_todo_tasks.png')
            raise Exception('# FAILED: test_03_mark_all_and_remove_todo_tasks')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
