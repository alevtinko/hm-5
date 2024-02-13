how_are_you = input('Hello, how are you?\n')

name = input(f'Great, that you are {how_are_you}! What is your name?\n')

old = input(f'Hello, {name}! How old are you?\n')

year_of_birth = input(f'I see, you were born in year {2024 - int(old)}? Let me know if it is True or False?\n').lower

if year_of_birth == 'True':
    year_of_birth = 2024 - int(old)
    print(f'Great, then {year_of_birth} is your birth year!\n')

else:
    year_of_birth = 2023 - int(old)
    print(f'Great, then {year_of_birth} is your birth year!\n')

