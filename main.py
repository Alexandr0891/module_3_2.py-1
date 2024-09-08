# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
  # module_3_2.py
     # Тема"Способы вызова функции"
     # создаём функцию send_email
def send_email(message,recipient,sender = "university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")) or "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        #исправл ошибка в условии функции
        #   1 условие

        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}") #исправл ошибка "адреса"
    elif recipient == sender:
        #   2 условие
        print("Нельзя отправить письмо самому себе!")
        #   3 условие
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")#исправлены адреса
        #   4 условие
    elif sender !="university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса univer.help@gmail.com на адрес alexandr.@gmail.com.")
        #  результат:
send_email('Добрый день , Вас ждет новый урок! ','alexandr.gmail.com','university.help@gmail.com')
send_email('Вас ждет вебинар!','alexandr.@gmail.com','univer.help@gmail.com')
send_email('Добрый день,зайдите в личный кабинет','university.help@mail.com','university.help@mail.com')
send_email('Вы успешно выполнили задание! ','alexandr.@gmail.com','university.help@gmail.com')
# Проверка работы над ошибками
send_email('Обратите внимание на ошибки','rus.82@gmail.ru','university.help@gmail.com')
send_email('Обратите внимание на ошибки','rus.92@kk.net','university.help@gmail.com')
send_email('Обратите внимание на ошибки','rus.10@gmail.com','university.help@gmail.com')
send_email('Обратите внимание на ошибки','rus.87@gmail.g','university.help@gmail.com')