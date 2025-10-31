import random 
def xor (text, key):
    cyphertext = ""
    for i in range (len(text)):
        cyphertext += chr(ord(text[i]) ^ key[i])
    return cyphertext

text = input ("Ingresa la palabra")
key = [random.randint(0,1) for _ in range (len(text))]


