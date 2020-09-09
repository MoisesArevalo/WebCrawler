import scrapy
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
import re
class WebUrl(Item):
    nombre = Field()
    url = Field()
class WebSpiderG(CrawlSpider):
    name ='Bgoogle'
    allowed_domain =['google.com']
    #start_urls =['https://www.google.com/search?q=textiles']
    # custom_settings = {
    #     'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    #     'CONCURRENT_REQUESTS': 5, 'DOWNLOAD_DELAY': 0, 'LOG_LEVEL': 'INFO'}
    # rules=(
    #      Rule(LinkExtractor(allow=r'start'))#start=20,
    #      Rule(LinkExtractor(allow=))
    # )
    def start_requests(self):
        search_url="https://www.google.com/search?q=textiles"
        yield scrapy.Request(search_url, callback=self.find_page, dont_filter=True)
    def find_page(self, response):
        #todo = response.xpath('//div[@class="r"]').getall()
        paginas = response.css('div.r').getall()
        # sel = Selector(response)
        # paginas= sel.xpath('//*[@id="rso"]/div')#//*[@id="rso"]/div[3]/div/div[1]/a')
        for pag in paginas:
            item = ItemLoader(WebUrl(), pag)
            # item.add_css('nombre','h3.LC20lb DKV0Md ::text')
            # item.add_xpath('url', './/a/@href/text()')
            item.add_value('nombre','e')
            item.add_value('url','www.com')
            yield item.load_item()
        # title = sel.xpath('//*[@id="rso"]/div[3]/div/div[1]/a/h3')
def is_google(a):
    url = a.attrib['href']
    return bool(re.search("/search", url))
class TestSpider(scrapy.Spider):
    name = "test"

    # How to get the start url
    # search `sukijan` on Google. And then go to second page, and then click first page result. You'll see that the url now includes `start` parameter. We'll use that for pagination
    # Also pay attention to parameter `q=sukijan`. That's our keyword
    # We use `% start for start in range(0, 100, 10)`. To generate urls that we want to crawl
    # So it will generate a list of urls like so
    # [q=sukijan start =0, q=sukijan start=10, q=sukijan start=20, q=sukijan, start=30... until 100]

    start_urls = [
        'https://www.google.com/search?q=sukijan&safe=strict&ei=sLTvXL_KH4zfz7sPpZOBuA4&start=%s&sa=N&ved=0ahUKEwi_4un2icPiAhWM73MBHaVJAOc4ChDx0wMIjQE&cshid=1559213273144254&biw=1680&bih=916' % start for start in range(0, 20, 10)
    ]

    def parse(self, response):
        # What is `jfp3ef a`
        # If you do `scrapy shell https://www.google.com/search?q=Sukijan&oq=sukijan&aqs=chrome.0.69i59j0l5.1739j0j7&sourceid=chrome&ie=UTF-8#ip=1`
        # And then do `view(response)`. It will open up a browser
        # From there do inspect element, locate a link, And you'll find that most of the links fall under `.jfp3ef` class
        for href in response.css('.jfp3ef a'):
            # We want to open url these links. But we don't want to open Google's url
            # For example url `More images for Sukijan`, etc.
            if not is_google(href):
                # This basically means 'Hey scrapy` follow this url.
                # When you find it run parse_text function on it.
                yield response.follow(href, self.parse_text)

    def parse_text(self, response):

        # get_text takes the response
        # And then it will takes all text whether it's in <p> tag, <h1> tag, <h2> tag etc
        # But it will leave everything inside <script> and <style>
        # It will also remove `\r`, `\n`, `\t`
        # Plus it combines all the text into a string, instead of a list

        def get_text(response):
            with_duplicated_space = ' '.join(response.xpath(
                './/text()[not(ancestor::script|ancestor::style|ancestor::noscript)]').extract()).strip().replace("\r", "").replace("\n", "").replace("\t", "")
            without_duplicated_space = re.sub(
                ' +', ' ', with_duplicated_space).strip()
            return without_duplicated_space

        yield {
            'title': response.css('title::text').get(),
            'text': get_text(response)
        }
