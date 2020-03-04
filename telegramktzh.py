# -*- coding: utf-8 -*-
import config
import telebot


token = config.token

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе    
    if (message.text.lower()==u'не могу найти оформленный билет' or message.text.lower()== u'не нашел купленный билет' or
         message.text.lower()==u'не пришел билет' or message.text.lower()== u'где мой билет'):
        bot.send_message(message.chat.id, 'Вы можете узнать статус своего заказа в личном кабинете в графе «Мои заказы».')
    elif (message.text.lower()==u'как зайти в личный кабинет?'):
        bot.send_message(message.chat.id, 'адрес электронной почты является вашим логином, восстановите пароль для входа в личный кабинет')
    else:
        bot.send_message(message.chat.id, 'Вы можете узнать статус своего заказа в личном кабинете в графе «Мои заказы».')
bot.polling(none_stop=True)
