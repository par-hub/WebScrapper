# import pandas as pd
# import requests
# from bs4 import BeautifulSoup 
# import numpy as np

# def get_title(soup):
#     try:
#         title = soup.find("span",attrs={"id":"productTitle"}).text.strip()
#     except AttributeError:
#         title = ""
#     return title
# def get_price(soup):
#     try:
#         price=soup.find("span",attrs={"class":"a-price aok-align-center reinventPricePriceToPayMargin priceToPay"}).text.strip()
#     except:
#         price = ""
#     return price
# def get_rating(soup):
#     try:
#         rating = soup.find("span",attrs={"class":"a-icon-alt"}).text.strip()
#     except AttributeError:
#         rating = ""
#     return rating
# if __name__ ==  '__main__':
#     url = "https://www.amazon.in/s?k=playstation+5&crid=2D4ORYTC2X036&sprefix=playstation+5+%2Caps%2C726&ref=nb_sb_noss_2"
#     HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.110 Safari/537.36', 'Accept-Language':'en-US,en;q=0.5'})
#     r = requests.get(url,headers=HEADERS)
#     print(r)
#     soup = BeautifulSoup(r.text,"lxml")
#     # print(soup)
#     links = soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
#     links_list = []
#     for link in links:
#         links_list.append(link.get("href"))
#     d = {"title":[],"price":[],"rating":[]}
#     for link in links_list:
#         r_2 = requests.get("https://www.amazon.in/" + link,headers=HEADERS)
#         new_soup = BeautifulSoup(r_2.text,"lxml")
#         d["title"].append(get_title(new_soup))
#         d["price"].append(get_price(new_soup))
#         d["rating"].append(get_rating(new_soup))

#     amazon_df = pd.DataFrame.from_dict(d)
#     amazon_df.replace({"title": {'': np.nan}}, inplace=True)
#     amazon_df = amazon_df.dropna(subset=['title'])
#     amazon_df.to_csv("amazon_data.csv",header=True,index=False)
#     print(amazon_df)


 



import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": "productTitle"}).text.strip()
    except AttributeError:
        title = ""
    return title

def get_price(soup):
    try:
        price = soup.find("span", attrs={"class": "a-price-whole"}).text.strip()  # Ensure the class name matches the actual HTML structure
    except AttributeError:
        price = ""
    return price

def get_rating(soup):
    try:
        rating = soup.find("span", attrs={"class": "a-icon-alt"}).text.strip()
    except AttributeError:
        rating = ""
    return rating
def get_review_count(soup):
    try:
        review_count = soup.find("span",attrs={'id':'acrCustomerReviewText'}).text.strip()
    except AttributeError:
        review_count = ""
    return review_count
def get_availabilty(soup):
    try:
        available = soup.find("div",attrs={'id':'availability'})
        available = available.find("span").text.strip()
    except AttributeError:
        available = "Not Available"
    return available

if __name__ == '__main__':
    url = "https://www.amazon.in/s?k=monitor+for+pc&crid=2PI8VTZUHEQNI&sprefix=mo%2Caps%2C714&ref=nb_sb_ss_ts-doa-p_1_2"
    HEADERS = ({
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50"

    })
    r = requests.get(url, headers=HEADERS)
    print(r)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        
        links_list = [link.get("href") for link in links]
        
        d = {"title": [], "price": [], "rating": [],"review":[],"availability":[]}
        for link in links_list:
            r_2 = requests.get("https://www.amazon.in/" + link, headers=HEADERS)
            new_soup = BeautifulSoup(r_2.text, "lxml")
            d["title"].append(get_title(new_soup))
            d["price"].append(get_price(new_soup))
            d["rating"].append(get_rating(new_soup))
            d["review"].append(get_review_count(new_soup))
            d["availability"].append(get_availabilty(new_soup))
        amazon_df = pd.DataFrame.from_dict(d)
        amazon_df.replace({"title": {'': np.nan}}, inplace=True)
        amazon_df = amazon_df.dropna(subset=['title'])
        amazon_df.to_csv("amazon_data.csv", header=True, index=False)
        
        print(amazon_df)
    else:
        print(f"Failed to retrieve page with status code: {r.status_code}")
