from random import randint
from time import localtime, struct_time, sleep
from escpos.printer import File
from genimg import get_weird_timestamp
import json
import os.path
from gpiozero import Button

button = Button(26)

counter_file = 'counter.json'

p = File('/dev/usb/lp0')

counter = 0

if not os.path.exists(counter_file):
    with open(counter_file, 'w') as f:
        json.dump(0, f)


def update_counter():
    global counter
    with open(counter_file, "r") as f:
        counter = json.load(f)
        counter += 1
        print(f'counter is now {counter}')
    with open(counter_file, "w") as f:
        json.dump(counter, f)


WAS_IT = ['Was it', 'Wasn\'t it', 'It feels\nit was',
          'It smells\nit was', 'It sounds\nit was', 'It feels\nit was']
HOURS = ['midnight', 'midnight', 'latenight', 'afternight', 'beforemorning', 'earlymorning', 'midmorning', 'midmorning', 'latemorning', 'aftermorning', 'beforenoon', 'earlynoon',
         'midnoon', 'midnoon', 'latenoon', 'afternoon', 'beforeevening', 'earlyevening', 'midevening', 'midevening', 'lateevening', 'afterevening', 'beforenight', 'earlynight']
ALMOST = ['almost', '']
LATELY = ['', 'recently', 'lately', 'earlier', 'long ago']
QUESTION = ['.', '?']

MAYBE = ['maybe', 'possibly', 'perhaps', 'probably',
         'presumably', 'assumably', 'supposable']
WILL_IT_BE = ['Will it be', 'it will be']
LIKE_AS = ['', 'like', 'as']
HEREAFTER = ['hereafter', 'later on', 'later',
             'in a while', 'in a little\nwhile', 'shortly', 'soon']

IT_COULD_BE = ['Is it', 'Isn\'t it',
               'Couldn\'t it be', 'It might be', 'It could be']
END = ['end', 'beginning']
SOMEHOW = ['somehow', 'maybe', 'sometime', 'about', 'around']
BY_NOW = ['by now', 'already', 'now', 'currently']


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def print_poem():
    update_counter()
    hour = struct_time(localtime())[3]
    minute = struct_time(localtime())[4]
    poem = []

    indexWas = randint(0, len(WAS_IT) - 1)
    if indexWas < 2:
        is_question = True
    else:
        is_question = False
    poem.append([WAS_IT[indexWas],
                 HOURS[(hour - 3) % 24],
                 ALMOST[randint(0, len(ALMOST) - 1)],
                 LATELY[translate(minute, 0, 59, 0, 4)],
                 QUESTION[is_question]])  # + 3 hours

    indexWill = randint(0, len(WILL_IT_BE) - 1)
    poem2_is_question = False if indexWill == 0 else True
    may_be = ''
    if poem2_is_question:
        may_be = MAYBE[randint(0, len(MAYBE) - 1)]

    poem.append([may_be, WILL_IT_BE[indexWill], LIKE_AS[randint(0, 2)],
                 HOURS[(hour + 2) % 24],
                 HEREAFTER[translate(minute, 0, 59, 0, 6)],
                 QUESTION[not poem2_is_question]])  # -2 hours

    could_be_index = randint(0, 4)
    poem3_is_question = True if could_be_index < 3 else False

    poem.append([IT_COULD_BE[could_be_index],
                 END[0 if minute < 30 else 1],
                 HOURS[hour],
                 SOMEHOW[randint(0, 4)],
                 BY_NOW[randint(0, 3)],
                 QUESTION[poem3_is_question]])

    # PRINT POEM
    p.set(font='a', align='center', width=4, height=4)

    p.text('\n')
    for line in poem:
        p.set(font='a', align='center', width=3, height=3)
        print(line)
        lineStr = ''
        for item in line:
            if item != '':
                if item in '.?':
                    lineStr += item
                else:
                    lineStr += '\n' + item if lineStr != '' else '' + item
        p.text(lineStr.upper())
        p.set(font='a', align='center', width=3, height=3)
        p.text('\n\n\n')

    p.text('\n')
    p.cut()

    # return poem


def print_footer():
    count_str = f'{counter:04}'
    p.set(font='b', align='center')
    p.text(
        f'receipt for the current moment{count_str.rjust(21," ")}\n'.upper())
    p.text(f'literaturmuseum der moderne{"marbach".rjust(24, " ")}\n'.upper())


while True:
    print('--- waiting for button press ---')
    button.wait_for_press()
    print('button pressed')
    button.wait_for_release()
    print('released')
    print_poem()
    sleep(10)
