import re #ReGex
from nltk.corpus import stopwords #Textos limpos
from collections import Counter # Palavras frequentes


def clean_text(text, blacklist=None):
    blacklist = blacklist or []
    stopwords_pt = set(stopwords.words("portuguese"))
    
    # Remove menções, hashtags, números e símbolos
    text = re.sub(r"(@\w+|#\w+|\d+|[^\w\s])", "", text)
    
    # Filtro
    words = [
        word for word in text.split() 
        if word.lower() not in stopwords_pt 
        and word.lower() not in blacklist
        and len(word) > 2  # Palavrias pequenas ignoradas
    ]
    
    return " ".join(words)

def top_words(texts, n=5, exclude=None):
    exclude = exclude or []
    all_words = " ".join(texts).split()
    filtered = [word for word in all_words if word.lower() not in exclude]
    return Counter(filtered).most_common(n)