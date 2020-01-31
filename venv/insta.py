from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def unfollow(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)) \
            .click()
        sleep(2)
        numberOfFollowing = self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")
        sleep(2)
        print("You have : "+numberOfFollowing.text)
        num= numberOfFollowing.text.split()
        n=num[0].replace(",", "")
        print(n)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        bot._get_names()
        for i in range(1,int(n)):
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(),'Following')]") \
                .click()
            sleep(1)
            self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]") \
                .click()
    def follow(self):

        self.driver.find_element_by_xpath("//a[contains(@href,'/explore/people/')]") \
            .click()
        self.driver.find_element_by_xpath("//button[contains(@class , 'sqdOP  L3NKy   y3zKF'")\
            .click()






        # self.driver.find_element_by_xpath("//ul[contains(@class,'jSC57  _6xe7A')]")
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[2]")\
        #     .click()
        # sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]")\
        #     .click()
        # following = self._get_names()
        # self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
        #     .click()
        # followers = self._get_names()
        # not_following_back = [user for user in following if user not in followers]
        # print(not_following_back)
        # print(followi

    def _get_names(self):
        sleep(2)
        sugs = self.driver.find_element_by_xpath("//ul[contains(@class,'jSC57  _6xe7A')]")
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            try:
                last_ht = ht
                sleep(1)
                ht = self.driver.execute_script("""
                                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                return arguments[0].scrollHeight;
                                """, scroll_box)
            except IOError:
                print("done")

        #
        # links = scroll_box.find_elements_by_tag_name('a')
        # names = [name.text for name in links if name.text != '']
        # # close button
        # self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button")\
        #     .click()
        # return names


bot=InstaBot('pluton9', '067036987-khalil')
# bot.unfollow()
bot.follow()