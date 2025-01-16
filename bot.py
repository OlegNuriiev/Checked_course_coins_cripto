from pyowm import OWM
import telebot

owm = OWM('d79435e34e84bbbe667c1c5acf4c829b')
mgr = owm.weather_manager()
bot = telebot.TeleBot("1864387534:AAHYZORtN9jzPjs_lSNX-C4LJPlN35Sqsxw")


@bot.message_handler(content_types=['text'])
def send_echo(message):

    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас дубак. Надевай шубу"
    elif temp < 20:
        answer += "Сейчас холодно"
    else:
        answer += "Очень жарко."

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
