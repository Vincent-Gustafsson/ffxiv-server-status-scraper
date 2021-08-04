import requests

from scraper.scraper import scrape


URL = "https://eu.finalfantasyxiv.com/lodestone/worldstatus/"


def main():
    print("starting")
    r = requests.get(URL)
    server_data = scrape(r)

    


if __name__ == "__main__":
    main()
