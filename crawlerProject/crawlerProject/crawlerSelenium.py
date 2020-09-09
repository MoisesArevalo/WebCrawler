from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pandas import DataFrame
from random import randint
from selenium.common.exceptions import NoSuchElementException
from time import sleep
class CrawlerWeb():
    elem = None
    driver = webdriver.Chrome()
    df = DataFrame(columns=['titulo','url'])
    def __init__(self, url):
        self.driver.get(url)
#driver.get("https://www.google.com/search?q=")
# assert "Google" in driver.title
    def setElement(self, by='q'):
        self.elem = self.driver.find_element_by_name(by)
        self.elem.clear()
    def search(self, keys=[], css_selector='', url_selector='', name_selector='', next_element='',n_result=10):
        n_page=0
        next = None
        for key in keys:
            self.elem.send_keys(key)
            self.elem.send_keys(Keys.RETURN)
            while (len(self.df)<n_result):
                lista = self.driver.find_elements_by_css_selector(css_selector)
                for elem in lista:
                    title = elem.find_element_by_css_selector(name_selector)
                    url = elem.find_element_by_css_selector(url_selector).get_attribute("href")
                    self.df = self.df.append({'titulo':title.text, 'url':url},ignore_index=True)
                sleep(randint(8,15))
                try:
                    # next = self.driver.find_element_by_link_text('Siguiente')next_element
                    next=self.driver.find_element_by_xpath(next_element)
                    next.click()
                except NoSuchElementException:
                    break
        return self.df
    #driver.close()