def find_anagrams(word, candidatos):
    anagrams=[]
    alphabetical_word=sorted(word.upper())
    
    for candidate in candidatos:
        if word.upper()!=candidate.upper():
            if sorted(candidate.upper())==alphabetical_word:
                anagrams.append(candidate)
        
    return anagrams