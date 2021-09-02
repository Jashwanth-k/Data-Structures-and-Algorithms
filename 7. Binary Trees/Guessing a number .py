
import random

number = random.randint(1,10)

for i in range(3):
    user = int(input('enter the number:'))
    if user == number:
        print('Hurray!')
        print(f"you guessed correct number it's:{number}")
        break
else:
    print(f"you guseesd wrong number it's:{number}")
