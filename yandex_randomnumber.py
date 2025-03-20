from random import randint

computer_number = randint(0, 100)

while True:
    user_number = int(input('Введите своё число от 1 до 100: '))
    if 100 < user_number < 0:
        print('Uncorrect number!')
    if computer_number > user_number:
        print('Your number is less than exprcted :(')
    if computer_number < user_number:
        print('Your number is more than expected :(')
    if computer_number == user_number:
        print('Wonderful!')
        break