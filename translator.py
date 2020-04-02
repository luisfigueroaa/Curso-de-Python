def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            # incluir tambien a las mayusculas
            if letter.isupper():
                translation = translation + "G"
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Ingrese una frase: ")))
