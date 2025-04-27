#==================#
# ANÁLISE DE DADOS #
#==================#

from textblob import TextBlob
from core.Utils import clean_text  # Função auxiliar

class SentimentAnalyzer:
    def __init__(self, blacklist=None):
        self.blacklist = blacklist or ["cu", "foda", "porra"]
    
    def analyze(self, text):
        cleaned_text = clean_text(text, self.blacklist)
        analysis = TextBlob(cleaned_text)
        return {
            "polarity": analysis.sentiment.polarity,
            "subjectivity": analysis.sentiment.subjectivity,
            "label": self._get_label(analysis.sentiment.polarity)
        }
    
    def _get_label(self, polarity):
        if polarity > 0.3:
            return "😊 Positivo"
        elif polarity < -0.3:
            return "😠 Negativo"
        return "😐 Neutro"