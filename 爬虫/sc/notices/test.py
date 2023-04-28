import time
import threading
from typing import Callable


class WebsiteChecker:
    def __init__(self, url: str, get_value: Callable[[], str]):
        self.url = url
        self.get_value = get_value
        self.value = None
        self.lock = threading.Lock()

    def run(self):
        while True:
            current_value = self.get_value()
            with self.lock:
                if current_value != self.value:
                    print(f"New value for {self.url}: {current_value}")
                    self.value = current_value
                    # do additional logic here
                else:
                    print(f"Value for {self.url} is unchanged")
            time.sleep(0.5)


def get_value_from_url(url: str) -> str:
    # replace this function with your code for getting the value from the URL
    return "Some value from " + url


if __name__ == "__main__":
    urls = ["http://example.com", "http://google.com", "http://reddit.com"]
    checkers = []

    for url in urls:
        checker = WebsiteChecker(url, lambda: get_value_from_url(url))
        checkers.append(checker)
        threading.Thread(target=checker.run, daemon=True).start()

    # main thread waits for keyboard interrupt
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
