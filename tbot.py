import telebot

import random

stories = [ "Ты почему так не любишь американцев? Да как представлю, что им раскладку клавиатуры не надо переключать",
            "Ты же программист? В электрике шаришь, получается. Надо траншею под кабель прокопать метров 500...",
            "То, что не удаётся запрограммировать на ассемблере, приходится паять!",
            "Чем отличается программист от политика? Программисту платят деньги за работающие программы"]

token = "7950525123:AAEyhUq51mAHa0CVlvZGC9DvoMPIco2pxAU"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, "/anekdot - показывает анекдоты")
    bot.send_message(message.chat.id, "/name - выводит ваше имя")

@bot.message_handler(content_types='text')
def story(message):
    if message.text == "/anekdot":
        story = stories[random.randint(0, 3)]
        bot.send_message(message.chat.id, story)
    elif message.text == "/name":
        bot.send_message(message.chat.id, "Рудольф")

    else:
        bot.send_message(message.chat.id, "Incorrect command")


bot.polling(none_stop=True, interval=0)


