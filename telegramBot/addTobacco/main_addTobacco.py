import telebot

#Для запуска писать в консоль python main_addTobacco.py

if __name__ == "__main__":
    #Чтение токена
    with open("config") as file:
        token = file.read()

    #Инициализация бота
    bot = telebot.TeleBot(token)
    print(123)
