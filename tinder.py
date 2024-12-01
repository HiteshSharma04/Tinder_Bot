from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
EMAIL = "email@urs.com"
PASS = "pass"
ADD = "https://tinder.com/"

driver.get(ADD)

try:
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q1747300428"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div'))
    )
    login_button.click()
    print("Login button clicked successfully!")
except Exception as e:
    print("Login button click failed:", e)

try:
    more = WebDriverWait(driver, 10)
    option = more.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q18919352"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/button'))
    )
    option.click()
    print("Option button clicked successfully!")
except Exception as e:
    print("Option button click failed:", e)

time.sleep(2)

try:
    dec = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q18919352"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]/div'))
    )
    dec.click()
    print("Dec button clicked successfully!")
except Exception as e:
    print("Dec button click failed:", e)

try:
    fb_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q18919352"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]'))
    )
    fb_login.click()
    print("Facebook login button clicked successfully!")
    
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print("Switched to Facebook login window!")
except Exception as e:
    print("Facebook login button click or window switch failed:", e)

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    email_input.send_keys(EMAIL)
    print("Email entered successfully!")

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pass'))
    )
    password_input.send_keys(PASS, Keys.ENTER)
    print("Password entered successfully!")
except Exception as e:
    print("Failed during Facebook login process:", e)

time.sleep(3)

# Attempt post-login interaction within Facebook window
try:
    post_login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_7N"]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div'))
    )
    post_login_button.click()
    print("Post-Facebook login button clicked successfully!")
    WebDriverWait(driver, 20).until(EC.title_contains("Tinder"))
except Exception as e:
    print("Post-Facebook login button click failed:", e)

# Switch back to Tinder's main window
try:
    driver.switch_to.window(driver.window_handles[0])
    print(f"Switched back to main Tinder window: {driver.title}")
except Exception as e:
    print("Failed to switch back to main Tinder window:", e)

try:
    allow_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q18919352"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]'))
    )
    allow_button.click()
    print("Allow button clicked successfully!")
except Exception as e:
    print("Allow button click failed:", e)

try:
    notify_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q18919352"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]'))
    )
    notify_button.click()
    print("Notify button clicked successfully!")
except Exception as e:
    print("Notify button click failed:", e)

time.sleep(20)

for n in range(100):
    time.sleep(1)
    try:
        info_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="q1747300428"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[2]/button/div/div/div/div/div[1]/div'))
        )
        driver.execute_script("arguments[0].click();", info_button)
    except Exception as e:
        print("drop", e)

    try:
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="q1747300428"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[2]/div/div/div[4]/button'))
        )
        driver.execute_script("arguments[0].click();", like_button)
    except Exception as e:
        print("cry", e)
        

driver.quit()
