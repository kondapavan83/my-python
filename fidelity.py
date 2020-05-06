from selenium import webdriver
import pprint
#import time
browser=webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.get("https://eresearch.fidelity.com/eresearch/gotoBL/fidelityTopOrders.jhtml")
table={}
for i in range(1,31):
    p={}
    for j in [x for x in range(1,8) if x != 6]:
        p[browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/div[2]/div[4]/table/thead/tr/th[{}]/a'.format(j)).text]=browser.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/div[2]/div[4]/table/tbody/tr[{}]/td[{}]'.format(i,j)).text
    p['buy/sell']=int((p['# Buy Orders']).replace(',',''))/int((p['# Sell Orders']).replace(',',''))
    # if int((p['Rank']).replace('.','')) <=15:
    # if p['buy/sell'] >2.5 and int((p['Rank']).replace('.','')) <=15:
    #table[p['buy/sell']/(int((p['Rank']).replace('.',''))/10)]=p
    if int((p['Rank']).replace('.','')) <=10:
        table[p['buy/sell']]=p
pprint.pprint(table)

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
