'''
Created on Nov 4, 2013

@author: doolansr
'''
import c0
import new_create
import time
import tkinter
from tkinter import ttk
def main():
    pass
def gui_send(robot):
    '''they will be communicationg via morse code
    there will be 4 ir bytes
    -new letter
    -dash
    -dot
    -space'''
    '''dot = 60
    dash = 75
    pause = 65
    space = 80
    new_leter = 90

    Commands using:
    #robot.startIR(value)
    #Box_of_Fun_Toys_for_Robots.senors.ir_byte
    '''
    '''class Text():
    def __init__(self):
        self.message = None
    text=Text()'''
    root = tkinter.Tk()
    root.title("Send IR Messages")
    main_frame = ttk.Frame(root)
    main_frame.grid()
    text_entry = ttk.Entry(main_frame, width=25)
    text_entry.grid()
    robot.message = text_entry
    label = ttk.Label(main_frame, text='Enter Text to be Sent')
    label.grid()
    button1 = ttk.Button(main_frame, text='Send Text')
    button1.grid()
    button1['command'] = lambda: beam_me(robot)
def gui_receve(robot):
    root = tkinter.Tk()
    root.title("Recive IR Messages")
    main_frame = ttk.Frame(root)
    main_frame.grid()
    label = ttk.Label(main_frame, text='')
    label.grid()
    button1 = ttk.Button(main_frame, text='Receive text')
    button1.grid()
    button1['command'] = lambda: read_beam(robot, label)
def dictionarys(n):
    '''this function will be called to hand down dictionaries
    this should avoid having to hand down through 6-7 funtions'''
    dot = 'dot'  # 60
    dash = 'dash'  # 75
    pause = 'pause'  # 65 # not used yet, to single for tranmissions
    # pause moved down to sending and reciving
    space = 'space'  # 80 # in between words, not sure how to impliment yet
    new_leter = 'nL'  # 90 # need this because otherwise it mis treates single dot/dash letters
    dot_dash_list_alpha_order = [(dot, dash, new_leter), (dash, dot, dot, dot, new_leter), (dash, dot, dot, new_leter), (dot, new_leter), (dot, dot, dash, dot, new_leter), (dash, dash, dot, new_leter), \
                               (dot, dot, dot, dot, new_leter), (dot, dot, new_leter), (dot, dash, dash, dash, new_leter), (dash, dot, dash, new_leter), (dot, dash, dot, dot, new_leter), (dash, dash, new_leter), \
                               (dash, dot, new_leter), (dash, dash, dash, new_leter), (dot, dash, dash, dot, new_leter), (dash, dash, dot, dash, new_leter), (dot, dash, dot), (dot, dot, dot, new_leter), \
                               (dash, new_leter), (dot, dot, dash, new_leter), (dot, dot, dot, dash, new_leter), (dot, dash, dash, new_leter), (dash, dot, dot, dash, new_leter), \
                               (dash, dot, dash, dash, new_leter), (dash, dash, dot, dot, new_leter)]
    number_list_chrono_order = [(dash, dash, dash, dash, dash, new_leter), (dot, dash, dash, dash, new_leter), (dot, dot, dash, dash, dash, new_leter), (dot, dot, dot, dash, dash, new_leter), \
                              (dot, dot, dot, dot, dash, new_leter), (dot, dot, dot, dot, dot, new_leter), (dash, dot, dot, dot, dot, new_leter), (dash, dash, dot, dot, dot), (dash, dash, dash, dot, dot, new_leter)\
                              , (dash, dash, dash, dash, dot, new_leter)]
    s = 'a'
    morse_convert = {}  # dictionary that has code as value for letters---------key is in alpha
    alpha_convert = {}  # dictionary that has letters as value for letters, ----key is in morse
    for k in range(len(dot_dash_list_alpha_order)):
        morse_convert[s] = dot_dash_list_alpha_order[k]
        alpha_convert[dot_dash_list_alpha_order[k]] = s
        s = chr(ord(s) + 1)
    morse_convert[' '] = (space, new_leter)
    alpha_convert[(space, new_leter)] = ' '
    for k in range(len(number_list_chrono_order)):  # numbers
        morse_convert[str(k)] = number_list_chrono_order[k]
        alpha_convert[number_list_chrono_order[k]] = str(k)
