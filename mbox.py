import os
import time
import tkinter
from tkinter import messagebox

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function
notify(title    = 'A Real Notification',
       subtitle = 'with python',
       message  = 'Hello, this is me, notifying you!')

root = tkinter.Tk()
root.withdraw()

def sleep():
    os.system("pmset displaysleepnow -t 1200; sleep 1200; caffeinate -u -t 1")
    root.withdraw()

sass_dict = {1: "Spending hours on a computer or hand-held device keeps the eyes converged and strains the eye muscles to cause headaches.",
             2: "It's been 30 minutes since your last break. Just look away. It's not that hard.",
             3: "Remember, how we told you that spending hours on a computer can strain the eye muscles to cause headaches? I foresee a headache \
coming your way...",
             4: "If you go blind, from not resting, you won't be able to enjoy our sassy messages. Wouldn't that be sad?",
             5: "Bro.",
             6: "Maybe you need some factual motivation: Your blink rate slows down when you look at things that are closer to your face \
(like your laptop), exacerbating dry eyes and itchiness. Do you suffer from dry eyes? Now, you know why. Take a break.",
             7: "You know.. it's been...80 minutes since your last break? What are you doing that's so time-sensitive? Or are you just lazy?",
             8: "Here's a fact to motivate you, you poor sufferer of eye strain... \
'A large majority, nearly 70%, of Millennials report symptoms of digital eye strain.' Don't be in that 70%.",
             9: "Don't go blind. I don't want you to go blind... because that'd mean my efforts were for naught.",
             10: "Dude."
             11: "If you don't rest your eyes soon, you may start to notice: blurred vision, double vision, dry red eyes, eye irritation, \
headaches, neck or back pain...and maybe even death..",
             }     

sass_factor = 0      

while True:
    root.update()
    if tkinter.messagebox.askyesno("HEALTH", "Do you want to take a rest?"):
        root.protocol("WM_DELETE_WINDOW")
        sleep()
        time.sleep(1200)       #change sleep time to 20 min = 1200 seconds
        sass_factor = 0
    else:
        sass_factor += 1
        time.sleep(600)      #change sleep time to 10 min = 600 seconds (half the time)
        if sass_factor != 0:
            if sass_factor <= len(sass_dict):
                tkinter.messagebox.showinfo("FUN FACTS",str(sass_dict[sass_factor]))
            else:
                tkinter.messagebox.showinfo("FUN FACTS","Wow, we've run out of sass to sass you with and that says something: You REALLY need to rest your eyes...")
