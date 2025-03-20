from random import randint

computer_number = randint(0, 100)

while True:
    user_number = int(input('Введите своё число от 1 до 100: '))
    if 100 < user_number < 0:
        print('Uncorrect number!')
    elif computer_number > user_number:
        print('Your number is less than exprcted :(')
    elif computer_number < user_number:
        print('Your number is more than expected :(')
    elif computer_number == user_number:
        print('Wonderful!')
        break