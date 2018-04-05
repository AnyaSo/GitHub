import sys
users = {}
logins=[]
for user in users:
    logins.append(user)
active_login = ""

def auvtorize():
    read_file(logins,users)
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    active_login = login
    if login not in logins or password != users[login][0]:
        print("Вы ввели неправильный логин или/и пароль")
        auvtorize()
    print("\nВы зашли в аккаунт под логином "+login)
    check_role(active_login)

def registration(active_login):
    read_file(logins,users)
    print("\nДля регистрации вам понадобится ввести логин и пароль")
    login_usera = input("Введите логин: ")
    if (login_usera not in logins):
        password_usera = input("Введите пароль: ")
        pas=[]
        users[login_usera] = pas
        pas.append(password_usera)
        pas.append('False\n')
        logins.append(login_usera)
        print(users)
        print("Регистрация прошла успешно!\n")
        write_file(users,logins)
        main_menu()
    else:
        print("Такой логин уже зарегестрирован\n")
        registration(active_login)

def check_role(active_login):
    if (users[active_login][1] == 'True\n'):
        menu_admina (active_login)
    else:
        menu_usera (active_login)

def menu_admina(active_login):
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
        write_file(users,logins)
        main_menu()
    elif (choice_1 == 8):
        write_file(users,logins)
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
        write_file(users,logins)
        main_menu()
    elif (choice_2 == 4):
        write_file(users,logins)
        sys.exit()

def change_login(active_login):
    read_file(logins,users)
    new_login = input("Введите новый логин: ")
    if new_login not in logins:
        users[new_login] = users.pop(active_login)
        logins.remove(active_login)
        active_login = new_login
        logins.append(new_login+'\n')
        if users[active_login][1]==False:
            users[active_login][1]='False'
        if users[active_login][1]==True:
            users[active_login][1]='True'
        print(users)
        print("Ваш логин успешно изменен!\n")
        write_file(users,logins)
        check_role(active_login)
    else:
        print("Этот логин уже занят, попробуйте снова\n")
        change_login(active_login)

def change_pass(active_login):
    old_pas = input("Введите старый пароль: ")
    if (old_pas == users[active_login][0]):
        password = input("Введите новый пароль: ")
        users[active_login][0] = password
        if users[active_login][1] == True:
            users[active_login][1] = 'True'
        if users[active_login][1] == False:
            users[active_login][1] = 'False'
        r=users[active_login][1]
        print(users)
        print("Пароль успешно изменен\n")
        write_file(users,logins)
        check_role(active_login)
    else:
        print("Вы ввели неверный пароль\n")
        change_pass(active_login)
        
def reset_pass_user(active_login):
    login = input("Введите логин пользователя, у котрого хотите сбросить пароль: ")
    if login in logins:
        users[login][0] = '555'
        p = '555'
        r = users[login][1]
        print(users)
        write_file(users,logins)
        menu_admina(active_login)

def change_role(active_login):
    login = input("Введите логин аккаунта, у которого хотите изменить роль: ")
    if login in logins:
        users[login][1] = True
        print("Теперь "+login+" admin\n")
        r = users[login][1] = 'True\n'
        print(users)
        write_file(users,logins)
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
        pas.append('False\n')
        print(users)
        print("Регистрация прошла успешно!\n")
        write_file(users,logins)
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
        write_file(users,logins)
        sys.exit()
    elif (choice == 4):
        print(users)
        main_menu()

def write_file(users,logins):
    f = open('users.txt','w')
    for login in users:
        f.write(login+' '+users[login][0]+' '+users[login][1])
    f.close()

def read_file(logins,users):
    f = open('users.txt')
    s=f.readlines()
    for i in s:
        log=i.split(" ")[0]
        pas=i.split(" ")[1:]
        users[log]=pas
        if log not in logins:
            logins.append(log)
    print(users)
    f.close()
    
main_menu()

