import random
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from time import sleep

from loguru import logger
from playwright.sync_api import Playwright, BrowserType, BrowserContext, Page
from playwright.sync_api import sync_playwright
from domains import DOMAINS


class Tls(threading.local):
    def __init__(self):
        self.playwright: Playwright = None
        self.browser: BrowserType = None
        self.context: BrowserContext = None
        self.page: Page = None


class Generator:
    tls = Tls()

    def __init__(self):
        pass

    def run(self, k, domain):
        logger.info("THREAD: %s - ENTER" % k)
        logger.info(domain)

        self.tls.playwright = sync_playwright().start()
        self.tls.browser = self.tls.playwright.chromium.launch(headless=True)
        self.tls.context = self.tls.browser.new_context(
            bypass_csp=True,
            ignore_https_errors=True,
            color_scheme=random.choice(["dark", "light", "no-preference"]),
            timezone_id=None,
            geolocation={"longitude": 1, "latitude": 2},
            locale="en-US",
            java_script_enabled=True,
            user_agent=None,
        )
        self.tls.page = self.tls.context.new_page()
        self.tls.page.goto(domain)

        try:
            title = self.tls.page.title()

            logger.info(f"Title: {title}")
        except Exception as err:
            logger.error(err)

        self.tls.page.close()
        self.tls.context.close()
        self.tls.browser.close()
        self.tls.playwright.stop()

        logger.info("THREAD: %s - EXIT" % k)


if __name__ == "__main__":
    generators = list()
    tpe = ThreadPoolExecutor(max_workers=4)

    for i, domain in enumerate(DOMAINS):
        generator = Generator()
        generators.append(generator)
        tpe.submit(generator.run, i + 1, domain)
        sleep(0.1)

    tpe.shutdown(wait=False)

    while sum([int(t.is_alive()) for t in tpe._threads]) > 1:
        sleep(3)