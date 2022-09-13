from TodoApp.common_selectors.main_page_selectors import MainsPageSelectors
from Common.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def enter_todo(self, todo=''):
        self.send_keys(MainsPageSelectors.TODO_FIELD, todo, press_enter=True)

    def click_on_all_button(self):
        self.click_on_element('Continue button', MainsPageSelectors.All_BUTTON)

    def click_on_active_button(self):
        self.click_on_element('Active button', MainsPageSelectors.ACTIVE_BUTTON)

    def click_on_complete_button(self):
        self.click_on_element('Complete button', MainsPageSelectors.COMPLETED_BUTTON)

    def click_on_clear_completed_button(self):
        self.click_on_element('Clear completed button', MainsPageSelectors.CLEAR_COMPLETED_BUTTON)

    def click_on_mark_all_button(self):
        self.click_on_element('Mark all button', MainsPageSelectors.MARK_ALL)

    def click_on_remove_single_todo_button(self, remove_single_task):
        selector = (MainsPageSelectors.REMOVE_SINGLE_TODO[0], str(MainsPageSelectors.REMOVE_SINGLE_TODO[1]).format(remove_single_task))
        return self.click_on_element_by_script(f'Remove single todo task: {remove_single_task}', *selector)

    def click_on_completed_checkbox(self, completed_checkbox):
        selector = (MainsPageSelectors.CHECKBOX[0], str(MainsPageSelectors.CHECKBOX[1]).format(completed_checkbox))
        return self.click_on_element_by_script(f'Checkbox {completed_checkbox}', *selector)

    def get_todo_count(self):
        todo_count = self.find_element(*MainsPageSelectors.TODO_COUNT).text
        numbers = int(''.join(filter(str.isdigit, todo_count)))
        return numbers

    def get_links_from_page(self, link_name):
        if link_name.lower() == 'written by':
            link_name = 'Evan You'
        elif link_name.lower() == 'part of':
            link_name = 'TodoMVC'
        selector = (MainsPageSelectors.MAJORITY_OF_THE_LINKS[0], str(MainsPageSelectors.MAJORITY_OF_THE_LINKS[1]).format(link_name))
        link = self.visibility_of_element(selector).get_attribute('href')
        return link

    def is_marked_as_completed_displayed(self, completed_task):
        selector = (MainsPageSelectors.TODO_COMPLETED[0], str(MainsPageSelectors.TODO_COMPLETED[1]).format(completed_task))
        return self.is_element_displayed(f'Marked as completed task: {completed_task}', selector)

    def is_correct_todo_added(self, todo_task, msg=True):
        selector = (MainsPageSelectors.ADDED_TODO[0], str(MainsPageSelectors.ADDED_TODO[1]).format(todo_task))
        return self.is_element_displayed(f'Added task is: {todo_task}', selector, msg=msg)

    def is_todo_list_displayed(self):
        return self.is_element_displayed('Todo list', MainsPageSelectors.TODO_LIST)

