from selenium import webdriver

"""
Suck it docstrings!!!
"""

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
