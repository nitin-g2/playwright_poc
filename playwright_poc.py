# from memory_profiler import profile
from playwright.sync_api import sync_playwright
import time
import pickle
import subprocess
script = "playwright_sub.py"
# @profile
class PlaywrightLoader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    def load(self, url):
        print("url", url)
        if not self.browser:
            print("browser attribute not present")
            playwright = sync_playwright().start()
            self.browser = playwright.chromium.launch(headless=True)
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        self.page.goto(url)
        try:
            print("title", self.page.title())
        except Exception as e:
            print("title not found.")


    # def load(self, url):
    #     print("url", url)
    #     if not self.browser:
    #         print("browser attribute not present")
    #         playwright = sync_playwright().start()
    #         # self.browser = playwright.chromium.launch(headless=True, args=[ '--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage','--disable-accelerated-2d-canvas','--no-first-run','--no-zygote','--single-process', '--disable-gpu'])
    #         self.browser = playwright.chromium.launch(headless=True)
    #         # self.context = self.browser.new_context()
    #     # self.page =n self.context.new_page()
    #     pickled_browser = pickle.dumps({"br": self.browser})
    #     # context = self.browser.new_context()
    #     subprocess.Popen(["python", script, pickled_browser, url])
    #     # page = context.new_page()
    #     # page.goto(url)
    #     # # subprocess.run("echo Hello World", shell=True)

    #     # try:
    #     #     print("titleeeee", page.title())
    #     # except Exception as e:
    #     #     print("title not found.")
    #     # page.close()
    #     # context.close()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
        self.browser = None
        self.context = None


