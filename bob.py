def response(hey_bob):
    if hey_bob.endswith("?") and not hey_bob.isupper:
        bob = "Sure."
    elif hey_bob.endswith("?") and hey_bob.isupper():
        bob = "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        bob =  "Whoa, chill out!"
    elif hey_bob == "" or hey_bob.isspace():
        bob = "Fine. Be that way!"
    else:
        bob = "Whatever."
        
    return bob