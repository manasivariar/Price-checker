import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
from time import sleep

URL = "https://www.flipkart.com/peps-springkoil-normal-top-maroon-6-inch-queen-bonnell-spring-mattress/p/itmfg8t7mhuyvjbq?pid=BEMEVHH7FSUKGADN&lid=LSTBEMEVHH7FSUKGADN8HBA9A&marketplace=FLIPKART&sattr[]=thickness&sattr[]=dimension&st=dimension&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na"


header = {
    "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"
}

def price_checker():

    request = requests.get(URL, headers=header)
    soup = BeautifulSoup(request.content, 'html.parser')

    product_name = soup.find(class_ = "B_NuCI").get_text()
    product_price = int(soup.find(class_ = "_30jeq3 _16Jk6d").get_text()[1:7].replace(",",""))
    
    chrome_driver = webdriver.Chrome(executable_path ='D:\chromedriver\chromedriver.exe')
    chrome_driver.get('https://www.flipkart.com/peps-springkoil-normal-top-maroon-6-inch-queen-bonnell-spring-mattress/p/itmfg8t7mhuyvjbq?pid=BEMEVHH7FSUKGADN&lid=LSTBEMEVHH7FSUKGADN8HBA9A&marketplace=FLIPKART&sattr[]=thickness&sattr[]=dimension&st=dimension&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na')
    chrome_driver.find_element_by_xpath('//*[@id="pincodeInputId"]').send_keys('680561')
    chrome_driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/span').click()
    sleep(2)
    date = chrome_driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[1]/ul/div/div/span[1]').text
    
    if(product_price > 15000):
        send_mail()
        print("DELIVERY IS AVAILABLE AND THE DELIVERY DATE IS :",date)
    else:
        print("PRICE NOT REDUCED, THE PRICE IS STILL", product_price)
        print("DELIVERY IS AVAILABLE AND THE DELIVERY DATE IS :",date)

def send_mail():
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.ehlo()

    gmail.login('manasirvariar13121999@gmail.com', 'gfduqhtxinpmymxi')

    subject = 'PRICE GOT REDUCED!'
    body = 'LINK: https://www.flipkart.com/peps-springkoil-normal-top-maroon-6-inch-queen-bonnell-spring-mattress/p/itmfg8t7mhuyvjbq?pid=BEMEVHH7FSUKGADN&lid=LSTBEMEVHH7FSUKGADN8HBA9A&marketplace=FLIPKART&sattr[]=thickness&sattr[]=dimension&st=dimension&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na'

    message = f"Subject: {subject}\n\n{body}"

    gmail.sendmail('manasirvariar13121999@gmail.com', 'manasirvariar007@gmail.com', message)
    print('EMAIL SENT!')

    gmail.quit()

while True:
    price_checker()
    sleep(60)

