import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def test_access(driver):
    driver.get('https://www.google.com')
    driver.save_screenshot('test.png')
    print(driver.title)
    #driver.quit()

if __name__ == '__main__':
    options = {
        'command_executor': 'http://selenium-hub:4444/wd/hub',
        'desired_capabilities': DesiredCapabilities.FIREFOX,
    }
    with webdriver.Remote(**options) as driver:
        test_access(driver)
