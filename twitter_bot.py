from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def twitter_task(tweet_url):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        print("[INFO] Memulai tugas Twitter.")
        driver.get("https://twitter.com/login")

        # Tunggu dan masukkan username menggunakan XPath yang Anda berikan
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input"))
        )
        driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input").send_keys("krmnlim")

        # Tunggu dan masukkan password menggunakan XPath yang Anda berikan
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
        )
        driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys("karmin123@")

        # Klik tombol login
        login_button_xpath = "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span"
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
