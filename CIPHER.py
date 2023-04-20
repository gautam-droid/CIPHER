#cipher--encrypting and decrypting messages

import sys

#asking user whether to encypt or decrypt``
while True:
    #inputted message
    inp_action=input('enter the action you want to do >>>>>>')
    print("Type either encrypt/decrypt or end to terminate the program")
    if(inp_action.lower().startswith('end')):  
     print("Program terminated!!")
     sys.exit(0)
         
    
    elif(inp_action.lower().startswith('encrypt')):
        action='encrypt'
        break
    
    elif(inp_action.lower().startswith('decrypt')):
        action='decrypt'
        break
cap_message=inp_action.upper()
Symbols=[chr(i) for i in range(65,91)]

#asking user continously to enter the key length
while True:
    key_ask=(input("Enter the key length in numbers"))
    print(key_ask)
    if (0<=int(key_ask)<len(Symbols) and key_ask.isdecimal()):
     key=key_ask
     break
    else:
        print("enter a valid key from 0 to {}".format(len(Symbols)))

#asking user to input message to encrypt/decrypt
ask_msg=input("Enter the message to be {}ed".format(action)).upper()
translated=''
        
#encrypting messages
for each_letter in ask_msg:
        if(each_letter in Symbols):
            find_number=Symbols.index(each_letter)
            if (action=='encrypt'):
                find_number=find_number+int(key)         
            elif(action=='decrypt'):
                find_number=find_number-int(key)      
            
#Handling the wrap-around................................            
            if find_number>=len(Symbols):
                find_number=find_number-len(Symbols)
            elif find_number<0:
                find_number=find_number+len(Symbols)
            translated=translated+Symbols[find_number]

print(translated)
