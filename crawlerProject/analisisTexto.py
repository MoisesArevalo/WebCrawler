from classifier import SentimentClassifier
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from collections import Counter
class Feel():
    sid = SentimentIntensityAnalyzer()
    def __init__(self):
        self.clf = SentimentClassifier()
    def getFeel(self, resultado):
        return 'Positivo' if resultado > 0.4 else ('Negativo' if resultado < -0.4 else 'Neutro') 
    def get_En(self, texto):
        """
        Puede retoranar valores [-1,1]
        mas cercanos a:
        -1: representa comentarios negativos
        0 : representa comentarios neutrales
        1 : representa comentarios positivos
        """
        resultado=[]
        resultado.append(self.getFeel(self.sid.polarity_scores(texto)['compound']))
        resultado.append(self.getFeel(TextBlob()))
        return 'Positivo' if resultado > 0.4 else ('Negativo' if resultado < -0.4 else 'Neutro') 
    def get_Es(self, texto):
        """
        Puede retoranar valores [0,1]
        mas cercanos a:
        0: representa comentarios negativos
        0.5 : representa comentarios neutrales
        1 : representa comentarios positivos
        """
        resultado=self.clf.predict(texto) 
        return 'Positivo' if resultado > 0.6 else ('Negativo' if resultado < 0.4 else 'Neutro') 