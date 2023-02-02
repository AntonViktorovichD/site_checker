#!/usr/bin/python3

import telebot
import time
from multiprocessing.context import Process
import schedule
import urllib.request
from urllib.error import URLError

bot = telebot.TeleBot("#####################")
def send_message1():
    try:
        urllib.request.urlopen("http://www.grandgold.jewelry").getcode()
    except URLError as e:
        bot.send_message(#########, f"Error: {e}")

schedule.every(15).minutes.do(send_message1)

class ScheduleMessage():
    def try_send_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_process():
        p1 = Process(target = ScheduleMessage.try_send_schedule, args = ())
        p1.start()

if __name__ == '__main__':
    ScheduleMessage.start_process()
    try:
        bot.polling(none_stop = True)
    except:
        pas
