# import analisisTexto
# from analisisTexto import Feel

# prueba = Feel()
# textoEs ='Es un pesimo producto, no me llego en la talla que solicite. Aunque el material se ve de buena calidad y resistente al agua.'
# textoEn = "Thank you for being prepared for our meetings, Tom! By coming to each meeting with well-researched and thought-out ideas, you're helping us move forward in our process. I look forward to our next meeting."
# print('En espanol %s \nIngles: %s '%(prueba.get_Es(textoEs), prueba.get_En(textoEs)))
import os
# os.system('scrapy crawl textil -a filename=/home/moises/Practicas/lista.csv -o datos.csv')
from crawlerSelenium import CrawlerWeb
import pandas
"""
Cada pagina contiene: 
    url de busqueda 
    id del inputText para ingresar las busquedas 
    Contenedor de los resultados en formato css
    Enlaces en formato css
    Titulo de cada enlace en formato css
    boton de siguiente en formato xpath
Para google: 
    url de busqueda 'https://www.google.com/search?q='
    Text para ingresar las busquedas 'q'
    Contenedor de los resultados 'div.r'
    Enlaces 'a'
    Titulo de cada enlace 'h3.LC20lb.DKV0Md'
    boton de siguiente //a[@id="pnnext"]
Para bing
    url de busqueda 'https://www.bing.com/search?q='
    Text para ingresar las busquedas 'q'
    Contenedor de los resultados 'li.b_algo'
    Enlaces 'a'
    Titulo de cada enlace 'a'
    boton de siguiente '//a[@title="Página siguiente"]'
Para yahoo search
    url de busqueda 'https://espanol.search.yahoo.com/search?p='
    Text para ingresar las busquedas 'p'
    Contenedor de los resultados 'div.dd.algo'
    Enlaces 'a'
    Titulo de cada enlace 'h3.title'
    boton de siguiente '//a[@class="next"]' 
"""
# google = CrawlerWeb('https://www.google.com/search?q=')
# google.setElement(by='q')
# df = google.search(['Textiles de lana'], 'div.r', 'a', 'h3.LC20lb.DKV0Md','//a[@id="pnnext"]' , n_result=20)
# print(df)
# bing = CrawlerWeb('https://www.bing.com/search?q=')
# bing.setElement(by='q')
# df = bing.search(['Textiles de lana'], 'li.b_algo', 'a', 'a','//a[@title="Página siguiente"]', n_result=20)
# print(df)
#df.to_csv('test.csv', index=False)
yahoo = CrawlerWeb('https://espanol.search.yahoo.com/search?p=')
yahoo.setElement(by='p')
df = yahoo.search(['Textiles de lana'], 'div.dd.algo', 'a', 'h3.title','//a[@class="next"]' , n_result=20)
print(df)