from stock_scraper import  YahooScraper
from pushover_notification import send_pushover_notification
import time
from datetime import datetime
import traceback

class StockMonitor:
    def __init__(self):
        self.scraper = YahooScraper()
        self.symbol = None

    def monitor(self, symbol: str, alert_at: float) -> None:
        self.symbol = symbol
        print(f"Monitoring {symbol}...will alert at {alert_at}")
        while True:
            price = None
            try:
                self.scraper.scrape(symbol)
                price = self.scraper.get_price()
                print(f'{datetime.now()} Current price: {price}, Alert at: {alert_at}')
                if price >= alert_at:
                    print(f"Alert! Price is {price}")
                    send_pushover_notification(f"{symbol} price is {price}")
                    break
            except Exception:
                traceback.print_exc()

            print(f'Sleeping for 5 minutes...')
            time.sleep(60 * 5)

if __name__ == '__main__':
    monitor = StockMonitor()
    monitor.monitor('ETH-USD', 2760.0)