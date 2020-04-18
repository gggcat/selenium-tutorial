from selenium import webdriver
import chromedriver_binary

def test_access(driver):
    driver.get('https://www.google.com')
    driver.save_screenshot('test.png')
    print(driver.title)
    driver.quit()

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1224,844")
    driver = webdriver.Chrome(options=options)
    test_access(driver)
