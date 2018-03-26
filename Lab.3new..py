users = []
ready_log = "qwe"
ready_pas = "222"
ready_user = [ready_log, ready_pas]
users.append(ready_user)


print(users)
while (True):
    all_logins=[]
    for user in users:
        all_logins.append(user[0])   
    all_pas=[]
    for us in users:
        all_pas.append(us[1])
    print("Веберите действие: ")
    print("1) Вход ")
    print("2) Зарегестрироваться ")
    print("3) Выход ")
    print("4) Показать список ")
    choice = int(input("Ваш выбор: "))
    import sys


                   #Вход
    if (choice == 1):
        print(users)
        print(all_logins)
        print(all_pas)
        login = input("Введите логин: ")
        password = (input("Введите пароль: "))
        if (login not in all_logins) or (password not in all_pas):
            print("Такой пользователь не найден")
        else:
           
                print("\nВы вошли в систему. \nВаше дальнейшее действие?")
                print("1) Изменить логин")
                print("2) Изменить пароль")
                print("3) Удалить учетную запись")
                print("4) Выход")
                
                choice_1 = int(input("Ваш выбор: "))

                                        #Изменяем логин
                if (choice_1 == 1):
                    print(all_logins)
                    new_login = input("Введите новый логин: ")
                    old_login = login
                    if old_login in all_logins:
                        position = 0
                        for i in range(len(all_logins)):
                            if old_login == all_logins[i]:
                                position = i

                        users[position][0] = new_login
                        print(users)
                        print("Ваш логин успешно изменен!\n")
                        
                        
                       #Изменяем пароль
                elif (choice_1 == 2):
                    print(all_pas)
                    old_pas = input("Введите старый пароль: ")
                    print(all_pas)
                    if old_pas in all_pas:
                        new_pas = input("Введите новый пароль: ")
                        pos = 0
                        for i in range(len(all_pas)):
                            if old_pas == all_pas[i]:
                                pos = i
                        users[pos][1] = new_pas
                        print("Ваш пароль успешно изменен!\n")


                          #Удаление
                elif (choice_1 == 3):
                    old_login = login
                    if old_login in all_logins:
                        posit = 0
                        for i in range(len(all_logins)):
                            if old_login == all_logins[i]:
                                posit = i
                        del users[posit]
                        print("Вы удалили свой аккаунт\n")

                        
                elif choice_1 == 4:
                    choice = 0





            #Регистрация
    elif (choice == 2):
        print("\nДля регистрации вам понадобится ввести логин и пароль")
        login_new = input("Введите логин: ")
        if (login_new not in all_logins):
            password_new= input("Введите пароль: ")
            new=[login_new,password_new]
            users.append(new)
            print("Вы зарегистрированны! \nДобро пожаловать на сайт!\n")
        else:
            print("Пользователь с таким логином уже зарегестрирован")


                #Выход
    elif (choice == 3):
        sys.exit()


                #Показать список пользователей
    elif (choice == 4):
        print(users)

    

    
    

