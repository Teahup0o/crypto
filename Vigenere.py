alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Message à coder: ").lower()
cle = input("Clé secrète (mot): ").lower()

cle_longue = (cle * (len(message)//len(cle) + 1))[:len(message)]

message_code = ""
for i in range(len(message)):
    lettre_message = message[i]
    lettre_cle = cle_longue[i]
    
    if lettre_message in alphabet:
 
        pos_message = alphabet.find(lettre_message)
        pos_cle = alphabet.find(lettre_cle)
        
        nouvelle_pos = (pos_message + pos_cle) % 26
        message_code += alphabet[nouvelle_pos]
    else:
        message_code += lettre_message

print("Message codé:", message_code)
