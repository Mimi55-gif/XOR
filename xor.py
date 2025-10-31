import random 
def xor (text, key):
    key = [random.randint(0,255) for _ in range(len(text))]
    cyphertext = ""
    for i in range (len(text)):
        cyphertext += chr(ord(text[i])) ^ ord(key[i% (len(key))])
        
    return cyphertext
