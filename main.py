from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
from tkinter import *
from selenium.common.exceptions import NoSuchCookieException, NoSuchElementException

mGui = Tk()
mGui.geometry("800x580")
mGui.title('Instagram bot')
mGui.configure(bg = 'pink')

Label(mGui,background='pink', text='Input username: ', fg='black', font=('Calibri', 18, 'bold')).pack(pady=5)
a = Entry(mGui)
a.pack(pady=5)
Label(mGui,background='pink', text='Input password: ', fg='black', font=('Calibri', 18, 'bold')).pack(pady=5)
b = Entry(mGui,show='*')
b.pack(pady=5)
Label(mGui,background='pink', text='Input hashtag(pa #): ', fg='black', font=('Calibri', 18, 'bold')).pack(pady=5)
c = Entry(mGui)
c.pack(pady=5)
Label(mGui,background='pink', text='On how many posts do you want to go through(recommended 10): ', fg='black', font=('Calibri', 18, 'bold')).pack(pady=5)
d = Entry(mGui)
d.pack(pady=5)
Label(mGui,background='pink', text='How many people do you want to follow(recommended 10): ', fg='black', font=('Calibri', 18, 'bold')).pack(pady=5)
e = Entry(mGui)
e.pack(pady=5)
Label(mGui,background='pink', text='Input 2 comments you want to use: ', fg='black', font=('Calibri', 18, 'bold')).pack(pady=5)
f = Entry(mGui)
f.pack(pady=5)
g = Entry(mGui)
g.pack(pady=5)

def getInput():
    z = a.get()
    x = b.get()
    v = c.get()
    m = d.get()
    n = e.get()
    j = f.get()
    k = g.get()
    mGui.destroy()

    global params
    params = [z,x,v,m,n,j,k]

Button(mGui, text="Submit",bd = '4', fg='black',font=('Calibri', 14 , 'bold'),command=getInput).pack(pady=5)

mGui.mainloop()

koha_1 = int(params[3])
koha_2 = int(params[4])


class Bot():

    links = []

    #komente
    comments = [
        params[5], params[6]
    ]
    
    amount = ('30')

    def __init__(self):
        self.login(params[0],params[1])#username password

        self.like_comment_by_hashtag(params[2])#hashtagjet

    def login(self, username, password):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')#pathi i chromedriver-it
        self.driver.get('https://instagram.com/')
        sleep(5)
        try:
            username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')#Emri#
            username_input.send_keys(username)
            sleep(3)
            password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')#Pasuordi#
            password_input.send_keys(password)
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()#Log in
            sleep(7)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click() # shtyp 'not-now' buton
            sleep(10)
            self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click() # shtyp 'not-now' buton
            sleep(3)
        except NoSuchElementException:
            sleep(5)    

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(koha_1): #Ne sa poste do shkosh
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            try:
                self.driver.get(link)
                # like
                sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click()
                sleep(10)

                # koment
                self.driver.find_element_by_class_name('RxpZH').click() 
                sleep(7)
                self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
                sleep(7)
                self.driver.find_element_by_xpath("//button[@type='submit']").click()
                sleep(7)

                # faqja
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').click()
                sleep(10)
                # Kliko tabin ku jan followersat
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
                sleep(10)
                # Shtyp butonin follow
                for i in range(koha_2):   #sa veta do ndjeksh nga faqja
                    self.driver.find_element_by_xpath('//button [@class="sqdOP  L3NKy   y3zKF     "]').click()# butoni i follow
                    sleep(8)
                    html = self.driver.find_element_by_tag_name('html') # te zbresesh poshte ne liste
                    html.send_keys(Keys.END)
                    sleep(8)
            except NoSuchElementException:
                sleep(7)        

def main():
    while True:
        my_bot = Bot()
        sleep(60*60) # 1 ore

if __name__ == '__main__':
    main()
