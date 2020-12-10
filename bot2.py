from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pydub.playback import play
import time
from playsound import playsound

path = "C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.reg.uci.edu/perl/WebSoc")
print(driver.title)

select_dept = Select(driver.find_element_by_name("Dept"))
select_dept.select_by_value('COMPSCI')

course_num = driver.find_element_by_name("CourseNum")
course_num.send_keys("175")
course_num.send_keys(Keys.RETURN)

sonar_sound = "sonar.wav"
open_sound = "classOpen.mp3"

active_counter = 0
while True:
    if active_counter == 50:
        print('active')
        active_counter = 0
    availability = driver.find_element_by_xpath(
        "//table[1]/tbody[1]/tr[9]/td[17]")
    if availability.text == "OPEN":
        playsound(open_sound)
        print('CLASS IS OPEN')
        break
    active_counter += 1
    time.sleep(6)
    driver.refresh()
driver.quit()
