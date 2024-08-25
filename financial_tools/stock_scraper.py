import requests
from bs4 import BeautifulSoup


class YahooScraper:
    def __init__(self):
        self.symbol = None
        self.base_url = f"https://sg.finance.yahoo.com/quote/"
        self.soup = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def scrape(self, symbol: str) -> None:
        self.symbol = symbol
        url = self.base_url + symbol
        response = requests.get(url, headers=self.headers)
        self.soup = BeautifulSoup(response.text, "html.parser")

    def get_price(self) -> float:
        price = self.soup.find("fin-streamer", {"data-field": "regularMarketPrice"}).text
        return float(price.replace(',', ''))


if __name__ == '__main__':
    scraper = YahooScraper()
    scraper.scrape('4287.T')
    print(scraper.get_price())
