alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Message à coder: ").lower()
decalage = int(input("Décalage:"))

code = ""
for lettre in message:
    if lettre in alphabet:
        position = alphabet.find(lettre)
        nouvelle_position = (position + decalage) % 26
        code += alphabet[nouvelle_position]
    else:
        code += lettre

print("Message codé:", code)

