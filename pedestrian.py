# Imports
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

global count
count = 0

# Chrome Driver
driver = webdriver.Chrome()

# Navigate to Google Maps
driver.get("https://www.google.com/maps")
assert "Google Maps" in driver.title

# Sleep momentarily
sleep(5)

# Select the search box, send desired location. 
search = driver.find_element(By.CSS_SELECTOR, "#searchboxinput")
search.clear()
search.send_keys("Broadway, New York, New York")
search.send_keys(Keys.RETURN)

# Sleep momentarily
sleep(7)

# Select and click on the street view button
toggleStreetView = driver.find_element(By.CSS_SELECTOR, ".q2sIQ")
toggleStreetView.click()

# Sleep momentarily
sleep(3)

# Select and click on the map canvas 
canvas = driver.find_element(By.CSS_SELECTOR, ".widget-scene-canvas")
canvas.click()

# Sleep momentarily
sleep(3)

# Driver action chain to manipulate the map canvas
actions =  ActionChains(driver)

# Pull values of street number and name, city name, state name, URL, and Lat Long
streetName = driver.find_element(By.CSS_SELECTOR, ".BDkzx").text
cityState = driver.find_element(By.CSS_SELECTOR, ".tJri0").text
cityName = cityState.split(",")[0]
stateName = cityState.split(", ")[-1]
url = driver.current_url
latitude = url[29:38]
longitude = url[40:51]

# Check values
print(streetName)
print(cityName)
print(stateName)
print(latitude)
print(longitude)
print(url)


# Function to take a screenshot of the map canvas, then pan the point of view. 
def snapAndPan(count):
        counter = count 
        canvas.screenshot("C:/Users/tkenn/Documents/VS_Code_Projects/walkerBTS/Screenshots/"+streetName+"_"+str(counter)+".png")
        actions.key_down(Keys.ARROW_LEFT)
        actions.pause(1.20)
        actions.key_up(Keys.ARROW_LEFT)
        actions.pause(1.20)
        actions.perform()

# Function to move the point of view down the road
def walk(count):
        counter = count 
        sleep(3)
        canvas.screenshot("C:/Users/tkenn/Documents/VS_Code_Projects/walkerBTS/Screenshots/"+streetName+"_"+str(counter)+".png")
        actions.key_down(Keys.ARROW_UP)
        actions.pause(1.20)
        actions.key_up(Keys.ARROW_UP)
        actions.perform()

# Driver function 
def Surveil():
        sleep(10)
        counter = 1
        snapAndPan(counter)
        counter += 1
        snapAndPan(counter)
        counter += 1
        snapAndPan(counter)
        counter += 1
        snapAndPan(counter)
        counter += 1
        snapAndPan(counter)
        walk(counter)

Surveil()

driver.close()