from Question import Question

questions_prompts = [
    '¿De qué color son las manzanas?\n(a) Rojas/Verdes\n(b) Moradas\n(c) Naranjas\n\n',
    '¿De que color son los plátanos?\n(a) Azul\n(b) Magenta\n(c) Amarillo\n\n',
    '¿De que color son las uvas?\n(a) Amarillas\n(b) Moradas\n(c) Azules\n\n'
]

questions = [
    Question(questions_prompts[0], 'a'),
    Question(questions_prompts[1], 'c'),
    Question(questions_prompts[2], 'b'),
]


def run_test(questions):
    score = 0
    for question in questions:  # Por cada pregunta dentro de preguntas
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\nTienes  "+str(score)+" de "+str(len(questions))+" correctas\n")


run_test(questions)
