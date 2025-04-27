#==================================#
# funções utilitárias reutilizávei #
#==================================#

from collections import Counter # Palavras frequentes

def clean_text(text, blacklist): #Remove palavras específicas
    return " ".join([word for word in text.split() if word.lower() not in blacklist])

def top_words(texts, n=5, exclude=None):
    """Retorna as n palavras mais frequentes, excluindo termos opcionais."""
    exclude = exclude or []
    all_words = " ".join(texts).split()
    filtered = [word for word in all_words if word.lower() not in exclude]
    return Counter(filtered).most_common(n)