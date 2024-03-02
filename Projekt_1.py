"""
Projekt_1.py: první projekt do Engeto Online Python Akademie.

Author: Petr Podolinský
Email: podolinsky.petr@gmail.com
Discord: Petr P. (podolinsky.petr)

TEXTOVÝ ANALYZÁTOR
============================================================
Tento program vyhodnotí, zda je uživatel registrovaný
a pokud ano, nabídne mu tři různé texty pro analýzu
četnosti výskytu slov dle zadaných kritérií.

Nakonec zobrazí histogram podle počtu znaků ve slovech.
"""
# Texty na výběr pro analýzu
from task_template import TEXTS

# Seznam registrovaných uživatelů
reg_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Hlavní část programu
print("$ python projekt1.py")

# Vstupní údaje o uživateli
username = input("Username: ")
password = input("Password: ")

# Ověření uživatele, zda patří mezi registrované - pokud ano,
# přivítání a nabídka výběru ze tří různých textů

if username in reg_users and reg_users[username] == password:
    print(40 * "-")
    print(f"Welcome to the app, {username}!")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(40 * "-")

    while True:
        try:
            vyber = int(input("Enter a number btw. 1 and 3 to select: "))
            if 1 <= vyber <= 3:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Uložení vybraného textu do proměnné vybrany_text,
    # rozdělení textu na slova a uložení do proměnné slova,
    # zavedení zatím prázdného slovníku delky_slov
    vybrany_text = TEXTS[vyber - 1]
    slova = vybrany_text.split()
    delky_slov = {}

    # Počáteční stav proměnných (nulování)
    pocet_titlecase = 0
    pocet_uppercase = 0
    pocet_lowercase = 0
    pocet_numeric = 0
    suma_numeric = 0

    # Analýza textu pomocí cyklu, hodnocení kritérií, čítač
    # Při výpočtu délky slova je odstraněna interpunkce
    # v rozsahu těchto znaků .,;?!
    for slovo in slova:
        delka = len(slovo.strip(".,;?!"))
        delky_slov[delka] = delky_slov.get(delka, 0) + 1

        if slovo.istitle():
            pocet_titlecase += 1
        elif slovo.isupper():
            pocet_uppercase += 1
        elif slovo.islower():
            pocet_lowercase += 1
        elif slovo.isnumeric():
            pocet_numeric += 1
            suma_numeric += int(slovo)

    # Výpis bloku s četnostmi dle jednotlivých druhů slov
    print(40 * "-")
    print(f"There are {len(slova)} words in the selected text.")
    print(f"There are {pocet_titlecase} titlecase words.")
    print(f"There are {pocet_uppercase} uppercase words.")
    print(f"There are {pocet_lowercase} lowercase words.")
    print(f"There are {pocet_numeric} numeric strings.")
    print(f"The sum of all the numbers {suma_numeric}")
    print(40 * "-")

    # Vytvoření společné proměnné max_delka_slova pro záhlaví i graf
    max_delka_slova = max(
        len(slovo) for text in TEXTS
        for slovo in text.split()
        )

    # Vytvoření formátovacího řetězce pro OCCURRENCES s centrováním
    print("LEN|", "OCCURRENCES".center(max_delka_slova + 4), "|NR.")
    print(40 * "-")

    # Zobrazení sloupcového grafu přímo v hlavní části kódu
    for delka, pocet in sorted(delky_slov.items()):
        graf_radek = '*' * pocet
        # Odsazení vpravo, tak aby byly znaky "|" pod sebou
        print(f"{delka:3}|{graf_radek.ljust(max_delka_slova + 5)} |{pocet}")

    # Hláška v případě, kdy uživatel nepatří mezi registrované
else:
    print("unregistered user, terminating the program..")
print()
