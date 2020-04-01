palabra_secreta = "auto"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != palabra_secreta and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Adivine la palabra: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Muchas oportunidades, PERDISTE")
else:
    print("¡Ganaste!")