if __name__ == '__main__':

    # @profile
    def runn():
        # s1 = tracemalloc.take_snapshot()

        # memory_info = psutil.virtual_memory()

        # domains = ["http://google.com", "http://yahoo.com", "http://gmail.com", "http://1mg.com", "http://github.com/pythonprofilers/memory_profiler", "https://morioh.com/p/e8e2940056ec", "https://psutil.readthedocs.io/en/latest/#system-related-functions", "https://www.docker.com/blog/how-to-dockerize-your-python-applications/"]
        # domains = ["http://coderzcolumn.com/","https://coderzcolumn.com/tutorials/","https://coderzcolumn.com/blogs/","https://coderzcolumn.com/quizzes/","https://coderzcolumn.com/quizzes/digital-marketing/strategies-to-improve-content-marketing","https://coderzcolumn.com/quizzes/digital-marketing/website-ranking-factors-quiz","https://coderzcolumn.com/quizzes/digital-marketing/seo-off-page-activities-quiz","https://coderzcolumn.com/quizzes/machine-learning/machine-learning-quiz-for-beginners","https://coderzcolumn.com/quizzes/machine-learning/machine-learning-basic-quiz","https://coderzcolumn.com/quizzes/blockchain/blockchain-beginners-level-3-quiz","https://coderzcolumn.com/quizzes/blockchain/blockchain-beginners-level-2-quiz","https://coderzcolumn.com/quizzes/blockchain/blockchain-basic-quiz","https://coderzcolumn.com/quizzes/digital-marketing/google-analytics-quiz","https://coderzcolumn.com/quizzes/digital-marketing/seo-basics","https://coderzcolumn.com/quizzes/python/python-basics","https://coderzcolumn.com/web-stories/","https://coderzcolumn.com/web-stories/digital-marketing/core-web-vitals","https://coderzcolumn.com/web-stories/python/famous-python-ides","https://coderzcolumn.com/web-stories/blockchain/interesting-blockchain-projects","https://coderzcolumn.com/web-stories/data-science/famous-python-data-visualization-libraries","https://coderzcolumn.com/web-stories/digital-marketing/famous-instagram-marketing-tools","https://coderzcolumn.com/web-stories/artificial-intelligence/python-deep-learning-libraries","https://coderzcolumn.com/tutorials/data-science/","https://coderzcolumn.com/tutorials/data-science/waterfall-chart-using-matplotlib","https://coderzcolumn.com/tutorials/data-science/how-to-convert-static-pandas-plot-matplotlib-to-interactive-hvplot","https://coderzcolumn.com/tutorials/data-science/matplotlib-animations","https://coderzcolumn.com/tutorials/data-science/plotnine-simple-guide-to-create-charts-using-grammar-of-graphics","https://coderzcolumn.com/tutorials/data-science/matplotlib-pyplot","https://coderzcolumn.com/tutorials/data-science/annotate-matplotlib-charts","https://coderzcolumn.com/tutorials/data-science/interactive-plotting-in-python-jupyter-notebook-using-bqplot","https://coderzcolumn.com/tutorials/data-science/interactive-plotting-in-python-using-bokeh","https://coderzcolumn.com/tutorials/data-science/getting-started-with-holoviews-basic-plotting","https://coderzcolumn.com/tutorials/data-science/guide-to-create-animation-using-bokeh","https://coderzcolumn.com/tutorials/data-science/interactive-gui-apps-using-bokeh-widgets","https://coderzcolumn.com/tutorials/data-science/plotnine-annotations","https://coderzcolumn.com/tutorials/data-science/pandas-bokeh-interactive-bokeh-charts-from-pandas-dataframes","https://coderzcolumn.com/tutorials/data-science/add-annotations-to-bokeh-charts","https://coderzcolumn.com/tutorials/data-science/link-bokeh-charts-to-ipywidgets-widgets","https://coderzcolumn.com/tutorials/data-science/candlestick-chart-in-python-mplfinance-plotly-bokeh","https://coderzcolumn.com/tutorials/data-science/altair-basic-interactive-plotting-in-python","https://coderzcolumn.com/tutorials/data-science/dates-times-and-time-zone-handling-in-python-using-pandas","https://coderzcolumn.com/tutorials/data-science/time-series-resampling-and-moving-window-functions","https://coderzcolumn.com/tutorials/data-science/how-to-create-sunburst-chart-in-python-plotly","https://coderzcolumn.com/tutorials/data-science/how-to-remove-trend-and-seasonality-from-time-series-data-using-python-pandas","https://coderzcolumn.com/tutorials/data-science/cufflinks-how-to-create-plotly-charts-from-pandas-dataframe-with-one-line-of-code","https://coderzcolumn.com/tutorials/data-science/how-to-plot-sankey-diagram-in-python-jupyter-notebook-holoviews-and-plotly","https://coderzcolumn.com/tutorials/data-science/missingno-visualize-missing-data-in-python","https://coderzcolumn.com/tutorials/data-science/build-dashboard-using-streamlit-and-cufflinks","https://coderzcolumn.com/tutorials/data-science/guide-to-create-pivot-tables-from-pandas-dataframe","https://coderzcolumn.com/tutorials/data-science/geoviews-scatter-and-bubble-maps","https://coderzcolumn.com/tutorials/data-science/geoviews-choropleth-maps","https://coderzcolumn.com/tutorials/data-science/geoplot-scatter-and-bubble-maps-python","https://coderzcolumn.com/tutorials/data-science/geoplot-choropleth-maps-python","https://coderzcolumn.com/tutorials/artificial-intelligence/","https://coderzcolumn.com/tutorials/artificial-intelligence/gluoncv-image-segmentation-using-pre-trained-mxnet-models","https://coderzcolumn.com/tutorials/artificial-intelligence/pytorch-image-segmentation-using-pre-trained-models","https://coderzcolumn.com/tutorials/artificial-intelligence/gluoncv-image-classification-using-pre-trained-mxnet-models","https://coderzcolumn.com/tutorials/artificial-intelligence/create-simple-neural-networks-in-python-using-keras","https://coderzcolumn.com/tutorials/artificial-intelligence/pytorch-image-classification-using-pre-trained-models","https://coderzcolumn.com/tutorials/artificial-intelligence/haiku-glove-embeddings-for-text-classification","https://coderzcolumn.com/tutorials/python/","https://coderzcolumn.com/tutorials/python/tarfile-simple-guide-to-work-with-tape-archives-in-python","https://coderzcolumn.com/tutorials/python/zipfile-simple-guide-to-work-with-zip-archives-in-python","https://coderzcolumn.com/tutorials/python/asyncio-concurrent-programming-using-async-await-syntax-in-python","https://coderzcolumn.com/tutorials/python/multiprocessing-basic","https://coderzcolumn.com/tutorials/python/email-how-to-represent-an-email-message-in-python","https://coderzcolumn.com/tutorials/python/smtplib-simple-guide-to-sending-mails-using-python","https://coderzcolumn.com/tutorials/python/signal-simple-guide-to-send-receive-and-handle-system-signals-in-python","https://coderzcolumn.com/tutorials/python/difflib-simple-way-to-find-out-differences-between-sequences-file-contents-using-python","https://coderzcolumn.com/tutorials/python/configparser-simple-guide-to-create-and-parse-configuration-files","https://coderzcolumn.com/tutorials/python/sched-how-to-schedule-events-in-python","https://coderzcolumn.com/tutorials/digital-marketing/","https://coderzcolumn.com/tutorials/digital-marketing/how-to-create-newsletter-on-linkedin","https://coderzcolumn.com/tutorials/digital-marketing/how-to-manage-roles-for-the-facebook-page","https://coderzcolumn.com/tutorials/digital-marketing/how-to-connect-facebook-page-with-instagram-account","https://coderzcolumn.com/tutorials/digital-marketing/how-to-schedule-a-post-on-facebook","https://coderzcolumn.com/tutorials/digital-marketing/how-to-create-instagram-post-with-creator-studio","https://coderzcolumn.com/tutorials/digital-marketing/how-to-create-an-event-for-your-facebook-page","https://coderzcolumn.com/tutorials/digital-marketing/how-to-create-a-facebook-business-page","https://coderzcolumn.com/tutorials/digital-marketing/simple-steps-to-social-media-strategy"]

        # process = psutil.Process(os.getpid())

        # print("2")
        # tracemalloc.take_snapshot()

        domains = ["https://medium.com/@x_TomCooper_x/ukraine-war-17-january-2023-klishchivka-dad1df69ae83",
                   "https://www.cantorsparadise.com/elliptic-curves-the-great-mystery-61599a93c61d",
                   "https://blog.medium.com/medium-embraces-mastodon-19dcb873eb11",
                   "https://betterhumans.pub/13-body-language-tips-for-young-professionals-to-be-more-influential-751b27e30662",
                   "https://eand.co/why-britains-severely-underestimating-british-collapse-4d5f50550c62",
                   "https://wlockett.medium.com/tesla-is-in-immense-trouble-and-musk-knows-it-9822ed601f72",
                   "https://www.cantorsparadise.com/elliptic-curves-the-great-mystery-61599a93c61d",
                   "https://docseuss.medium.com/the-secret-ingredient-to-telling-a-good-story-31497a020de4",
                   "https://venture.circuit.ooo/products-with-community-at-their-core-e53d8810276b",
                   "https://medium.com/@chazhutton/i-asked-chatgpt-to-create-comics-then-i-drew-them-6e9622dfc30e",
                   "https://blog.medium.com/what-were-reading-raising-good-humans-ai-generated-twins-and-new-year-s-resolutions-that-stick-114f7dfd2a5d",
                   "https://blog.medium.com/medium-embraces-mastodon-19dcb873eb11",
                   "https://markwschaefer.medium.com/20-entertaining-uses-of-chatgpt-you-never-knew-were-possible-3bc2644d4507",
                   "https://betterhumans.pub/how-to-say-no-actual-phrases-for-better-boundaries-b5d824e2b7e9",
                   "https://betterprogramming.pub/context-over-task-lists-2e8912d7df61",
                   "https://humanparts.medium.com/raise-good-humans-bd2db24212b8",
                   "https://clivethompson.medium.com/the-power-of-indulging-your-weird-offbeat-obsessions-77c12f10e69f",
                   "https://jackashepherd.medium.com/7-truly-remarkable-events-in-the-history-of-swearing-82e787e624ad",
                   "https://medium.com/irlproduct/how-senior-product-managers-think-differently-c5d8cd0cb52c",
                   "https://medium.com/age-of-awareness/the-age-based-classroom-kills-education-b27193558325",
                   "https://uxdesign.cc/what-the-fnu-fa72cf4ad5bd",
                   "https://kozyrkov.medium.com/the-15-new-years-resolutions-you-need-to-make-right-now-c0ec111bd212",
                   "https://medium.com/humungus/what-i-learned-selling-comedy-tickets-on-the-streets-of-new-york-5570fa61742f",
                   "https://medium.com/the-spike/2022-a-review-of-the-year-in-neuroscience-ae4e0de082e7",
                   "https://barackobama.medium.com/my-2022-end-of-year-lists-ba76b6278801",
                   "https://kozyrkov.medium.com/2022-a-productivity-revolution-f34f32a27e5b",
                   "https://scottbelsky.medium.com/creating-in-the-era-of-creative-confidence-b4e251d725f",
                   "https://medium.com/indian-thoughts/mushrooms-mastodon-jonah-hill-and-me-dc1df1313f4b",
                   "https://uxdesign.cc/a-product-managers-64-insights-from-2022-22e3bd78b8c9",
                   "https://medium.com/swlh/dont-just-set-goals-build-systems-8158ac541df",
                   "https://humanparts.medium.com/my-memory-knows-what-its-doing-notes-on-grief-ffb8d73e986f",
                   "https://kozyrkov.medium.com/ai-science-fiction-vs-reality-a8bee2ab711d"]
        index = 0
        size = len(domains)
        playwright_loader = PlaywrightLoader()
        
        while index < 800:
            time.sleep(0.2)
            playwright_loader.load(domains[(index%size)])
            index += 1


        playwright_loader.close()


    runn()

#
# browser
# context
# page
#
# A: with single context
# 1: loading all the urls in just one page close the page at the end of the last page
# 2: creating multiple pages(counter of first point)
#
# B: with multiple context
# 1: loading all the urls in just one page close the page at the end of the last page
# 2: creating multiple pages(counter of first point)
