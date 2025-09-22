"""Module de vérification de palindromes."""

import unicodedata

def ispalindrome(s):
    """Vérifie si une chaîne est un palindrome."""
    # Met tout en minuscules
    s = s.lower()

    # Supprime les accents
    s = ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )
    # Supprime les caractères non alphanumériques
    s = ''.join(c for c in s if c.isalnum())

    # Compare avec la version inversée
    return s == s[::-1]


def main():
    """Fonction principale de test."""
    exemples = [
        "radar", "kayak", "level", "rotor", "civique", "deifié",
        "Élu par cette crapule", "A man, a plan, a canal, Panama", "Noël léon",
        "12321", "python", "bonjour"]

    for s in exemples:
        print(f"{s} -> {ispalindrome(s)}")


if __name__ == "__main__":
    main()
