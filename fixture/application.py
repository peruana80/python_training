from selenium import webdriver
#import os
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import os

chromedriver = "C:\Users\kala\Documents\GitHub\python_training\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver


class Application:


    def __init__(self, browser="firefox"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy (self):
        self.wd.quit()