#     print(convert_to_morse_code('abcd f1', morse_convert))    #tests convert to morse
#     print(convert_out_of_morse_code(convert_to_morse_code('abcd f1', morse_convert), alpha_convert)) #tests convert out of morse

    numbers_to_unit = {'60':'dot', '75':'dash', '65':'pause', '80':'space', '90':'nl'}
    unit_to_numbets = {'dot':'60', 'dash':'75', 'pause':'65', 'space':'80', 'nL':'90'}
    if n == 'alpha_convert':
        return alpha_convert
    elif n == 'morse_convert':
        return morse_convert
    elif n == 'numbers_to_unit':
        return numbers_to_unit
    elif n == 'unit_to_numbets':
        return unit_to_numbets
    else:
        pass

def convert_to_morse_code(string):
    'converts the sting to morse code'
    # verified
    sentance = []
    morse_convert = dictionarys('morse_convert')
    for k in range(len(string)):
        sentance = sentance + [morse_convert.get(string[k])]
    return sentance
def convert_out_of_morse_code(string):
    'converts the morse code to a string'
    # verified
    alpha_convert = dictionarys('alpha_convert')
    sentance = ''
    for k in range(len(string)):
        sentance = sentance + str(alpha_convert.get(string[k]))
    return sentance
def convert_to_beam(message):
    'converts morse code into a list of numbers to be beamed'
    # not tested
    string = convert_to_morse_code(message)
    beam = []
    for k in range(len(string)):
        for j in range(len(string[k])):
            if string[k][j] == 'dot':
                beam.append(60);
                beam.append(65);
            if string[k][j] == 'dash':
                beam.append(75);
                beam.append(65);
            if string[k][j] == 'space':
                beam.append(80);
                beam.append(65);
            if string[k][j] == 'nL':
                beam.append(90);
                beam.append(65);


    return beam
def beam_me(robot):
    'beams the the list of numbers with a .3 second pause'
    # tested 11/11/2013
    beam = convert_to_beam(robot.message.get());
    prev_p = 255
    sensor = new_create.Sensors.ir_byte
    receive = robot.robot.getSensor(sensor)
    print(beam)
    for k in range(len(beam)):

        robot.robot.startIR(beam[k])
        print('onward', beam[k])
        while True:
            time.sleep(.05)
            p = robot.robot.getSensor(sensor)
            if p == 255:
                continue
            if p == beam[k]:
                continue
            if p == prev_p:
                continue

        prev_p = p
        print(prev_p)
#         time.sleep(.05)
    robot.robot.startIR(250)

def read_beam(robot, label):
    'reads the beam and returns numbers'
#     for _ in range(100):
#         sensor = new_create.Sensors.ir_byte
#         receive = robot.robot.getSensor(sensor)
#         print(receive)
#         time.sleep(.3)
    n = 0
    beam_read = []
    prev_rec = 255
    p = 0
    message = ''
    sensor = new_create.Sensors.ir_byte

#     print('i got', receive)

    while  True:
        time.sleep(1.5)
        receive = robot.robot.getSensor(sensor)
        if receive == 100:
            continue
        if receive == 105:
            continue
        if receive == 255:
            continue
        if receive == prev_rec:
            continue
        print('i got', receive)
        beam_read.append(str(receive))
        prev_rec = receive
#         print(receive)
        if p == 100:
            p = 105
        else:
            p = 100
        robot.robot.startIR(p)
        if receive == 250:
            break

#             if n == 65:
#                 if p == 100:  # framework to send response back if hears beam
#                     p = 105
#                 else:
#                     p = 100
#
#             elif n == 90:  # 'nL'
#                 beam_read.append(n)
#                 print(beam_to_letter(beam_read), end='')  # if using same robot, will recive error
#                 # robot sending byte message will interfere
#                 message = message + str(beam_to_letter(beam_read))
#                 label['text'] = message
#                 beam = []
#                 if p == 100:  # framework to send response back if hears beam
#                     p = 105
#                 else:
#                     p = 100
#             elif n != 250:
#                 beam_read.append(n)
#                 if p == 100:  # framework to send response back if hears beam
#                     p = 105
#                 else:
#                     p = 100
#             else:
#                 break
#         if p == 100:  # framework to send response back if hears beam
#             p = 105
#         else:
#             p = 100


def beam_to_letter(beam):
    tuple1 = []
    numbers_to_unit = dictionarys('numbers_to_unit')
    alpha_convert = dictionarys('alpha_convert')
    for k in range(beam):
        tuple1.append(numbers_to_unit[beam[k]])
    return convert_out_of_morse_code(tuple(tuple1), alpha_convert)


if __name__ == '__main__':
    main()
