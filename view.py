import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def click_play_button(driver):
    try:
        play_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".PlayHint-sc-121lzq-0.ixmQLY"))
        )
        play_button.click()
        return True
    except Exception as e:
        print("Play button not found or not clickable: ", e)
        return False

def play_video(driver, url, jumlah_tab):
    main_window = driver.current_window_handle
    for i in range(jumlah_tab):
        driver.execute_script("window.open(arguments[0]);", url)
        driver.switch_to.window(driver.window_handles[-1])

        if click_play_button(driver):
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "video"))
                )
                driver.execute_script("document.getElementById('video').play();")
                print(f"Play button clicked - Video di tab {i+1} diputar.")
            except Exception as e:
                print(f"Tidak dapat memutar video di tab {i+1}: {e}")

        driver.switch_to.window(main_window)
        time.sleep(2)

def main():
    jumlah_tab_awal = int(input("Berapa tab yang ingin dibuka? "))

    while True:
        options = uc.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--mute-audio')
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")

        driver = uc.Chrome(options=options)

        url = "https://shopee.co.id/universal-link?redir=https%3A%2F%2Flive.shopee.co.id%2Fshare%3Ffrom%3Dlive%26session%3D54588066%26viewer%3D0%23pcshare"

        # Menghitung jumlah tab untuk iterasi ini (antara 80% hingga 100% dari jumlah_tab_awal)
        jumlah_tab = random.randint(int(jumlah_tab_awal * 0.8), jumlah_tab_awal)
        print(f"Membuka {jumlah_tab} tab pada iterasi ini.")  # Pastikan nilai ini berva

        play_video(driver, url, jumlah_tab)

        # Jeda acak antara 60 sampai 120 detik setelah memutar video
        wait_time_after_playing = random.randint(60, 120)
        print(f"Menunggu {wait_time_after_playing} detik sebelum memulai ulang...")
        time.sleep(wait_time_after_playing)

        # Jeda acak antara 60 sampai 120 detik sebelum menutup browser
        wait_time_before_closing = random.randint(60, 120)
        print(f"Menunggu {wait_time_before_closing} detik sebelum menutup browser...")
        time.sleep(wait_time_before_closing)

        driver.quit()

if __name__ == "__main__":
    main()
