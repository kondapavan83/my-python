from selenium import webdriver
import time
browser=webdriver.Firefox(executable_path="/Users/nkonda/Downloads/geckodriver")
last_bid=203

browser.get("https://e-rocks.com/item/uvm766737/penfieldite-boleite#history-bid-info")
user_box=browser.find_element_by_xpath('//*[@id="edit-name"]')
pwd_box=browser.find_element_by_xpath('//*[@id="edit-pass"]')
user_box.send_keys('kondapavan@gmail.com')
pwd_box.send_keys('4******de')
login_button=browser.find_element_by_xpath('//*[@id="edit-submit"]')
login_button.click()
#time.sleep(60)
while 1:
    #browser.refresh()
    bidbox=browser.find_element_by_xpath('//*[@id="bid_amount"]')
    current_price=browser.find_element_by_xpath('/html/body/div[4]/section/div[2]/div/div[2]/div/div[3]/div/div/article/div/section[2]/div[2]/div/div[1]/div/div/span[2]')
    if int(current_price.text) > last_bid+3 and int(current_price.text)<230:
        last_bid=int(current_price.text)+5
        print("bidding at "+str(int(current_price.text)+5))
        bidbox.send_keys(str(int(current_price.text)+5))
        bid_button=browser.find_element_by_xpath('/html/body/div[4]/section/div[2]/div/div[2]/div/div[3]/div/div/article/div/section[2]/div[2]/div/div[4]/a[2]/div')
        bid_button.click()
        confirm_button=browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/button[1]/span')
        confirm_button.click()
        continue
    else:
        print("you are highest bidder")
    time.sleep(580)
