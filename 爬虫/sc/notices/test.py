import threading
import time
import requests


class WebsiteChecker:
    def __init__(self, url, value_func):
        self.url = url
        self.value_func = value_func
        self.last_value = None
        self.lock = threading.Lock()

    def run(self):
        while True:
            value = self.value_func(self.url)
            with self.lock:
                if self.last_value is not None and self.last_value != value:
                    self.handle_change(value)
                self.last_value = value
            time.sleep(0.5)

    def handle_change(self, value):
        print(f"Value changed to {value} for {self.url}")


def get_value_from_url(url):
    response = requests.get(url)
    # 这里假设我们从响应中获取到了值
    value = response.text
    return value


def main():
    urls = ["http://example.com", "http://example.org", "http://example.net"]
    checkers = []
    for url in urls:
        checker = WebsiteChecker(url, get_value_from_url)
        checkers.append(checker)
        thread = threading.Thread(target=checker.run)
        thread.daemon = True
        thread.start()
    # 主线程等待所有检查器线程结束
    for checker in checkers:
        thread.join()


if __name__ == '__main__':
    main()
