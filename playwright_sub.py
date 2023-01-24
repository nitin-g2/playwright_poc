import sys
import pickle
browser = pickle.loads(sys.argv[1])
print("brrowser", browser)
url = pickle.loads(sys.argv[2])


context = browser.new_context()
page = context.new_page()
page.goto(url)
# subprocess.run("echo Hello World", shell=True)

try:
    print("titleeeee", page.title())
except Exception as e:
    print("title not found.")
page.close()
context.close()