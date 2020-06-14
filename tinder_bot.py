from selenium import webdriver
from time import sleep

from secret import email, password

# each action has two step: select and interact
class TinderBot():
    def __init__(self): 
        self.driver = webdriver.Chrome()

    def login(self): 
        self.driver.get('https://tinder.com')

        # self.driver.implicitly_wait(20)
        sleep(2)

        gm_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[1]/div/button')
        gm_btn.click()

          #switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
 
        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(email)
        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn.click()

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw_in.send_keys(password)
        pnext_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span')
        pnext_btn.click()
        
        self.driver.switch_to_window(base_window)

  #popup after login: allow location
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()

