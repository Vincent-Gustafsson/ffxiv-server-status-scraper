import requests

from scraper.scraper import scrape
from messaging.producer import send_message

URL = "https://eu.finalfantasyxiv.com/lodestone/worldstatus/"


def main():
    # TODO GÖR OM TILL ENDLESS LOOP, GÖR SCRIPT RELIABLE INSTEAD
    # CRONTAB @reboot ELLER etc/rc.local
    r = requests.get(URL)
    server_data = scrape(r)
    send_message(server_data)


if __name__ == "__main__":
    main()
