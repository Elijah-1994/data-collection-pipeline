#%%
from project.WaterstonesScrapper import WaterstonesScrapper
import unittest
import os
import requests
import time
import tempfile

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scrapper = WaterstonesScrapper()
     
    def test__create_directory(self):
        self.scrapper._WaterstonesScrapper__create_directory() # test to confirm method creates the correct folder directory
    
    def test_navigate_to_manga_page_1(self):
      expected_value = 'https://www.waterstones.com/category/graphic-novels-manga/manga?page=1'
      actual_value = self.scrapper.navigate_to_manga_page_1()
      self.assertEqual(expected_value, actual_value) # test to confirm if the url returned in the method is the correct url
      self.assertIsInstance(actual_value,str) # test to confirm if the returned variable is the correct data type.
      
    def test_get_website_links_manga_page_1(self): 
      actual_value = self.scrapper.get_website_links_manga_page_1()
      self.assertIsInstance(actual_value,tuple) #test to confirm if the returned variable is the correct data type.
      expected_value = 24
      actual_value = len(self.scrapper.get_website_links_manga_page_1()[0])
      self.assertEqual(expected_value, actual_value) # test to confirm method is scraping all of the hmtl links on page 1.
    
    def test_get_website_links_manga_page_2_to_page_5(self):
      actual_value = self.scrapper.get_website_links_manga_page_1()
      self.assertIsInstance(actual_value,tuple) #test to confirm if the returned variable is the correct data type.
      expected_value = 48
      actual_value = (self.scrapper.get_website_links_manga_page_2_to_page_5()[1]) # self.assertEqual(expected_value, actual_value) # test to confirm method is scraping all of the hmtl links from page 1 to page 5.
  
    def test_scrape_links_and_store_text_image_data(self):
      actual_value = self.scrapper.scrape_links_and_store_text_image_data()
      self.assertIsInstance(actual_value,list) # test to confirm if the returned variable is the correct data type
      #actual_value = self.scrapper.scrape_links_and_store_text_image_data()[0]
      #self.assertIsInstance(actual_value,dict) # test to confirm if the returned variable is the correct data type

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)
