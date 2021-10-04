def response(hey_bob):

    if not hey_bob.strip():
        return "Fine. Be that way!"
    
    if hey_bob.strip()[-1] == "?":
        if hey_bob.strip().isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
        
    if hey_bob.strip().isupper():
        return "Whoa, chill out!"   

    return "Whatever."
pass