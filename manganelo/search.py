from selenium import webdriver
from selenium.webdriver.common.by import By


class Search:
    def __init__(self, site):
        self.site = site
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.site)

    def search_ep(self) -> dict:
        chap_title = self.driver.find_element(By.CSS_SELECTOR, "#row-content-chapter li a")
        title = self.driver.find_element(By.CSS_SELECTOR, ".story-info-right h1")
        try:
            chap_name = chap_title.text.split(":", 1)[1]
        except IndexError:
            chap_name = chap_title.text
        try:
            print(chap_name)
            chap_number = float(chap_title.text.split(":", 1)[0].split()[1])
            print(chap_number)
        except ValueError:
            print("Cap error: Chapter number NaN")
            chap_number = 0
        try:
            with open(f"mangas\{title.text}-data.txt", "r") as f:
                chapter = float(f.readline())
                print("Opening file")
        except FileNotFoundError:
            with open(f"mangas\{title.text}-data.txt", "w") as f:
                f.write(f"{chap_number}")
                print("create file")
                chapter = chap_number
        else:
            if chap_number > chapter:
                with open(f"mangas\{title.text}-data.txt", "w") as f:
                    f.write(f"{chap_number}")
        finally:
            if chap_number > chapter:
                new_chapter = {
                    "is_new": True,
                    "chapter_num": chap_number,
                    "chapter_name": chap_name
                }
                return new_chapter
            else:
                new_chapter = {
                    "is_new": False,
                    "chapter_num": chap_number,
                    "chapter_name": chap_name
                }
                return new_chapter

    def close_tabs(self):
        self.driver.quit()
