#login using Selenium Webdriver

# Usage :- python git_ui_login.py 

import sys
from getpass import getpass
from selenium import webdriver

class GitUiLogin(object):
  
  GIT_LOGIN_URL='http://github.com/login'
  
  def __init__(self, username, password):
    self.username=username
    self.password=password
    self.browser = webdriver.Chrome()

  def login(self):
    self.browser.get(self.GIT_LOGIN_URL)
    self.browser.find_elements_by_id('login_field')[0].send_keys(self.username)
    self.browser.find_elements_by_id('password')[0].send_keys(self.password)
    self.browser.find_elements_by_name('commit')[0].submit()

if __name__=='__main__':
  username= sys.argv[1]
  assert (len(sys.argv) == 2), "Usage: python <script_name> <username>"
  print "Enter password for user: %s" % username
  password=getpass(prompt='Enter your password: ')
  
  if not password:
    raise Exception("Password not entered.")

  git_ui_handler=GitUiLogin(username, password)
  git_ui_handler.login()
   

