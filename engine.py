import os
import subprocess
import json
from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

def main():
    print(os.getcwd())
    directory = input("Enter directory name > ")  
    windows = True
    winda = input("You using windows? Yes/No > ")
    if winda == "Yes":
        windows = True
    elif winda == "No":
        windows = False
    os.chdir(directory)
    print("Проверка")
    if not os.path.isfile("filee.py"): 
        code = open("filee.py", "w+")   
        code.write("""from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
""")
        code.close()  
        print("Выполнено!")
        n = 0
    else:
        n = 100
    with open(f"lang/{input('Enter your language here: en/ru > ')}.json", "r", encoding="utf-8") as rfile:
        lang = json.load(rfile)
    print(lang["greeting"])
    token = input(lang["enter_token"])
    print(lang["menu"])
    wastoken = False
    while n != 100:
        if wastoken == False:
            code = open("filee.py", "a+")
            code.write (f"TOKEN = '{token}' \nbot = Bot(token=TOKEN) \ndp = Dispatcher(bot) \n")
            code.close()
            wastoken = True
        n = int(input(lang["act"]))
        match n:
            case 1:
                print(lang["enter_button"])
                idk1 = input()
                code = open("filee.py", "a+")
                code.write(f"@dp.message_handler(Text(equals='{idk1}')) \nasync def start(message: types.Message): \n    ")
                print(lang["enter_purpose"])
                idk2 = int(input())
                for _ in range (idk2):
                    idk3 = input(lang["type_code"])
                code.write(f"{idk3} \n    ")
                code.write(f"\n")
                code.close()
                print(lang["button_done"])

            case 2:
                print(lang["closing"])
                code = open("filee.py", "a+")
                code.write (f"if __name__ == '__main__': \n    executor.start_polling(dp, skip_updates=True)")
                code.close()
                print(lang["success_on_end"])
                n = 100

            case 3:
                print(lang["goto_help"])

            case 4:
                print(lang["before_1_qm"])
                lib = input()
                code = open("filee.py", "a+")
                code.write (f"from {lib} import * \n")
                code.close()

            case 5:
                print(lang["before_1_qm"])
                code = open("filee.py", "a+")
                code.write ("@dp.message_handler(commands=['start']) \nasync def start(message: types.Message): \n    ")
                print(lang["code_length"])
                n = int(input())
                for i in range (n):
                    idk4 = input()
                    code.write (f"{idk4} \n    ")
                code.write("\n")
                code.close()

            case 6:
                current_directory = os.getcwd()
                if windows == True:
                    bat_file_path = os.path.join(current_directory, "aioinstaller.bat")
                else:
                    bat_file_path = os.path.join(current_directory, "aioinstaller.sh")
                subprocess.call([bat_file_path])
            case 7:
                print(lang["tokencheck"])
                TOKEN = input()
                bot = Bot(token=TOKEN)
                dp = Dispatcher(bot)
                try:
                    if __name__ == '__main__':
                        executor.start_polling(dp, skip_updates=True)
                except:
                    print("The token is incorrect")
                

    print(lang["done"])


if __name__ == "__main__":
    main()
else:
    print("You are not supposed to open this as a module")
    raise TypeError
