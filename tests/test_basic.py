import os
import unittest
import dash
import dash_html_components as html

from app import app, server, app_name
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options

'''
class TestApp(unittest.TestCase):

    def test_root_layout_is_container(self):
        self.assertIs(app._layout.className, "container")

    def test_secret_key_is_set(self):
        # don't forget to set the SECRET_KEY on TravisCI too
        self.assertNotEqual(os.environ.get("SECRET_KEY"), "secret-key")

    def test_app_is_named_after_app_name(self):
        self.assertIs(app.title, "Mk Analysis")
'''


# # options = webdriver.Options()
# # options.binary_location = '/usr/bin/chromium-browser'

# # # All the arguments added for chromium to work on selenium
# # options.add_argument("--no-sandbox") #This make Chromium reachable
# # options.add_argument("--no-default-browser-check") #Overrides default choices
# # options.add_argument("--no-first-run")
# # options.add_argument("--disable-default-apps") 
# driver = webdriver.Chrome('/home/travis/virtualenv/python3.7   /chromedriver') # chrome_options=options


# # 2. give each testcase a tcid, and pass the fixture
# # as a function argument, less boilerplate
# def test_bsly001_falsy_child(dash_duo):

#     # 3. define your app inside the test function
#     app = dash.Dash(__name__)
#     app.layout = html.Div(id="nully-wrapper", children=0)

#     # 4. host the app locally in a thread, all dash server configs could be
#     # passed after the first app argument
#     dash_duo.start_server(app)

#     # 5. use wait_for_* if your target element is the result of a callback,
#     # keep in mind even the initial rendering can trigger callbacks
#     dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)

#     # 6. use this form if its present is expected at the action point
#     assert dash_duo.find_element("#nully-wrapper").text == "0"

#     # 7. to make the checkpoint more readable, you can describe the
#     # acceptance criterion as an assert message after the comma.
#     assert dash_duo.get_logs() == [], "browser console should contain no error"

#     # 8. visual testing with percy snapshot
#     dash_duo.percy_snapshot("bsly001-layout")

#     def test_one(dash_duo):
#         app = import_app("dash_test.app")
#         dash_br.start_server(app)
#         dash_br.wait_for_text_to_equal("h1", "Hello Dash", timeout=4)


if __name__ == "__main__":
    unittest.main()

