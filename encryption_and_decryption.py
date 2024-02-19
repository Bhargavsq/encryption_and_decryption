# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:39:57 2024
encryption  and decryption
@author: DC
"""

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's is the text after encryption : {cipher_text}")
    
def decryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's is the text after encryption : {cipher_text}")
    
wanna_end = False
while not wanna_end:
    what_to_do = input("type 'encrypt' for encryption , type 'decrypt' for decryption: \n")
    text=input("Type your message : \n")
    shift = int(input("Enter shift key : \n"))
    if what_to_do == "encrypt" & what_to_do == "Encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do == "decrypt" & what_to_do == "Decrypt":
        decryption(plain_text=text,shift_key=shift)
    play_again = input("Type yes to again play type no fro quite : \n")
    if play_again == "no" & play_again == "No" & play_again == "NO":
        wanna_end = True
        print("Have a nice day Bye...")
    
