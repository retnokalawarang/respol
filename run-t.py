from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
import time
import csv
import string
import random
import sys
import os

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://yegmcsxgxkbqbjdmsvfm.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InllZ21jc3hneGticWJqZG1zdmZtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTk2NzI3NzIsImV4cCI6MjAzNTI0ODc3Mn0.79Czw_E8h4Bm3iV22Ja6R66-l-rTHfucnuWPeWAFuAY"
SUPABASE_TABLE_NAME = "bento"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


def load_data(start_data, end_data):

    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "x.csv")

    data_account = []

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    data_account = data_account[int(start_data) : int(end_data)]

    return data_account


def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    # options.add_argument("--window-size=1920, 1200")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def run_bot(data_account, recover=2):
    kw = data_account[0]

    driver = web_driver()
    driver.maximize_window()

    try:

        nama_modif = kw.replace(" ", "-")
        gmail = f"{nama_modif}-leaked-vidioo-{random_string(6)}@gmail.com"
        slug = f"{nama_modif}-leaked-videos-viral-on-x-ox-{random_string(6)}"
        # judul = f"$[NEW!]™ {kw} Leaked Video Viral On Social Media Twitter or X"
        judul = f"[~𝐄𝐗𝐂𝐋𝐔𝐒𝐈𝐕𝐄~]** {kw} Leaked Video Viral on social media Twitter x or tiktok trendingnow"
        link = f"https://onlypremium.site?title= CLICK HERE >> {kw}?ref=bento_11_23"

        driver.get("https://bento.me/signup?ref=techcrunch&app=wetransferflow&atb=true")
        time.sleep(3)

        # Isi form dengan slug
        driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='your-name']"
        ).send_keys(slug)
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(15)

        # Isi email dan password
        driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Email address']"
        ).send_keys(gmail)
        driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(
            "@@Kamudia12sPos"
        )
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(15)

        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

        driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div/div/div/div[2]/button[1]"
        ).click()

        time.sleep(3)

        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[1]/div/div/div/div[3]/button[1]/div[1]",
        ).click()

        time.sleep(3)

        driver.find_element(
            By.XPATH, "/html/body/div[2]/div[1]/div/div/div/button"
        ).click()
        time.sleep(5)

        # Ketik judul pada editor
        driver.find_element(
            By.CSS_SELECTOR, "div[contenteditable='true'].ProseMirror.rt-editor"
        ).send_keys(judul)
        time.sleep(1)

        konten = f"{kw} Leaked Video Original Video Viral Video Leaked on X Twitter Telegram \n [-FULL-]— {kw} ʟᴇᴀᴋᴇᴅ Video ᴠɪʀᴀʟ On Social Media Twitter \n Leaked Video {kw} Original Video Viral Video Leaked on X Twitter.. \n"
        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div",
        ).send_keys(konten)
        time.sleep(7)

        driver.switch_to.default_content()
        # Klik tombol untuk submit
        driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[1]/main[1]/div[3]/div[2]/button[1]/div[1]",
        ).click()
        time.sleep(5)

        # Isi link dan simpan hasil
        driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[2]/form[1]/input[1]"
        ).send_keys(link)
        time.sleep(2)

        driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/main[1]/div[2]/div[1]/button[1]"
        ).click()
        time.sleep(5)

        # with open("result.txt", "a") as f:
        #     f.write(driver.current_url + "\n")

        response = (
            supabase.table(SUPABASE_TABLE_NAME)
            .insert({"result": driver.current_url})
            .execute()
        )

        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(5)
        driver.close()
    except Exception as e:
        if recover == 0:
            print(
                f"TERJADI ERROR: ${e}",
                file=sys.__stderr__,
            )
            driver.close()
            return e

        run_bot(data_account, recover - 1)


def main():

    if len(sys.argv) < 3:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    workers = 1

    if not start_data and not end_data:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    futures = []
    line_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(start_data + 1, end_data + 1):
            try:
                futures.append(
                    executor.submit(
                        run_bot,
                        data[line_count],
                    )
                )
            except:
                pass
            line_count += 1

    wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
