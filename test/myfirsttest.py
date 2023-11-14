from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# Инициализация драйвера
driver = webdriver.Chrome()

try:

    # Тест 2: Чекбоксы
    driver.get("http://the-internet.herokuapp.com/checkboxes")
    checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-child")
    checkbox.click()
    driver.implicitly_wait(15)
    print("Успех по первому!")

    # Тест 3: Drag & Drop
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    source_element = driver.find_element(By.ID, "column-a")
    target_element = driver.find_element(By.ID, "column-b")
    action = ActionChains(driver)
    action.drag_and_drop(source_element, target_element).perform()
    print("Успех по второму!")
    
    # Тест 4: Выпадающее меню
    driver.get("http://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_value("2")
    print("Успех по третьему!")

finally:
    # Закрытие браузера
    driver.quit()
