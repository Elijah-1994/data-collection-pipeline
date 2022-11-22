#%%
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from uuid import uuid4
import os
import requests
import time
import tempfile
import json
#%%
class WaterstonesScrapper:
    def __init__(self,):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://www.waterstones.com/")
        self.images_directory ='raw_data/images' 
        self.parent_directory = os.getcwd()
        self.time_stamps = datetime.now()
        self.time_stamps_formated = self.time_stamps.strftime("%Y-%m-%d,%H:%M:%S")
        self.date = self.time_stamps.strftime("%Y-%m-%d")
    pass
    
    def create_directory(self,):
        '''
        This function is used create the folder directories to store the json and image data. 
        '''
        parent_directory = self.parent_directory
        images_directory = self.images_directory
        path = os.path.join(parent_directory, images_directory) 
        try:
            os.makedirs(path, exist_ok = True)
        except OSError as error:
                return
    pass
    
    def accept_cookies(self):                        
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
            time.sleep(1)
            return 
        except AttributeError: 
                accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
                accept_cookies_button.click()
                time.sleep(1)
        except:
            pass
        
    def navigate_to_manga_page_1(self):
        manga_a_tag =  self.driver.find_elements(by=By.XPATH, value='//a[@class="name"]')
        a_tag_links = []
        for element in manga_a_tag:
            link = element.get_attribute('href')
            a_tag_links.append(link)
        html_links=[]
        for element in a_tag_links:
            if element =='https://www.waterstones.com/category/graphic-novels-manga/manga':
                html_links.append(element)
        manga_link = html_links[0]
        self.driver.get(manga_link)
        navigate_to_see_more_manga_page = self.driver.find_elements(by=By.XPATH, value='//a[@class="button button-teal"]')
        see_more_manga_page_list = []
        for element in navigate_to_see_more_manga_page:
            link = element.get_attribute('href') 
            see_more_manga_page_list.append(link)
        manga_page = []
        for element in see_more_manga_page_list:
            if element == 'https://www.waterstones.com/category/graphic-novels-manga/manga?page=1':
                manga_page.append(element)
        manga_page_1 = manga_page[0]
        
        return(manga_page_1)
    pass

    def get_website_links_manga_page_1(self,):
        navigate_to_manga_page_1 = self.navigate_to_manga_page_1()
        self.driver.get(navigate_to_manga_page_1)
        current_url = self.driver.current_url
        time.sleep(3)
        self.driver.find_element('xpath', '//body').send_keys(Keys.END)
        manga_page_container = self.driver.find_elements(by=By.XPATH,value='//div[@class="image-wrap"]/a')
        list_of_hmtl_links = []
        for element in manga_page_container:
            link = element.get_attribute('href')
            list_of_hmtl_links.append(link)
        self.driver.get(link)
        #print (list_of_hmtl_links)
        return (list_of_hmtl_links,current_url)
    pass

    def get_website_links_manga_page_2_to_page_5(self,):
        list_of_hmtl_links,current_url = self.get_website_links_manga_page_1()
        current_url = current_url[0:63]
        current_url = current_url + "/page/"
        list_of_manga_page_links = []
        for element in range (2,3):
            list_of_manga_page_links.append(f'{current_url}{element}')
            self.driver.get(current_url)
        for element in list_of_manga_page_links:
            self.driver.get(element)
            time.sleep(3)
            self.driver.find_element('xpath', '//body').send_keys(Keys.END)
            manga_container = self.driver.find_elements(by=By.XPATH,value='//div[@class="image-wrap"]/a')
            for element in manga_container:
                link = element.get_attribute('href')
                list_of_hmtl_links.append(link)
        print (list_of_hmtl_links)
        return (list_of_hmtl_links)
    pass

    def scrape_links_and_store_text_image_data(self,):
        #combined_list_of_html_links = self.get_website_links_manga_page_2_to_page_5()
        big_list_of_data_dictionaries=[]
        dict_properties = {'ISBNS':[],'Names': [], 'Authors': [], 'Publishers': [], 'Book_Formats':[], 'Descriptions': [],}
        link = 'https://www.waterstones.com/book/chainsaw-man-vol-1/tatsuki-fujimoto/9781974709939'
        self.driver.get(link)
        accept_cookies = self.accept_cookies()
        #image_ids = 'fa1a53bf-e3c3-478a-b3d9-4d24aebeb1f0'
        time.sleep(10)
        #dict_properties['IDS'].append(image_ids)
        ##timestamps = self.time_stamps_formated
       # dict_properties['Timestamps'].append(timestamps)
        isbn =self.driver.find_element(by=By.XPATH, value='//span[contains(@itemprop,"isbn")]').get_attribute("textContent")
        dict_properties['ISBNS'].append(isbn)
        name = self.driver.find_element(by=By.XPATH, value='//span[@class="book-title"]').text
        dict_properties['Names'].append(name)
        author = self.driver.find_element(by=By.XPATH, value= '//span[contains(@itemprop,"author")]').text
        dict_properties['Authors'].append(author)
        publisher = self.driver.find_element(by=By.XPATH, value='//span[contains(@itemprop,"publisher")]').get_attribute("textContent")
        dict_properties['Publishers'].append(publisher)
        book_format =  self.driver.find_element(by=By.XPATH, value='//span[@class="name"]').text
        dict_properties['Book_Formats'].append(book_format)
        description= self.driver.find_element(by=By.XPATH, value='//div[@class="tabs-content-container clearfix"]//div[@itemprop="description"]').text
        dict_properties['Descriptions'].append(description)
        image = self.driver.find_element(by=By.XPATH, value='//div[@class="book-image-main"]/img')
        img = image.get_attribute('src')
        img_content = requests.get(img).content
        #name = 'raw_data/images/manga/' +f'{self.date}_' + f'{image_ids}' + '.jpg'
        #with open (name,'wb') as handler:
            #handler.write(img_content)
            #big_list_of_data_dictionaries.append(dict_properties)
       # self.driver.quit()
        print (dict_properties) 
        return dict_properties
    
    def save_raw_dictionaries(self,big_list_of_data_dictionaries):
        with open("raw_data/data.json", mode="w", encoding= "utf-8") as file:
            file.write(json.dumps((big_list_of_data_dictionaries), default=str))   
    pass

def scrapper_method():
    scrapper = WaterstonesScrapper()
    scrapper.create_directory()
    accept = scrapper.accept_cookies()
    scrapper.navigate_to_manga_page_1()
    scrapper.get_website_links_manga_page_1()
    #scrapper.get_website_links_manga_page_2_to_page_5()
    #scrapper.scrape_links_and_store_text_image_data()
    #scrape = scrapper.save_raw_dictionaries()

pass

if __name__ == '__main__':
    scrapper_method()

