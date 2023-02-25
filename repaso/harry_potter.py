import random

# griffindor: valor
# slythering: ambicion
# hufflepuff: lealtad
# ravenclaw: sabiduria

class HatQuestion:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers

def get_answer():
    answer = int(input('Responde 1, 2, 3 o 4: '))
    if answer == 1 or answer == 2 or answer == 3 or answer == 4:
        return answer
    
    return get_answer()

hat_questions = [HatQuestion('Cómo te definirias?', [
                            ('1. valiente', 'griffindor'),
                            ('2. leal', 'hufflepuff'),
                            ('3. sabio', 'ravenclaw'),
                            ('4. ambicioso', 'slythering')]),
                HatQuestion('Cuál es tu clase favorita?', [
                            ('1. vuelo', 'griffindor'),
                            ('2. animales fantasticos', 'hufflepuff'),
                            ('3. pociones', 'ravenclaw'),
                            ('4. defensa contra las artes oscuras', 'slythering')]),
                HatQuestion('Donde pasarias mas tiempo?', [
                            ('1. Invernadero', 'griffindor'),
                            ('2. en la sala comun', 'hufflepuff'),
                            ('3. biblioteca', 'ravenclaw'),
                            ('4. explorando', 'slythering')]),
                HatQuestion('Cuál es tu color favorito?', [
                            ('1. rojo', 'griffindor'),
                            ('2. amarillo', 'hufflepuff'),
                            ('3. azul', 'ravenclaw'),
                            ('4. verde', 'slythering')]),
                HatQuestion('Cuál es tu mascota?', [
                            ('1. lechuza', 'griffindor'),
                            ('2. sapo', 'hufflepuff'),
                            ('3. gato', 'ravenclaw'),
                            ('4. serpiente', 'slythering')])]


houses = {
    'griffindor': 0,
    'slythering': 0,
    'hufflepuff': 0,
    'ravenclaw': 0,
}


for hat_question in hat_questions:
    print(hat_question.questions)
    for hat_answer in hat_question.answers:
        print(hat_answer[0])

    house = hat_question.answers[get_answer() - 1][1]
    houses[house] += 1
    print()

print(houses)

selected_house = []
max_points = 0

for house, points in houses.items():
    if points > max_points:
        selected_house.clear()
        selected_house.append(house)
        max_points = points
    elif points == max_points:
        selected_house.append(house)

if len(selected_house) == 1:
    print(f'Lo tengo claro... {selected_house[0].capitalize()}!!!')
else:
    print(f'Es complicado... {random.choice(selected_house).capitalize()}')

