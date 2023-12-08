# from parsel import Selector
# import requests
#
#
# class Supernatural:
#     URL = 'https://sverhestestvennoe.club/'
#     PLUS_URL = 'https://sverhestestvennoe.club/'
#     LINK_XPATH = '//a[@class="season_elem"]/@href'
#
#     def parse_data(self):
#         html = requests.get(self.URL).text
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         for link in links:
#             print(self.PLUS_URL + link)
#         return links[:5]
#
#
# if __name__ == '__main__':
#     scraper = Supernatural()
#     scraper.parse_data()
