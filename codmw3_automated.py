# This is a piece of code to automate the collection of daily login rewards for Call of Duty: Modern Warfare 3 (2023) using python
# It can be altered for any game by chnaging the launcher/path in the subprocess line
# random delays are added in case the game's anticheat system flags the robotic input
# run "pip install pyautogui" in your system in case you don't have this module installed before running this program



import pyautogui as pao
import time
import random
import schedule
import subprocess

# Function to add random delays
def random_delay(min_seconds, max_seconds):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

# Function to automate the login process and collect rewards
def login_and_collect_rewards():
    # Launch Battle.net launcher
    subprocess.Popen(r"C:\Program Files (x86)\Battle.net\Battle.net Launcher.exe") # the path to the battle.net launcher may be different in your system
    time.sleep(30)  # Wait for the Battle.net launcher to load

    # Adjust coordinates and timing as per your screen resolution and launcher UI (mine was 1920*1080 scaled at 125% for reference)
    # In order to get the coordiantes of your cursor you will require 3rd party software; I used "Mpos"

    # Click on the username field
    pao.click(x=1245, y=474)
    random_delay(1, 2)

    # Enter username
    pao.typewrite('your_username')
    random_delay(2, 3)

    # Click on the password field
    pao.click(x=1147, y=406)
    random_delay(1, 2)

    # Enter password
    pao.typewrite('your_password')
    random_delay(2, 3)

    # Click on the login button
    pao.click(x=1232, y=553)
    random_delay(10, 15)

    # Click on the Call of Duty icon
    pao.click(x=231, y=182)
    random_delay(5, 10)

    # Click on the Play button
    pao.click(x=263, y=907)
    random_delay(60, 90)  # Wait for the game to load

    # Press 'Return' to accept rewards
    pao.press('return')
    random_delay(15, 20)

    # Press 'Return' again if required
    pao.press('return')
    random_delay(180, 240)  # Wait for the rewards collection process to complete/save

    # Close the game
    pao.hotkey('alt', 'f4')

    # Close the game
    pao.hotkey('alt', 'f4')

# Schedule the script to run every 24 hours at a specified time
schedule.every().day.at("10:00").do(login_and_collect_rewards)

while True:
    schedule.run_pending()
    time.sleep(1)

# I will be updating the code to handle instance of failed login and other errors by comparing the screenshot of a succesful login to the live image on the screen soon
