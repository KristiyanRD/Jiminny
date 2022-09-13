from selenium.webdriver.common.by import By


class MainsPageSelectors:

    TODO_FIELD = (By.CLASS_NAME, "new-todo")
    TODO_COUNT = (By.CLASS_NAME, "todo-count")
    TODO_LIST = (By.CLASS_NAME, "todo-list")
    All_BUTTON = (By.XPATH, "//a[contains(text(),'All')]")
    ACTIVE_BUTTON = (By.XPATH, "//a[contains(text(),'Active')]")
    COMPLETED_BUTTON = (By.XPATH, "//a[contains(text(),'Completed')]")
    CLEAR_COMPLETED_BUTTON = (By.XPATH, "//button[contains(text(),'Clear completed')]")
    MARK_ALL = (By.XPATH, "//label[contains(text(),'Mark all as complete')]")
    # Parametrised selectors
    CHECKBOX = (By.XPATH, "//label[contains(text(),'{}')]/../input")
    ADDED_TODO = (By.XPATH, "//label[contains(text(),'{}')]")
    REMOVE_SINGLE_TODO = (By.XPATH, "//label[contains(text(),'{}')]/../button")
    TODO_COMPLETED = (By.XPATH, "//*[@class='todo completed']//label[contains(text(),'{}')]/../..")
    # Links
    MAJORITY_OF_THE_LINKS = (By.XPATH, "//a[contains(text(),'{}')]")
