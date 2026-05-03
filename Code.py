import sys
import warnings
import requests
from time import sleep
from bs4 import BeautifulSoup
from tkinter import Tk
from tkinter.messagebox import showinfo
from _tkinter import TclError

warnings.filterwarnings("ignore")


class CricketInfo:
    def __init__(self):
        self.url = "http://static.cricinfo.com/rss/livescores.xml"

    def display_score(self, score):
        TIME_TO_WAIT = 20000  # 20 seconds

        root = Tk()
        root.withdraw()

        try:
            root.after(TIME_TO_WAIT, root.destroy)
            showinfo("Live Cricket Score", score)
        except TclError:
            pass

    def live_match_details(self):
        sno = 1
        match_guid = []

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "xml")

        print("\n=====================")
        print("Live Cricket Matches")
        print("=====================\n")

        for item in soup.find_all("item"):
            print(f"{sno}. {item.description.text}")
            match_guid.append(item.guid.text)
            sno += 1

        return match_guid

    def validate_user_input(self):
        print("\nEnter match number or 0 to exit:")

        while True:
            try:
                user_input = int(input(">> "))

                if user_input < 0 or user_input > 30:
                    print("Invalid input. Try again!")
                    continue

                if user_input == 0:
                    sys.exit()

                return user_input

            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_live_matches(self):
        match_guid = self.live_match_details()
        user_input = self.validate_user_input()

        try:
            while True:
                match_url = match_guid[user_input - 1]
                response = requests.get(match_url)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "xml")
                score = soup.find_all("title")

                self.display_score(score[0].text)
                sleep(20)

        except KeyboardInterrupt:
            print("\nProgram interrupted.")


if __name__ == "__main__":
    app = CricketInfo()
    app.get_live_matches()