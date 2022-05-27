import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

class whisky_web_scraping():
    
    def scrape_html(self,base_url, page):        
        self.base_url = base_url
        self.page = page
        
        url = base_url + str(page)
        r = requests.get(url)
        
        soup = BeautifulSoup(r.content, 'lxml')
        
        return soup
    
    def get_page_content(self, soup):
        
        self.soup = soup
        
        products_info_price = soup.find_all('div', class_ = 'product-card__content')
        
        return products_info_price
    
    def get_page_price(self, soup):
        
        self.soup = soup
        
        products_info_price = soup.find_all('div', class_ = 'product-card__data')
        
        return products_info_price
    
    def get_product_name(self, products_info_content):
        
        self.products_info_content = products_info_content
        
        product_name = []
        
        # Iterate through each product in the webpage
        for product in range(len(products_info_content)):
            
            # Extract the first class P - Which holds the name of the beverge
            name_p = products_info_content[product].find_all('p')[0]
            
            # Extract the contents of the first paragraphs - the name of the bevarage
            alcohol_name = name_p.contents[0].strip()
            
            # Append each name to the list
            product_name.append(alcohol_name)
        return product_name
    
    def get_product_alcohol_percent(self, products_info_content):
        
        self.products_info_content = products_info_content
        
        product_al_percent = []
        
        # Iterate through each product in the webpage
        for product in range(len(products_info_content)):
            
            # Extract the second class P - which holds the alcohol values
            al_p = products_info_content[product].find_all('p')[1]
            
            # Apply string manipulation to extract the alcohol percent
            alcohol_percent_str = al_p.contents[0].strip()
            start_localization_percent = alcohol_percent_str.find('/ ')
            end_localization_percent = alcohol_percent_str.find('%')
            alcohol_percent = alcohol_percent_str[start_localization_percent + 2:end_localization_percent]
            
            # Append each alcohol percent to the list
            product_al_percent.append(alcohol_percent)
        return product_al_percent
    
    def get_product_alcohol_amount(self, products_info_content):
        
        self.products_info_content = products_info_content
        
        product_al_amount = []
        
        # Iterate though each product in the webpage
        for product in range(len(products_info_content)):
            
            # Extract the second class P - which holds the alcohol values
            al_p = products_info_content[product].find_all('p')[1]
            
            # Apply string  manipulation to extract the alcohol amount
            alcohol_percent_str = al_p.contents[0].strip()
            start_localization_amount = 0
            end_localization_amount = alcohol_percent_str.find('cl')
            alcohol_amount = alcohol_percent_str[start_localization_amount:end_localization_amount]
            
            # Append each alcohol amount to the list
            product_al_amount.append(alcohol_amount)
        return product_al_amount

    def get_product_price(self, products_info_price):
        
        self.products_info_price = products_info_price
        
        product_price = []
        
        # Iterate thoigh each product in the webpage
        for product in range(len(products_info_price)):
            
            # Extract the price for each product
            alcohol_price = products_info_price[product].contents[0].contents[0].replace('£','').strip()
            
            # Append each alcohol price to the list
            product_price.append(alcohol_price)
        return product_price
    
    def create_df(self, names, alcohol_amount, alcohol_percent, price):
        
        self.names = names
        self.alcohol_amount = alcohol_amount
        self.alcohol_percent = alcohol_percent
        self.price = price
        
        # Create a Dataframe
        original_df = pd.DataFrame(names, columns=['Product_Name'])
        original_df['Alcohol_Percent'] = alcohol_percent
        original_df['Alcohol_Amount'] = alcohol_amount
        original_df['Alcohol_Price'] = price
        
        return original_df
    
    