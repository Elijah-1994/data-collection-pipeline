#%%
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from uuid import uuid4
import os
import requests
import time
import tempfile
import json
#%%
class WaterstonesScrapper:
    '''
        This class represents the process of using selenium webdriver to drive to waterstones.com and to scrape text and image data from the manga book section.
        Methods have been defined to take in html elements to scrape the data for the first 5 pages of the see more manga section.

        Attributes:
            driver: initialises the webdriver.chrome method to drive to the waterstones website.
            raw_data_dictionary: creates folder directory to store data.
            images_directory: creates folder directory to store image data.
            parent_directory : parent directory of the working folder location.
            time_stamps: intialises the datetime.now() method which returns the current date and time.
            time_stamps_formated: intialises the strftime.() method which returns the current date and time in string format.
    
    '''
    def __init__(self,):
        '''
        See help(WaterstoneScrapper) for accurate signature
        
        '''
        options = Options()
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        options.add_argument("start-maximized")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36')
        options.add_argument('no-sandbox')
        options.add_argument("disable-dev-shm-usage")
        self.driver = webdriver.Chrome(chrome_options=options) 
        self.driver.get("https://www.waterstones.com/")
        self.__images_directory ='raw_data/images' 
        self.__parent_directory = os.getcwd()
        self.time_stamps = datetime.now()
        self.time_stamps_formatted = self.time_stamps.strftime("%Y-%m-%d,%H:%M:%S")
        self.date = self.time_stamps.strftime("%Y-%m-%d")
    pass
    
    def __create_directory(self,):
        '''
        This function is used create the folder directories to store the json and image data. 
        
        '''
        parent_directory = self.__parent_directory
        images_directory = self.__images_directory
        path = os.path.join(parent_directory, images_directory) 
        try:
            os.makedirs(path, exist_ok = True)
        except OSError as error:
                return
    pass
    
    def __accept_cookies(self): 
        '''
        This function is used to the find the html element of the accept cookies button. 
        on the waterstones website and to click on the accept cookies button. waterstones website and to click on the accept cookies button.
        
        '''                         
        try:
            accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
            time.sleep(1)
        except AttributeError: 
                accept_cookies_button = self.driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
                accept_cookies_button.click()
                time.sleep(1)
        except:
            pass
        
    def navigate_to_manga_page_1(self)->str:  
        '''
        This function is used to drive to the manga book section on waterstone.com 
        and then to page 1 of the see more manga section.

        Returns:
            str: returns the page 1 web-link of the see more manga section in string format. 
        
        '''
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

    def get_website_links_manga_page_1(self,)->tuple:
        '''
        This function is used to  extract and store the website links of each manga book
        on page 1 of the see more manga section.
        
        Returns:
            tuple: returns the list of the web-links for each book on page 1 and
            the web-link of the current page 1 url in string format.
        
        '''
        navigate_to_manga_page_1 = self.navigate_to_manga_page_1()
        self.driver.get(navigate_to_manga_page_1)
        current_url = self.driver.current_url
        time.sleep(3)
        self.driver.find_element('xpath', '//body').send_keys(Keys.END)
        manga_page_container = self.driver.find_elements(by=By.XPATH,value='//div[@class="image-wrap"]/a')
        list_of_html_links = []
        for element in manga_page_container:
            link = element.get_attribute('href')
            list_of_html_links.append(link)
        self.driver.get(link)
        return (list_of_html_links,current_url)
    pass

    def get_website_links_manga_page_2_to_page_5(self,) ->list:
        '''
        This function is used to  extract and store the web-links of each manga book
        from pages 2 to page 5 and append to a list which contains the web-links for each book
        from page 1. 
        
        Returns:
            tuple: returns the list of the web-links for each book from page 1 to page 5 and the length of the list.
 
        '''
        list_of_html_links,current_url = self.get_website_links_manga_page_1()
        current_url = current_url[0:63]
        current_url = current_url + "/page/"
        list_of_manga_page_links = []
        for element in range (2,6):
            list_of_manga_page_links.append(f'{current_url}{element}')
            self.driver.get(current_url)
        for element in list_of_manga_page_links:
            self.driver.get(element)
            time.sleep(10)
            self.driver.find_element('xpath', '//body').send_keys(Keys.END)
            manga_container = self.driver.find_elements(by=By.XPATH,value='//div[@class="image-wrap"]/a')
            for element in manga_container:
                link = element.get_attribute('href')
                list_of_html_links.append(link)
        length_of_list_of_html_links = len(list_of_html_links)
        return (list_of_html_links,length_of_list_of_html_links)
    pass

    def scrape_links_and_store_text_image_data(self,) ->list:
        '''
        This function is used extract the text data from each web-link page of the books and store in a dictionary.
        This function also extracts the image data for each book and stores to the correct directory in jpg format.

        Returns:
            list: returns a list which contains a dictionary of data for each book.
            
        '''
        combined_list_of_html_links = self.get_website_links_manga_page_2_to_page_5()[0]
        big_list_of_data_dictionaries=[]
        for element in combined_list_of_html_links:
            dict_properties = {'IDS':[], 'Timestamps':[],'ISBNS':[],'Names': [], 'Authors': [], 'Publishers': [], 'Book_Formats':[], 'Descriptions': [],}
            self.driver.get(element)
            image_ids = str(uuid4())
            time.sleep(10)
            dict_properties['IDS'].append(image_ids)
            timestamps = self.time_stamps_formated
            dict_properties['Timestamps'].append(timestamps)
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
            name = 'raw_data/images/' +f'{self.date}_' + f'{image_ids}' + '.jpg'
            with open (name,'wb') as handler:
                handler.write(img_content)
            big_list_of_data_dictionaries.append(dict_properties)
        self.driver.quit()
        return big_list_of_data_dictionaries
    
    def __save_raw_dictionaries(self,big_list_of_data_dictionaries):
        '''
        This function is used to save the list which contains the dictionaries in json format.

        '''
        with open("raw_data/data.json", mode="w", encoding= "utf-8") as file:
            file.write(json.dumps((big_list_of_data_dictionaries), default=str))   
    pass

def scrapper_method():
    scrapper = WaterstonesScrapper()
    scrapper._WaterstonesScrapper__create_directory()
    scrapper._WaterstonesScrapper__accept_cookies()
    scrapper.navigate_to_manga_page_1()
    scrapper.get_website_links_manga_page_1()
    scrapper.get_website_links_manga_page_2_to_page_5()
    scrapper._WaterstonesScrapper__save_raw_dictionaries(scrapper.scrape_links_and_store_text_image_data())
pass

if __name__ == '__main__':
    scrapper_method()
