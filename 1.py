import difflib

commands = ['hello','days to bd','add phone','add birthday','change phone','delete phone','find ','show all','good bye','exit','close','add','ads','help']

while True:
    user_input = input("Введіть команду: ")
    if user_input in commands:
        print(f"Виконую команду: {user_input}")
        '''
        Виконати дії для вірної команди
        '''
    else:
        suggestion = difflib.get_close_matches(user_input, commands, cutoff=0.45)
        # print(suggestion)
        if suggestion:
            print(f"Невідома команда. Можливо, ви мали на увазі: {', '.join(suggestion)}.")
        else:
            print("Невідома команда.")
