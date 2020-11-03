from selenium import webdriver
import pprint
import time
browser=webdriver.Firefox(executable_path="/Users/nkonda/Downloads/geckodriver")
browser.get("https://us.etrade.com/etx/wm/analystresearch/#/trending")
table={}
user_box=browser.find_element_by_xpath('//*[@id="user_orig"]')
pwd_box=browser.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/div[2]/div[2]/div/input')
logon_button=browser.find_element_by_xpath('//*[@id="logon_button"]')
user_box.send_keys('kondapavan')
pwd_box.send_keys('XXXX')
logon_button.click()
rating_button=browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/section/section/div/div[2]/div/div/ng-transclude/div/div/table/thead/tr/th[3]/button[1]')
rating_button.click()
print(browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/section/section/div/div[2]/div/div/ng-transclude/div/div/table/tbody/tr[1]/td[1]/div[2]').text)
recommendations=browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/section/section/div/div[2]/div/div/ng-transclude/div/div/table/tbody/tr[1]/td[6]/div/div[2]/a')
recommendations.click()
time.sleep(4)
print(browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/section/div/div[4]/section/div[2]/div/table/tbody/tr[1]/td[5]/span').text)
print(browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/section/div/div[4]/section/div[2]/div/table/tbody/tr[2]/td[5]/span').text)
print(browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/section/div/div[4]/section/div[2]/div/table/tbody/tr[3]/td[5]/span').text)
print(browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/section/div/div[4]/section/div[2]/div/table/tbody/tr[4]/td[5]/span').text)
print(browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/section/div/div[4]/section/div[2]/div/table/tbody/tr[5]/td[5]/span').text)
# for i in range(1,31):
#     p={}
#     for j in [x for x in range(1,8) if x != 6]:
#         p[browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/div[2]/div[4]/table/thead/tr/th[{}]/a'.format(j)).text]=browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/div[2]/div[4]/table/tbody/tr[{}]/td[{}]'.format(i,j)).text
#     p['buy/sell']=int((p['# Buy Orders']).replace(',',''))/int((p['# Sell Orders']).replace(',',''))
#     table[p['buy/sell']/int((p['Rank']).replace('.',''))]=p
#     # table[p['buy/sell']
# pprint.pprint(table)

# pwd_box=browser.find_element_by_xpath('//*[@id="edit-pass"]')
# user_box.send_keys('kondapavan@gmail.com')
# pwd_box.send_keys('4ortitude')
# login_button=browser.find_element_by_xpath('//*[@id="edit-submit"]')
# login_button.click()
# #time.sleep(60)
# while 1:
#     #browser.refresh()
#     bidbox=browser.find_element_by_xpath('//*[@id="bid_amount"]')
#     current_price=browser.find_element_by_xpath('/html/body/div[4]/section/div[2]/div/div[2]/div/div[3]/div/div/article/div/section[2]/div[2]/div/div[1]/div/div/span[2]')
#     if int(current_price.text) > last_bid+3 and int(current_price.text)<230:
#         last_bid=int(current_price.text)+5
#         print("bidding at "+str(int(current_price.text)+5))
#         bidbox.send_keys(str(int(current_price.text)+5))
#         bid_button=browser.find_element_by_xpath('/html/body/div[4]/section/div[2]/div/div[2]/div/div[3]/div/div/article/div/section[2]/div[2]/div/div[4]/a[2]/div')
#         bid_button.click()
#         confirm_button=browser.find_element_by_xpath('/html/body/div[12]/div[2]/div/button[1]/span')
#         confirm_button.click()
#         continue
#     else:
#         print("you are highest bidder")
#     time.sleep(580)
