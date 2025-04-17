# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver ()
# driver = webdriver.Chrome() # For Chrome
driver = webdriver.Safari()  # For Safari

# Open the Google homepage
driver.get("https://www.google.com")


# Wait for the page to load (s)
time.sleep(0.5)

# Find the search box element on the page by its name attribute
search_box = driver.find_element(By.NAME, "q")


# Type a search query into the search box
search_box.send_keys("Selenium Python tutorial")

# Simulate pressing the 'Enter' key to submit the search
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)

# Close the browser window
driver.quit()
