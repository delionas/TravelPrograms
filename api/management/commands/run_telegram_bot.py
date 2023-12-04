from django.core.management.base import BaseCommand
from api.models import Product

import telebot
bot = telebot.TeleBot("6306240090:AAEnZ-zC7jfYwa44T4_wZgWNhkUPC_POtdI") # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")
@bot.message_handler(commands=['products'])
def products(message):
    products = Product.objects.all()
    for product in products:
        bot.send_message(message.chat.id, product.name)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
