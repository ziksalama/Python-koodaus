user = "python"
password = "rules"
input_password = input("Syötä käyttäjätunnus:\n")
input_user = input("Syötä salasana:\n")

while input_user != user and input_password != password:
    print("Pääsy evätty\nYritä uudestaan")
    input_user = input("Syötä käyttäjätunnus:\n")
    input_password = input("Syötä salasana:\n")
print("Tervetuloa")