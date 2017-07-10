from selenium import webdriver
#uses selenium webdriver to open a Firefox browser
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#checks(asserts) that the page has django in its title.
assert 'Django' in browser.title
