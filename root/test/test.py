#%%
from main_v2 import WaterstonesScrapper
import unittest
import sys

class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.scrapper = WaterstonesScrapper()
        
    def test_accept_cookies(self,):
     value =  self.scrapper.accept_cookies()
     self.assertIsNotNone(value is not None)
      
    def test_navigate_to_manga_page_1(self):
     expected_value = 'https://www.waterstones.com/category/graphic-novels-manga/manga?page=1'
     actual_value = self.scrapper.navigate_to_manga_page_1()
     self.assertEqual(expected_value, actual_value)
        
    def test_get_website_links_manga_page_1(self):
      expected_value = ['https://www.waterstones.com/book/chainsaw-man-vol-1/tatsuki-fujimoto/9781974709939', 'https://www.waterstones.com/book/komi-cant-communicate-vol-1/tomohito-oda/9781974707126', 'https://www.waterstones.com/book/chainsaw-man-vol-11/tatsuki-fujimoto/9781974727117', 'https://www.waterstones.com/book/one-piece-vol-1/eiichiro-oda/9781569319017', 'https://www.waterstones.com/book/solo-leveling-vol-5/chugong/dubu/9781975344382', 'https://www.waterstones.com/book/the-promised-neverland-vol-1/kaiu-shirai/demizu-posuka/9781421597126', 'https://www.waterstones.com/book/chainsaw-man-vol-4/tatsuki-fujimoto/9781974717279', 'https://www.waterstones.com/book/chainsaw-man-vol-5/tatsuki-fujimoto/9781974719228', 'https://www.waterstones.com/book/my-hero-academia-vol-1/kohei-horikoshi/9781421582696', 'https://www.waterstones.com/book/toilet-bound-hanako-kun-vol-1/aidalro/aidalro/9781975332877', 'https://www.waterstones.com/book/the-liminal-zone/junji-ito/9781974726448', 'https://www.waterstones.com/book/bleach-20th-anniversary-edition-vol-1/tite-kubo/9781974735983', 'https://www.waterstones.com/book/spy-x-family-vol-2/tatsuya-endo/9781974717248', 'https://www.waterstones.com/book/chainsaw-man-vol-2/tatsuki-fujimoto/9781974709946', 'https://www.waterstones.com/book/chainsaw-man-vol-10/tatsuki-fujimoto/9781974725359', 'https://www.waterstones.com/book/haikyu-vol-1/haruichi-furudate/9781421587660', 'https://www.waterstones.com/book/spy-x-family-vol-8/tatsuya-endo/9781974734276', 'https://www.waterstones.com/book/death-note-short-stories/tsugumi-ohba/takeshi-obata/9781974730735', 'https://www.waterstones.com/book/spy-x-family-vol-1/tatsuya-endo/9781974715466', 'https://www.waterstones.com/book/chainsaw-man-vol-6/tatsuki-fujimoto/9781974720712', 'https://www.waterstones.com/book/chainsaw-man-vol-9/tatsuki-fujimoto/9781974724048', 'https://www.waterstones.com/book/look-back/tatsuki-fujimoto/9781974734641', 'https://www.waterstones.com/book/death-note-black-edition-vol-2/takeshi-obata/tsugumi-ohba/9781421539652', 'https://www.waterstones.com/book/attack-on-titan-1/hajime-isayama/9781612620244']
      actual_value = self.scrapper.get_website_links_manga_page_1()[0]
      self.assertListEqual(expected_value, actual_value)
      expected_value = 'https://www.waterstones.com/category/graphic-novels-manga/manga?page=1'
      actual_value = self.scrapper.get_website_links_manga_page_1()[1]
      self.assertEqual(expected_value, actual_value)
    
    def test_get_website_links_manga_page_2_to_page_5(self):
     expected_value = ['https://www.waterstones.com/book/chainsaw-man-vol-1/tatsuki-fujimoto/9781974709939', 'https://www.waterstones.com/book/komi-cant-communicate-vol-1/tomohito-oda/9781974707126', 'https://www.waterstones.com/book/chainsaw-man-vol-11/tatsuki-fujimoto/9781974727117', 'https://www.waterstones.com/book/one-piece-vol-1/eiichiro-oda/9781569319017', 'https://www.waterstones.com/book/solo-leveling-vol-5/chugong/dubu/9781975344382', 'https://www.waterstones.com/book/the-promised-neverland-vol-1/kaiu-shirai/demizu-posuka/9781421597126', 'https://www.waterstones.com/book/chainsaw-man-vol-4/tatsuki-fujimoto/9781974717279', 'https://www.waterstones.com/book/chainsaw-man-vol-5/tatsuki-fujimoto/9781974719228', 'https://www.waterstones.com/book/my-hero-academia-vol-1/kohei-horikoshi/9781421582696', 'https://www.waterstones.com/book/toilet-bound-hanako-kun-vol-1/aidalro/aidalro/9781975332877', 'https://www.waterstones.com/book/the-liminal-zone/junji-ito/9781974726448', 'https://www.waterstones.com/book/bleach-20th-anniversary-edition-vol-1/tite-kubo/9781974735983', 'https://www.waterstones.com/book/spy-x-family-vol-2/tatsuya-endo/9781974717248', 'https://www.waterstones.com/book/chainsaw-man-vol-2/tatsuki-fujimoto/9781974709946', 'https://www.waterstones.com/book/chainsaw-man-vol-10/tatsuki-fujimoto/9781974725359', 'https://www.waterstones.com/book/haikyu-vol-1/haruichi-furudate/9781421587660', 'https://www.waterstones.com/book/spy-x-family-vol-8/tatsuya-endo/9781974734276', 'https://www.waterstones.com/book/death-note-short-stories/tsugumi-ohba/takeshi-obata/9781974730735', 'https://www.waterstones.com/book/spy-x-family-vol-1/tatsuya-endo/9781974715466', 'https://www.waterstones.com/book/chainsaw-man-vol-6/tatsuki-fujimoto/9781974720712', 'https://www.waterstones.com/book/chainsaw-man-vol-9/tatsuki-fujimoto/9781974724048', 'https://www.waterstones.com/book/look-back/tatsuki-fujimoto/9781974734641', 'https://www.waterstones.com/book/death-note-black-edition-vol-2/takeshi-obata/tsugumi-ohba/9781421539652', 'https://www.waterstones.com/book/attack-on-titan-1/hajime-isayama/9781612620244', 'https://www.waterstones.com/book/chainsaw-man-vol-8/tatsuki-fujimoto/9781974722785', 'https://www.waterstones.com/book/blue-exorcist-vol-1/kazue-kato/9781421540320', 'https://www.waterstones.com/book/demon-slayer-kimetsu-no-yaiba-vol-3/koyoharu-gotouge/9781974700547', 'https://www.waterstones.com/book/chainsaw-man-vol-7/tatsuki-fujimoto/9781974720965', 'https://www.waterstones.com/book/animal-crossing-new-horizons-vol-1/kokonasu-rumba/9781974725922', 'https://www.waterstones.com/book/sailor-moon-1-naoko-takeuchi-collection/naoko-takeuchi/9781646512010', 'https://www.waterstones.com/book/komi-cant-communicate-vol-2/tomohito-oda/9781974707133', 'https://www.waterstones.com/book/one-piece-vol-2/eiichiro-oda/9781591160571', 'https://www.waterstones.com/book/berserk-volume-1/kentaro-miura/9781593070205', 'https://www.waterstones.com/book/demon-slayer-kimetsu-no-yaiba-vol-1/koyoharu-gotouge/9781974700523', 'https://www.waterstones.com/book/jujutsu-kaisen-vol-2/gege-akutami/9781974710034', 'https://www.waterstones.com/book/deadpool-samurai-vol-1/sanshiro-kasama/hikaru-uesugi/9781974725311', 'https://www.waterstones.com/book/jujutsu-kaisen-vol-17/gege-akutami/9781974732333', 'https://www.waterstones.com/book/assassination-classroom-vol-1/yusei-matsui/9781421576077', 'https://www.waterstones.com/book/grandmaster-of-demonic-cultivation-mo-dao-zu-shi-novel-vol-3/mo-xiang-tong-xiu/marina-privalova/9781638581567', 'https://www.waterstones.com/book/demon-slayer-kimetsu-no-yaiba-vol-6/koyoharu-gotouge/9781974700578', 'https://www.waterstones.com/book/jojos-bizarre-adventure-part-1-phantom-blood-vol-1/hirohiko-araki/9781421578798', 'https://www.waterstones.com/book/toilet-bound-hanako-kun-vol-3/aidairo/aidairo/9781975311353', 'https://www.waterstones.com/book/tokyo-revengers-omnibus-vol-1-2/ken-wakui/9781638585718', 'https://www.waterstones.com/book/one-piece-omnibus-edition-vol-1/eiichiro-oda/9781421536255', 'https://www.waterstones.com/book/heaven-officials-blessing-tian-guan-ci-fu-novel-vol-3/mo-xiang-tong-xiu/zeldacw/9781638582106', 'https://www.waterstones.com/book/heaven-officials-blessing-tian-guan-ci-fu-novel-vol-1/mo-xiang-tong-xiu/9781648279171', 'https://www.waterstones.com/book/the-promised-neverland-vol-2/kaiu-shirai/posuka-demizu/9781421597133', 'https://www.waterstones.com/book/love-is-an-illusion-vol-1/fargo/9781638585657']
     actual_value = self.scrapper.get_website_links_manga_page_2_to_page_5()
     self.assertListEqual(expected_value, actual_value)
       
    def test_scrape_links_and_store_text_image_data(self,):
      scrapper = WaterstonesScrapper()
      expected_value = {'ISBNS': ['9781974709939'], 'Names': ['Chainsaw Man, Vol. 1 - Chainsaw Man 1 (Paperback)'], 'Authors': ['Tatsuki Fujimoto'], 'Publishers': ['Viz Media, Subs. of Shogakukan Inc'], 'Book_Formats': ['Paperback'], 'Descriptions': ["Broke young man + chainsaw dog demon = Chainsaw Man!\n\nDenji was a small-time devil hunter just trying to survive in a harsh world. After being killed on a job, he is revived by his pet devil Pochita and becomes something new and dangerous-Chainsaw Man!\n\nDenji's a poor young man who'll do anything for money, even hunting down devils with his pet devil-dog Pochita. He's a simple man with simple dreams, drowning under a mountain of debt. But his sad life gets turned upside down one day when he's betrayed by someone he trusts. Now with the power of a devil inside him, Denji's become a whole new man-Chainsaw Man!"]}      
      actual_value =  self.scrapper.scrape_links_and_store_text_image_data()
      self.assertDictEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)
