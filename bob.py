def response(hey_bob):
    if hey_bob.isupper():
        bob =  "Whoa, chill out!"
    if hey_bob.endswith("?"):
        bob = "Sure."
    if hey_bob.endswith("?") and hey_bob.isupper():
        bob = "Calm down, I know what I'm doing!"
    if hey_bob == "":
        bob = "Fine. Be that way!"
    else:
        bob = "Whatever."
        
    return bob