#%%
from project.WaterstonesScrapper import WaterstonesScrapper
import unittest
import sys

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scrapper = WaterstonesScrapper()
        
    #def test_navigate_to_manga_page_1(self):
      #expected_value = 'https://www.waterstones.com/category/graphic-novels-manga/manga?page=1'
      #actual_value = self.scrapper.navigate_to_manga_page_1()
      #self.assertEqual(expected_value, actual_value) # test to confirm if the url returned in the method is the correct url
      #self.assertIsInstance(actual_value,str) # test to confirm if the returned variable is the correct data type.
      
    #def test_get_website_links_manga_page_1(self): 
      #actual_value = self.scrapper.get_website_links_manga_page_1()
      #self.assertIsInstance(actual_value,tuple) #test to confirm if the returned variable is the correct data type.
     # expected_value = 24
     # actual_value = len(self.scrapper.get_website_links_manga_page_1()[0])
     # self.assertEqual(expected_value, actual_value) # test to confirm method is scraping all of the hmtl links on page 1.
    
    #def test_get_website_links_manga_page_2_to_page_5(self):
      #actual_value = self.scrapper.get_website_links_manga_page_1()
      #self.assertIsInstance(actual_value,tuple) #test to confirm if the returned variable is the correct data type.
     # expected_value = 120
     # actual_value = (self.scrapper.get_website_links_manga_page_2_to_page_5()[1])
     # self.assertEqual(expected_value, actual_value) # test to confirm method is scraping all of the hmtl links from page 1 to page 5.

    def test_scrape_links_and_store_text_image_data(self,):
      scrapper = WaterstonesScrapper()
     # expected_value = {'ISBNS': ['9781974709939'], 'Names': ['Chainsaw Man, Vol. 1 - Chainsaw Man 1 (Paperback)'], 'Authors': ['Tatsuki Fujimoto'], 'Publishers': ['Viz Media, Subs. of Shogakukan Inc'], 'Book_Formats': ['Paperback'], 'Descriptions': ["Broke young man + chainsaw dog demon = Chainsaw Man!\n\nDenji was a small-time devil hunter just trying to survive in a harsh world. After being killed on a job, he is revived by his pet devil Pochita and becomes something new and dangerous-Chainsaw Man!\n\nDenji's a poor young man who'll do anything for money, even hunting down devils with his pet devil-dog Pochita. He's a simple man with simple dreams, drowning under a mountain of debt. But his sad life gets turned upside down one day when he's betrayed by someone he trusts. Now with the power of a devil inside him, Denji's become a whole new man-Chainsaw Man!"]}      
      actual_value =  self.scrapper.scrape_links_and_store_text_image_data()
      self.assertIsInstance(actual_value,list)
     # self.assertDictEqual(expected_value, actual_value)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)
