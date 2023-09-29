from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.properati.com.ec/s/quito/departamento/alquiler")
lista = driver.find_elements(By.CLASS_NAME, "listing")
for f in lista:
    price = f.find_element(by=By.CLASS_NAME, value="price").text
    location = f.find_element(by=By.CLASS_NAME, value="listing-card__location").text
    rooms = f.find_element(by=By.CLASS_NAME, value="listing-card__properties").text
    ven = f.find_element(by=By.CLASS_NAME, value="listing-card__publication-info").text

    print(price)
    print(location)
    print(rooms)
    print(ven)
    print("=" * 40)



#elem = driver.find_element(By.NAME, "q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()