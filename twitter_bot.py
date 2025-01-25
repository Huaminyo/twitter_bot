from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def twitter_task(tweet_url):
    # Inisialisasi WebDriver
    driver = webdriver.Chrome()  # Pastikan Anda sudah menginstal ChromeDriver

    try:
        print(f"[INFO] Memulai tugas Twitter.")
        print("[INFO] Login ke akun Twitter...")

        # Input username dan password langsung
        driver.get("https://twitter.com/login")
        time.sleep(2)

        driver.find_element("name", "session[username_or_email]").send_keys("krmnlim")  # Username
        driver.find_element("name", "session[password]").send_keys("karmin123@")  # Password
        driver.find_element("name", "session[password]").send_keys(Keys.RETURN)
        print(f"[INFO] Berhasil login sebagai krmnlim.")
        time.sleep(5)

        # Navigasi ke URL Tweet
        driver.get(tweet_url)
        print(f"[INFO] Membuka URL tweet: {tweet_url}.")
        time.sleep(3)

        # Klik tombol retweet
        print("[INFO] Melakukan retweet...")
        retweet_button = "//*[@id='id__baxe9tuemra']/div[2]/button/div/div[2]/span/span/span"
        driver.find_element("xpath", retweet_button).click()
        time.sleep(1)
        driver.find_element("xpath", "//div[@data-testid='retweetConfirm']").click()

        # Klik tombol like
        print("[INFO] Menyukai tweet...")
        like_button = "//*[@id='id__baxe9tuemra']/div[3]/button/div/div[2]/span/span/span"
        driver.find_element("xpath", like_button).click()

        print(f"[INFO] Tugas Twitter selesai.")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")
    finally:
        driver.quit()
        print(f"[INFO] Menutup driver.")

# =================== MAIN FUNCTION ===================
if __name__ == "__main__":
    # Masukkan URL tweet yang ingin di-retweet dan di-like
    TWEET_URL = "https://x.com/NewTread_/status/1882458950790205638"  # URL tweet yang diberikan

    print("[INFO] Memulai tugas Twitter.")
    twitter_task(TWEET_URL)

    print("[INFO] Tugas Twitter selesai.")
