# import analisisTexto
# from analisisTexto import Feel

# prueba = Feel()
# textoEs ='Es un pesimo producto, no me llego en la talla que solicite. Aunque el material se ve de buena calidad y resistente al agua.'
# textoEn = "Thank you for being prepared for our meetings, Tom! By coming to each meeting with well-researched and thought-out ideas, you're helping us move forward in our process. I look forward to our next meeting."
# print('En espanol %s \nIngles: %s '%(prueba.get_Es(textoEs), prueba.get_En(textoEs)))
import os
os.system('scrapy crawl textil -a filename=/home/moises/Practicas/lista.csv -o datos.csv')