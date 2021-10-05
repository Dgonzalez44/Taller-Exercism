def count_words(sentence):
    s = sentence.lower()
    
    for punc in '.,;:!@#$%^&*()-_':
        s = s.replace(punc, ' ')
        
    list_words = [w.strip("'") for w in s.split()]
    word_counts = {}
    
    for palabra in set(list_words):
        word_counts.setdefault(palabra, list_words.count(palabra))
    return word_counts