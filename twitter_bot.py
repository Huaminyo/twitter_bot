from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def twitter_task(tweet_url):
    driver = webdriver.Chrome()

    try:
        print("[INFO] Memulai tugas Twitter.")
        driver.get("https://twitter.com/login")

        # Tunggu dan klik tombol Sign In
        sign_in_button_xpath = "//*[@data-testid='loginButton']"  # Coba menggunakan atribut data-testid
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath))
        )
        driver.find_element(By.XPATH, sign_in_button_xpath).click()

        # Tunggu sampai elemen username tersedia dan input username
        username_xpath = "//*[@name='session[username_or_email]']"  # Gunakan name attribute
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, username_xpath))
        )
        driver.find_element(By.XPATH, username_xpath).send_keys("krmnlim")

        # Tunggu sampai elemen password tersedia dan input password
        password_xpath = "//*[@name='session[password]']"  # Gunakan name attribute
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, password_xpath))
        )
        driver.find_element(By.XPATH, password_xpath).send_keys("karmin123@")
        
        # Klik tombol login
        login_button_xpath = "//span[contains(text(),'Log in')]"  # Gunakan teks tombol login
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, login_button_xpath))
        )
        driver.find_element(By.XPATH, login_button_xpath).click()

        print("[INFO] Berhasil login sebagai krmnlim.")
        time.sleep(5)

        # Akses URL tweet
        driver.get(tweet_url)
        print(f"[INFO] Membuka URL tweet: {tweet_url}.")
        time.sleep(3)

        # Klik tombol retweet
        retweet_button_xpath = "//div[@data-testid='retweet']"
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, retweet_button_xpath))
        )
        driver.find_element(By.XPATH, retweet_button_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@data-testid='retweetConfirm']").click()

        # Klik tombol like
        like_button_xpath = "//div[@data-testid='like']"
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, like_button_xpath))
        )
        driver.find_element(By.XPATH, like_button_xpath).click()

        print("[INFO] Tugas Twitter selesai.")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
    finally:
        driver.quit()
        print("[INFO] Menutup driver.")

# =================== MAIN FUNCTION ===================
if __name__ == "__main__":
    TWEET_URL = "https://x.com/NewTread_/status/1882458950790205638"  # URL tweet yang diberikan
    print("[INFO] Memulai tugas Twitter.")
    twitter_task(TWEET_URL)
    print("[INFO] Tugas Twitter selesai.")
