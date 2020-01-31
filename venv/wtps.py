from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = "https://web.whatsapp.com/"
class InstaBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=chrome-data")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://web.whatsapp.com')  # Already authenticated
        sleep(20)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
        #     .click()
    def send_message(self):

        self.driver.find_element_by_xpath("//input[contains(@class, '_2zCfw copyable-text selectable-text')]") \
            .send_keys("Ouissal")
        sleep(1)
        self.driver.find_element_by_xpath("//input[contains(@class, '_2zCfw copyable-text selectable-text')]") \
            .send_keys(Keys.ENTER)

        for i in range(20):
            self.driver.find_element_by_xpath("//div[contains(@class, '_3u328 copyable-text selectable-text')]") \
                .send_keys("<3")
            sleep(1)
            self.driver.find_element_by_xpath("//div[contains(@class, '_3u328 copyable-text selectable-text')]") \
                .send_keys(Keys.ENTER)

    def open_url(self):
        """Open a URL using the driver's base URL"""

        # Proceed as before
        self.driver.add_cookie({'name': 'ref', 'value':  '1@8amJInDapV5qy6xnurV4yr++bzLy1z5HZ84w1pqRK+XmTXVfaZ7rPJa6','domain':'.web.whatsapp.com','path':'/pp' })
        self.driver.add_cookie({'name': 'tok', 'value':  '1@1i3/cv7lFfP8FlZRtIMbhbRsP7/mkjRx/kwzMBDoHMiBaxT2K9GJwS4fEslrvLaiBOaBItgWbfWQxw==','domain':'.web.whatsapp.com','path':'/pp' })
        self.driver.refresh()
    # def cookies(self):
    #     cookies_ref={'name':'ref','value':'1@GAVFScqaFWbPqafg8sJXIULgRflllFV8ffpuY7FGi3mKa0GwjM86/NwJ'}
    #     cookies_tok={'name':'tok','value':'1@IW12TKrMwNxrbP7CNQOueW7R7F/hRtI6Er2mT+SwHW3x5q+U26CRBmwo45He4JQlpts9i8GePqIL3A=='}
    #     self.driver.add_cookie(cookies_ref)
    #     self.driver.add_cookie(cookies_tok)
    #     cookies = self.driver.get_cookies()
    #     print(len(cookies))
    #     print(cookies)
    def family(self):

        self.driver.find_element_by_xpath("//input[contains(@class, '_2zCfw copyable-text selectable-text')]") \
            .send_keys("painful")
        sleep(1)
        self.driver.find_element_by_xpath("//input[contains(@class, '_2zCfw copyable-text selectable-text')]") \
            .send_keys(Keys.ENTER)

        self.driver.find_element_by_xpath("//div[contains(@class, '_3u328 copyable-text selectable-text')]") \
            .send_keys("testtt")
        sleep(1)
        self.driver.find_element_by_xpath("//div[contains(@class, '_3u328 copyable-text selectable-text')]") \
            .send_keys(Keys.ENTER)
bot=InstaBot()
bot.send_message()
# bot.open_url()
# bot.cookies()