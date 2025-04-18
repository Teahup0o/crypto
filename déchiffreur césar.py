alphabet = "abcdefghijklmnopqrstuvwxyz"

message_code = input("Message codé à décoder: ").lower()

print("\nTous les décalages :")
for decalage in range(26):
    message_clair = ""
    for lettre in message_code:
        if lettre in alphabet:
            pos = alphabet.find(lettre)
            nouvelle_pos = (pos - decalage) % 26
            message_clair += alphabet[nouvelle_pos]
        else:
            message_clair += lettre
    print(f"Décalage {decalage:2d} : {message_clair}")
