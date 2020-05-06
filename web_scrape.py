from bs4 import BeautifulSoup
import requests, webbrowser, re
source=requests.get('https://www.amazon.com/s/ref=lp_289814_ex_n_1?rh=n%3A1055398%2Cn%3A%211063498%2Cn%3A284507&bbn=284507&ie=UTF8&qid=1582022608').text
# with open('example.html') as html_file:
#   soup=BeautifulSoup(html_file,'lxml')
soup=BeautifulSoup(source, 'lxml')
#print(soup.find('a',href='https://www.iana.org/domains/example'))
#print(soup.prettify())
#print((soup.find('a',class_='image')).text)
#anchor=soup.find('a',class_='image').img['src']
img_lnk={}
#print(source)
print(soup)
try:
    if soup.find('div',class_='bxc-grid__image.*'):
        print(True)
    else:
        print(False)
    print(f'{anchor}')
    #for anchor in soup.find_all('div',class_='bxc-grid__image   bxc-grid__image--light'):
    #     print(anchor)
    #     try:
    #         img_title=anchor.a['aria-label']
    #         print(img_title)
    #         anc=anchor.a['href']
    #         print(anc)
    #         anc1=f'https://www.amazon.com{anc}'
    #         img_lnk[img_title]=anc1
    #         #webbrowser.open_new_tab(anc1)
    #         print(anc1)
    #     except:
    #         print("fail")
    #         pass
    # #print(img_lnk)
except:
    pass
