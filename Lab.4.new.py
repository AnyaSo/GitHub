import sys
users = {
    "admin": ['222',True],
    "anya": ['555',False]
    }
logins=[]
for user in users:
    logins.append(user)
active_login = ""

def auvtorize():
    login = input("Введите логин: ")
    while login not in logins:
        login = input("Введите логин: ")
    password = input("Введите пароль: ")
    while password != users[login][0]:
        password = input("Введите пароль: ")
    active_login = login
    print("\nВы зашли в аккаунт под логином "+login)
    check_role(active_login)

def registration(active_login):
    print("\nДля регистрации вам понадобится ввести логин и пароль")
    login_usera = input("Введите логин: ")
    if (login_usera not in logins):
        password_usera = input("Введите пароль: ")
        pas=[]
        users[login_usera] = pas
        pas.append(password_usera)
        pas.append(False)
        logins.append(login_usera)
        print(users)
        print("Регистрация прошла успешно!\n")
        main_menu()
    else:
        print("Такой логин уже зарегестрирован")
        registration(active_login)

def check_role(active_login):
    if (users[active_login][1] == True):
        menu_admina (active_login)
    else:
        menu_usera (active_login)

def menu_admina(active_login):
    print("\nВы вошли в систему как admin. \nВаше дальнейшее действие?")
    print("1) Создать пользователя")
    print("2) Изменить свой логин")
    print("3) Изменить свой пароль")
    print("4) Сбросить пароль пользователя")
    print("5) Список пользователей")
    print("6) Изменить роль пользователя")
    print("7) Выход из аккаунта")
    print("8) Выход из програмы")
    choice_1 = int(input("Ваш выбор: "))
    if (choice_1 == 1):
        create_user(active_login)
    elif (choice_1 == 2):
        change_login(active_login)
    elif (choice_1 == 3):
        change_pass(active_login)
    elif (choice_1 == 4):
        reset_pass_user(active_login)
    elif (choice_1 == 5):
        print(users)
        menu_admina(active_login)
    elif (choice_1 == 6):
        change_role(active_login)
    elif (choice_1 == 7):
        main_menu()
    elif (choice_1 == 8):
        sys.exit()

def menu_usera(active_login):
    print("1) Изменить свой логин")
    print("2) Изменить свой пароль")
    print("3) Выход из аккаунта")
    print("4) Выход из программы")
    choice_2 = int(input("Ваш выбор: "))
    if (choice_2 == 1):
        change_login(active_login)
    elif (choice_2 == 2):
        change_pass(active_login)
    elif (choice_2 == 3):
        main_menu()
    elif (choice_2 == 4):
        sys.exit()

def change_login(active_login):
    new_login = input("Введите новый логин: ")
    if new_login not in logins:
        users[new_login] = users.pop(active_login)
        logins.remove(active_login)
        active_login = new_login
        logins.append(new_login)
        print(users)
        print("Ваш логин успешно изменен!\n")
        check_role(active_login)
    else:
        print("Этот логин уже занят, попробуйте снова")
        change_login(active_login)

def change_pass(active_login):
    old_pas = input("Введите старый пароль: ")
    if (old_pas == users[active_login][0]):
        password = input("Введите новый пароль: ")
        users[active_login][0] = password
        print(users)
        print("Пароль успешно изменен\n")
        check_role(active_login)
    else:
        print("Вы ввели неверный пароль")
        change_pass(active_login)
        
def reset_pass_user(active_login):
    login = input("Введите логин пользователя, у котрого хотите сбросить пароль: ")
    if login in logins:
        users[login][0] = "555"
        print(users)
        menu_admina(active_login)

def change_role(active_login):
    login = input("Введите логин аккаунта, у которого хотите изменить роль: ")
    if login in logins:
        users[login][1] = True
        print("Теперь "+login+" admin")
        print(users)
        check_role(active_login)
    else:
        print("Неверный логин")
        change_role(active_login)

def create_user(active_login):
    print("\nДля регистрации вам понадобится ввести логин и пароль")
    login_usera = input("Введите логин: ")
    if (login_usera not in logins):
        password_usera = input("Введите пароль: ")
        users[login_usera] = password_usera
        logins.append(login_usera)
        pas = []
        users[login_usera] = pas
        pas.append(password_usera)
        pas.append(False)
        print(users)
        print("Регистрация прошла успешно!\n")
        menu_admina(active_login)
    else:
        print("Такой логин уже зарегестрирован")
        create_user(active_login)

def main_menu():
    print("\nВеберите действие: ")
    print("1) Вход ")
    print("2) Зарегестрироваться ")
    print("3) Выход ")
    print("4) Показать список ")
    choice = int(input("Ваш выбор: "))
    if (choice == 1):
        auvtorize()
    elif (choice == 2):
        registration(active_login)
    elif (choice == 3):
        sys.exit()
    elif (choice == 4):
        print(users)
        main_menu()

main_menu()

