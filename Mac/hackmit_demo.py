#!/usr/bin/python

import os
import time
import tkinter
from tkinter import *
from tkinter import messagebox

def notify(title, subtitle, message):
    '''
    Mac notifications
    '''
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

root = tkinter.Tk()
root.withdraw()
widget_list = []

def sleep():
    '''
    Dims screen
    '''
    root.withdraw()
    for image in widget_list:
        image.pack_forget()
    os.system("pmset displaysleepnow -t 10; sleep 10; caffeinate -u -t 1") # change the numbers for dim time in seconds

def showimage(i):
        # you can add more gifs to go along with your messages
        image_dict = {1:"", 2:"", 3:"", 4:"", 5:"5.gif", 6:"12.gif", 7:"", 8:"", 9:"", 10:"", 11:"", 12:"12.gif"}
        pusheen = PhotoImage(file=image_dict[i])
        pusheen_context = Label(image=pusheen)
        pusheen_context.image = pusheen
        pusheen_context.pack()
        widget_list.append(pusheen_context)

def main():
    '''
    Prompts user to take a rest. If they comply, dim screen for 20 seconds
    If they don't comply, send reminders/messages/fun facts every 10 minutes until they do
    '''

    latent_time = 10 # 1200 sec = 20 min in between rests
    time_between_reminders = 4 # 600 sec = 10 min in between reminders
    prompt_message = "Do you want to take a rest?"
    messages =  {1: "Pusheen would want you to take a break too.",
                 2: "It's been 30 minutes since your last break. Just look away. It's not that hard.",
                 3: "Spending hours on a computer can strain the eye muscles to cause headaches. " + 
                    "I spy a headache coming your way...",
                 4: "If you go blind, from not resting, you won't be able to enjoy our sassy messages. Wouldn't that be sad?",
                 5: "Bro.",
                 6: "Maybe you need some factual motivation: Your blink rate slows down when you look at things that are closer to your face (like your laptop), " + 
                    "exacerbating dry eyes and itchiness. Do you suffer from dry eyes? Now, you know why. Take a break.",
                 7: "You know.. it's been...80 minutes since your last break? What are you doing that's so time-sensitive? Or are you just lazy?",
                 8: "Here's a fact to motivate you, you poor sufferer of eye strain... " + 
                    "'A large majority, nearly 70%, of Millennials report symptoms of digital eye strain.' Don't be in that 70%.",
                 9: "Don't go blind. I don't want you to go blind... because that'd mean my efforts were for naught.",
                 10: "If you don't rest your eyes soon, you may start to notice: blurred vision, double vision, dry red eyes, eye irritation, " + 
                     "headaches, neck or back pain...and maybe even death...",
                 11: "Dude.",
                 12: "Wow, we've run out of sass to sass you with and that says something: You REALLY need to rest your eyes...",
                 'title': 'Eye Break',
                 'subtitle': 'With 20/20/20',
                 'message_20': "It's been 20 min! Click on the Python Eye-Con to take a 20 sec break!",
                 'message_10': "It's been another 10 min! Click on the Python Eye-Con to take a 20 sec break!"
                 }    
    number_messages = 12

    sass_factor = 0 # number of times user hit snooze 
    complied = False
    while True:
        root.update()
        if complied:
            notify(messages['title'],
                   messages['subtitle'],
                   messages['message_20'])
        if tkinter.messagebox.askyesno("EYE BREAK", prompt_message):
            complied = True
            sleep()
            time.sleep(latent_time)
            sass_factor = 0
        else:
            complied = False
            showimage(sass_factor + 1)
            root.update()
            root.deiconify()
            sass_factor += 1
            time.sleep(time_between_reminders)
            if sass_factor != 0:
                if sass_factor <= len(messages):
                    notify(messages['title'],
                           messages['subtitle'],
                           messages['message_10'])
                    tkinter.messagebox.showinfo("FUN FACT", str(messages[sass_factor]))
                else:
                    notify(messages['title'],
                           messages['subtitle'],
                           messages['message_10'])
                    tkinter.messagebox.showinfo("FUN FACT", str(messages[number_nessages]))


main()
