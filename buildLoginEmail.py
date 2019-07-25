# function that builds the email from prvided name, surname and domain.
# Checks the polish vowels and replaces them with latin counterparts.
# Function also formats the user input to lowercase.

def email(imie, nazwisko, emailFirmy):

    lowImie = list(imie.lower())
    imie0 = imie[0].lower()
    lowNazw = list(nazwisko.lower())
    polObj = {  
        "ą": "a",
        "ę": "e",
        "ó": "o",
        "ź": "z",
        "ż": "z",
        "ł": "l"
    }

    for x in range(len(lowNazw)):
        for y in polObj:
            if lowNazw[x] == y:
                lowNazw[x] = polObj[y]

    for x in range(len(lowImie)):
        for y in polObj:
            if lowImie[x] == y:
                lowImie[x] = polObj[y]

    lowImieStr = "".join(lowImie)
    lowNazwStr = "".join(lowNazw)

    print(lowImieStr + lowNazwStr + emailFirmy)
    print(imie0 + lowNazwStr)

email("Anna", "Kowalska", "@testowyemail.pl")


