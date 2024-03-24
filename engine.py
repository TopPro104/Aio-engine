import os
import subprocess
print(os.getcwd())
directory = input("Enter directory name > ")  
os.chdir(directory)
print("Проверка")
if not os.path.isfile("filee.py"): 
    code = open("filee.py", "w+")
    code.write("from aiogram import Bot, types, Dispatcher \nfrom aiogram.utils import executor \nfrom aiogram.dispatcher.filters import Text \nfrom aiogram.dispatcher import FSMContext \nfrom aiogram.dispatcher.filters.state import State, StatesGroup \n")
    code.close()  
    print("Выполнено!")
    n = 0
else:
    n = 100

lang = input("Enter your language here: Eng/Rus > ")
if lang == "Rus":
    print("Приветствую в первой версии движка для создания бота на Aiogram,со всеми подробностями можно познакомиться в readme.txt")
    token = input("Введите токен своего бота ")
    print("[1] Добавить что-то в код  [2] Завершить создание \n[3] Ты не знаешь Aiogram  [4] Импорт библиотеки \n[5] Добавить start команду  [6] Скачать нужную версию aiogram")
else:
    print("Welcome to the first version of the engine for creating a bot on Aiogram, all the details can be found in readme.txt")
    token = input("Enter your bot token ")
    print("[1] Add something to the code [2] Complete creation \n[3] You don’t know Aiogram [4] Import the library \n[5] Add a start command [6] Download the required version of aiogram")
wastoken = False
if lang == "Rus":
    while n != 100:
        if wastoken == False:
            code = open("filee.py", "a+")
            code.write (f"TOKEN = '{token}' \nbot = Bot(token=TOKEN) \ndp = Dispatcher(bot) \n")
            code.close()
            wastoken = True
        n = int(input("Действие "))
        if n == 1:
            print("Введите имя кнопки")
            idk1 = input()
            code = open("filee.py", "a+")
            code.write (f"@dp.message_handler(Text(equals='{idk1}')) \nasync def start(message: types.Message): \n    ")
            print("Сделано,теперь напишите кол-во строк которое вы введете для этой команды")
            idk2 = int(input())
            for i in range (idk2):
                idk3 = input("Пишите код \n")
                code.write (f"{idk3} \n    ")
            code.write (f"\n")
            code.close()
            print("Завершено (После окончания действия над кнопкой ее нельзя изменять)")

        if n == 2:
            print("Завершение программы!")
            code = open("filee.py", "a+")
            code.write (f"if __name__ == '__main__': \n    executor.start_polling(dp, skip_updates=True)")
            code.close()
            print("Успешно! Если у вас возникли проблемы с кодом и ошибка в самом движке просьба обращаться @Samtakoiiii")
            n = 100

        if n == 3:
            print("Тебе к файлу help.txt")

        if n == 4:
            print("Надеюсь ты сюда попал до использования 1,итак,введи название библиотеки без import")
            lib = input()
            code = open("filee.py", "a+")
            code.write (f"from {lib} import * \n")
            code.close()

        if n == 5:
            print("Надеюсь ты сюда попал до использования 1,итак,введи название библиотеки без import")
            code = open("filee.py", "a+")
            code.write ("@dp.message_handler(commands=['start']) \nasync def start(message: types.Message): \n    ")
            print("Напишите на сколько строк будет ваш код для start команды")
            n = int(input())
            for i in range (n):
                idk4 = input()
                code.write (f"{idk4} \n    ")
            code.write("\n")
            code.close()

        if n == 6:
            current_directory = os.getcwd()
            bat_file_path = os.path.join(current_directory, "aioinstaller.bat")
            subprocess.call([bat_file_path])

    print("Код завершен")

else:
    while n != 100:
        if wastoken == False:
            code = open("filee.py", "a+")
            code.write (f"TOKEN = '{token}' \nbot = Bot(token=TOKEN) \ndp = Dispatcher(bot) \n")
            code.close()
            wastoken = True
        n = int(input("Action "))
        if n == 1:
            print("Enter a name for the button ")
            idk1 = input()
            code = open("filee.py", "a+")
            code.write (f"@dp.message_handler(Text(equals='{idk1}')) \nasync def start(message: types.Message): \n    ")
            print("Done, now write the number of lines you will enter for this command")
            idk2 = int(input())
            for i in range (idk2):
                idk3 = input("Write the code \n")
                code.write (f"{idk3} \n    ")
            code.write (f"\n")
            code.close()
            print("Completed (Once the button action is completed, it cannot be changed)")

        if n == 2:
            print("Completion of the program!")
            code = open("filee.py", "a+")
            code.write (f"if __name__ == '__main__': \n    executor.start_polling(dp, skip_updates=True)")
            code.close()
            print("Successfully! If you have any problems with the code or an error in the engine itself, please contact @Samtakoiiii")
            n = 100

        if n == 3:
            print("To your help.txt file")

        if n == 4:
            print("I hope you got here before using 1, so enter the name of the library without importing")
            lib = input()
            code = open("filee.py", "a+")
            code.write (f"from {lib} import * \n")
            code.close()

        if n == 5:
            code = open("filee.py", "a+")
            code.write ("@dp.message_handler(commands=['start']) \nasync def start(message: types.Message): \n    ")
            print("Write how many lines your code for the start command will be")
            n = int(input())
            for i in range (n):
                idk4 = input()
                code.write (f"{idk4} \n    ")
            code.write("\n")
            code.close()

        if n == 6:
            current_directory = os.getcwd()
            bat_file_path = os.path.join(current_directory, "aioinstaller.bat")
            subprocess.call([bat_file_path])

    print("Code ended")
        
