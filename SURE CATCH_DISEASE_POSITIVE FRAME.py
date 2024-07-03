'''
CODE FOR INSTALLING NECESSARY PACKAGES TO RUN THIS SCRIPT

import os

os.system('python -m pip install scipy')
os.system('python -m pip install pandas')
os.system('python -m pip install openpyxl')
'''

'''
IMPORTED BUILT-IN PACKAGES/MODULES
'''

import turtle
import tkinter as tk
import turtle
import time
import timeit
import threading
import sys

import pandas as pd

from turtle import Screen, Turtle
from time import *
from tkinter import *
from tkinter import font as tkFont
from random import choice

from tkinter import Tk
from tkinter.ttk import Button







'''
ALL GLOBAL VARIABLES
'''
# Conditional to be met for breaking for loop in threaded timer();
# becomes true after the last question is asked after 3 of the same choice answers in a row
end = False


cd_timeline = []
real_timeline = []

# All countdown times for all responses true or false
all_cd = ''
all_cds = []
# All realtime responses calculated as (36000 - all_cds[-1])*0.1
all_rt = ''
all_rts = []

# Single Variable for Participant ID
ID = ''
id_cd = ''
id_cds = []
id_rt = ''
id_rts = []

# CD for "countdown" response time for True choices (made in 6 sec or less)
true_choice_cd = ''
true_choice_cds = []
true_choice_rt = ''
true_choice_rts = []

# CD response times for false choices
false_choice_cd = ''
false_choice_cds = []
# false_choice_timer() subtracts false_choice_time from last recorded time in all_rts
false_choice_rt = ''
false_choice_rts = []

# should only end with list of 16 elements
true_game_trial_cd = ''
true_game_trial_cds = []
true_game_trial_rt = ''
true_game_trial_rts = []

# number of these trials depends on participant task adherence
false_game_trial_cd = ''
false_game_trial_cds = []
false_game_trial_rt = ''
false_game_trial_rts = []

# should only end with list of 4 elements
true_catch_trial_cd = ''
true_catch_trial_cds = []
true_catch_trial_rt = ''
true_catch_trial_rts = []

# number of these trials depends on participant task adherence
false_catch_trial_cd = ''
false_catch_trial_cds = []
false_catch_trial_rt = ''
false_catch_trial_rts = []

true_catch_gamble_weighted_cd = ''
true_catch_gamble_weighted_cds = []
true_catch_gamble_weighted_rt = ''
true_catch_gamble_weighted_rts = []

false_catch_gamble_weighted_cd = ''
false_catch_gamble_weighted_cds = []
false_catch_gamble_weighted_rt = ''
false_catch_gamble_weighted_rts = []

true_catch_sure_weighted_cd = ''
true_catch_sure_weighted_cds = []
true_catch_sure_weighted_rt = ''
true_catch_sure_weighted_rts = []

false_catch_sure_weighted_cd = ''
false_catch_sure_weighted_cds = []
false_catch_sure_weighted_rt = ''
false_catch_sure_weighted_rts = []

recall_loop_cd = ''
recall_loop_cds = []
recall_loop_rt = ''
recall_loop_rts = []

Q1_cd = ''
Q1_cds = []
Q1_rt = ''
Q1_rts = []

true_recall_choices_cd = ''
true_recall_choices_cds = []
true_recall_choices_rt = ''
true_recall_choices_rts = []

false_recall_choices_cd = ''
false_recall_choices_cds = []
false_recall_choices_rt = ''
false_recall_choices_rts = []


# time taken to make choice
time2choice = ''
time2choices = []



# All choices
all_choice = ''
all_choices = []

# Choices made in 6 sec or less
true_choice = ''
true_choices = []

# Choices made after 6 sec
false_choice = ''
false_choices = []

# On time choices made during game trials; should end up with 16 elements in list
true_game_trial_choice = ''
true_game_trial_choices = []

# Late choices made during game trials
false_game_trial_choice = ''
false_game_trial_choices = []

# Choices made during catch trials (which have oppositely weighted options); should end up with 4 elements in list
true_catch_trial_choice = ''
true_catch_trial_choices = []

# Late choices made during catch trials (which have oppositely weighted options)
false_catch_trial_choice = ''
false_catch_trial_choices = []

recall_choice = ''
recall_choices = []
true_recall_choice = ''
true_recall_choices = []
false_recall_choice = ''
false_recall_choices = []

total_trial_count = 0
game_trial_count = 0
catch_trial_count = 0
catch_sure_weighted_trial_count = 0
catch_gamble_weighted_trial_count = 0

# All true trials (should be 20 by the end)
true_trial_count = 0

false_trial_count = 0

# All True game trials (choices made in <= 6 sec)
true_game_trial_count = 0

# All False game trials (choices made after 6 sec)
false_game_trial_count = 0

# All True catch trials (choices made in <= 6 sec)
true_catch_trial_count = 0

# All False catch trials (choices made after 6 sec)
false_catch_trial_count = 0
true_catch_gamble_weighted_trial_count = 0
true_catch_sure_weighted_trial_count = 0
false_catch_gamble_weighted_trial_count = 0
false_catch_sure_weighted_trial_count = 0
recall_trial_count = 0
true_recall_trial_count = 0
false_recall_trial_count = 0
true_consec_trial_count = 0

# Set to True or False in choice_timer()
true_trial = ''
false_trial = ''

recall_true_trial = ''
recall_false_trial = ''

recall_time2choice = ''
recall_time2choices = []
Qs_time2choice = ''
Qs_time2choices = []


Q1_answer = ''
Q1_answers = []

Q2_answer = ''
Q2_answers = []

Q3_answer = ''
Q3_answers = []

Q4_answer = ''
Q4_answers = []

Q5_answer = ''
Q5_answers = []


events = []

trial_types = []


dataframe = {}


'''
DATA FILE CREATION
'''

def pad_data(data, padel):
    global dataframe
    dataframe = {
        'CD Timeline':cd_timeline,
        'Real Timeline': real_timeline,
        'Event (VE = Vignette End, CC = Choice Click)':events,
        'CD (ds)':all_cds,
        'RT (ds)':all_rts,
        'Recall Loop RT':recall_loop_rts,
        'Trial Type (0 = Game, 1 = Catch, 2 =  Game Loop, 3 = Recall Question)':trial_types,
        'Choice/Response':all_choices,
        'Time to Choice':time2choices,
        'True Trial Choice RT':true_choice_rts,
        'False Trial Choice RT':false_choice_rts,
        }
    
    lmax = 0
    for lname in dataframe.keys():
        lmax = max(lmax, len(dataframe[lname]))
    for lname in dataframe.keys():
        ll = len(dataframe[lname])
        if  ll < lmax:
            dataframe[lname] += [padel] * (lmax - ll)
    return dataframe
    


def create_excel():

    for i in range(0, (len(all_rts) - len(recall_loop_rts))):
        recall_loop_rts.insert(0, '')
    
    pad_data(dataframe, '')
    
    df = pd.DataFrame.from_dict(dataframe)
    
    df.to_excel('Participant ' + ID + ' Choice Data' + '.xlsx', header=True, index=False)

    #sys.exit()


def create_data_file():

    
    
    f = open('Participant ' + ID + ' Choice Data' + '.txt', "w+")
    f.write('DISEASE Vignette; POSITIVE Frame; SURE Weighted Catch Trials' + '\n')
    f.write('Participant: ' + ID + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

    f.write('CD Timeline: ' + str(cd_timeline) + '\n')
    f.write('\n')
    f.write('Length of cd_timeline List: ' + str(len(cd_timeline)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('Real Timeline: ' + str(real_timeline) + '\n')
    f.write('\n')
    f.write('Length of real_timeline List: ' + str(len(real_timeline)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

    f.write('Total Trials Count: ' + str(total_trial_count) + '\n')
    f.write('Total True Trials Count: ' + str(true_trial_count) + '\n')
    f.write('Total False Trials Count: ' + str(false_trial_count) + '\n')
    f.write('\n')
    f.write('\n')

    f.write('Recorded Events: ' + str([item for item in events if item != '']) + '\n')
    f.write('Length of events List: ' + str(len([item for item in events if item != ''])) + '\n')
    f.write('\n')
    f.write('\n')

    f.write('All Countdown Response/Event Times: ' + str([item for item in all_cds if item != '']) + '\n')
    f.write('Length of all_cds List: ' + str(len([item for item in all_cds if item != ''])) + '\n')
    f.write('\n')
    f.write('\n')
    
    f.write('All Real Time Response/Event Times: ' + str([item for item in all_rts if item != '']) + '\n')
    f.write('Length of all_rts List: ' + str(len([item for item in all_rts if item != ''])) + '\n')
    f.write('\n')
    f.write('\n')
    
    f.write("All Choices/Responses: " + str([item for item in all_choices if item != '']) + '\n')
    f.write('Length of all_choices List: ' + str(len([item for item in all_choices if item != ''])) + '\n')
    f.write('\n')
    
    f.write('Times to Choice/Response: ' + str([item for item in time2choices if item != '']) + '\n')
    f.write('Length of time2choices List: ' + str(len([item for item in time2choices if item != ''])) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

    f.write('Trial Types: ' + str([item for item in trial_types if item != '']) + '\n')
    f.write('Length of trial_types List: ' + str(len([item for item in trial_types if item != ''])) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

    f.write('True Trial Choices/Responses: ' + str(true_choices) + '\n')
    f.write('Length of true_choices List: ' + str(len(true_choices)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('True Trial Response Times: ' + str(true_choice_rts) + '\n')
    f.write('Length of true_choice_rts List: ' + str(len(true_choice_rts)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

    f.write('False Trial Choices/Responses: ' + str(false_choices) + '\n')
    f.write('Length of true_choices List: ' + str(len(false_choices)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('False Trial Response Times: ' + str(false_choice_rts) + '\n')
    f.write('Length of False Choice Response Times List: ' + str(len(false_choice_rts)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    
    
    f.write('Total Game Trial Count: ' + str(game_trial_count) + '\n')
    f.write('\n')
    f.write('True Game Trial Count: ' + str(true_game_trial_count) + '\n')
    f.write('True Game Trial Choices: ' + str(true_game_trial_choices) + '\n')
    f.write('Length of true_game_trial_choices List: ' + str(len(true_game_trial_choices)) + '\n')
    f.write('\n')
    f.write('True Game Trial Response Times: ' + str(true_game_trial_rts) + '\n')
    f.write('Length of true_game_trial_rts List: ' + str(len(true_game_trial_rts)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('False Game Trial Count: ' + str(false_game_trial_count) + '\n')
    f.write('False Game Trial Choices: ' + str(false_game_trial_choices) + '\n')
    f.write('Length of false_game_trial_choices List: ' + str(len(false_game_trial_choices)) + '\n')
    f.write('\n')
    f.write('False Game Trial Response Times: ' + str(false_game_trial_rts) + '\n')
    f.write('Length of false_game_trial_rts List: ' + str(len(false_game_trial_rts)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    
    f.write('Total Catch Trial Count: ' + str(catch_trial_count) + '\n')
    f.write('\n')
    f.write('True Catch Trial Count: ' + str(true_catch_trial_count) + '\n')
    f.write('True Catch Trial Choices: ' + str(true_catch_trial_choices) + '\n')
    f.write('Length of true_catch_trial_choices List: ' + str(len(true_catch_trial_choices)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('True Catch Trial Response Times: ' + str(true_catch_trial_rts) + '\n')
    f.write('Length of true_catch_trial_rts List: ' + str(len(true_catch_trial_rts)) + '\n')
    f.write('\n')
    f.write('\n')
    
    f.write('False Catch Trial Count: ' + str(false_catch_trial_count) + '\n')
    f.write('False Catch Trial Choices: ' + str(false_catch_trial_choices) + '\n')
    f.write('Length of false_catch_trial_choices List: ' + str(len(false_catch_trial_choices)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('False Catch Trial Response Times: ' + str(false_catch_trial_rts) + '\n')
    f.write('Length of false_catch_trial_rts List: ' + str(len(false_catch_trial_rts)) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')



    
    f.write('Total Sure Weighted Catch Trial Count: ' + str(catch_sure_weighted_trial_count) + '\n')
    f.write('True Sure Weighted Catch Trial Count: ' + str(true_catch_sure_weighted_trial_count) + '\n')
    f.write('False Sure Weighted Catch Trial Count: ' + str(false_catch_sure_weighted_trial_count) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')
    
    f.write('Total Gamble Weighted Catch Trial Count: ' + str(catch_gamble_weighted_trial_count) + '\n')
    f.write('True Gamble Weighted Catch Trial Count: ' + str(true_catch_gamble_weighted_trial_count) + '\n')
    f.write('False Gamble Weighted Catch Trial Count: ' + str(false_catch_gamble_weighted_trial_count) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')


    f.write('Recall Loop Vignette Trial Count: ' + str(recall_trial_count) + '\n')
    f.write('\n')
    f.write('Recall Loop Vignette Choices: ' + str(recall_choices) + '\n')    
    f.write('\n')

    f.write('All Recall Loop Response Times (vignette ends, choice clicks, recall question responses): ' + str(recall_loop_rts) + '\n')
    f.write('\n')
    f.write('\n')
    f.write('\n')

    f.write('True Recall Loop Vignette Trial Count: ' + str(true_recall_trial_count) + '\n')
    f.write('True Recall Loop Vignette Choices: ' + str(true_recall_choices) + '\n')
    f.write('\n')

    f.write('False Recall Loop Vignette Trial Count: ' + str(false_recall_trial_count) + '\n')
    f.write('False Recall Loop Vignette Choices: ' + str(false_recall_choices) + '\n')
    f.write('\n')
    f.write('\n')
    
    f.write('Recall Trials time2choices (Vignette & Question Responses): ' + str(recall_time2choices) + '\n')
    f.write('Length of recall_time2choices List: ' + str(len(recall_time2choices)) + '\n')
    f.write('\n')
    f.write('\n')
    
    f.write ("Q1 Responses: " + str(Q1_answers) + '\n')
    f.write ("Q2 Responses: " + str(Q2_answers) + '\n')
    f.write ("Q3 Responses: " + str(Q3_answers) + '\n')
    f.write ("Q4 Responses: " + str(Q4_answers) + '\n')
    f.write ("Q5 Responses: " + str(Q5_answers) + '\n')

    f.close
    create_excel()
    return



# TIMER FUNCTION RUNNING IN BACKGROUND
def timer():
    # Set time 0, countdown from 36000 in 0.1 sec increments
    global my_timer
    global trial_cd_time
    global true_choice_rt
    global true_choice_rts
    global true_choice_rt
    global true_choice_rts
    global realtime
    global end
    
    # Timer set in sec
    my_timer = 36000

    for x in range(36000):
        my_timer -= (timeit.timeit('time.sleep(0.1)', number=1))*10
        #sleep(0.1)
        print(my_timer)
        cd_timeline.append(my_timer)
        real_timeline.append((36000 - my_timer)*0.1)
        if end:
            break
    return



'''
TRIAL DECIDER
'''

def rand_vignette():
    global fns
    choice(fns)()
    return

# CALL TRIAL TYPE AFTER TRUE CHOICES ACCORDING TO HOW MANY OF EACH TRIAL HAS BEEN COMPLETED
def trial_decider():
    global all_choice
    global catch_trial_count
    global true_game_trial_count
    global true_catch_sure_weighted_trial_count
    global true_catch_gamble_weighted_trial_count

    global false_game_trial_count
    global false_catch_sure_weighted_trial_count
    global false_catch_gamble_weighted_trial_count

    global true_trial
    global false_trial

    if true_game_trial_count < 8 and true_catch_trial_count == 0 or true_game_trial_count < 16 and true_catch_trial_count == 4:
        game_disease_vignette()
        print('called game_disease_vignette()')
        
    elif true_game_trial_count >= 8 and true_game_trial_count < 16 and true_catch_trial_count < 4:
        rand_vignette()
        print('called rand_vignette()')
        
    elif true_game_trial_count == 16 and true_catch_trial_count < 4:
        catch_disease_vignette()
        print('called catch_disease_vignette()')
        
    elif true_game_trial_count == 16 and true_catch_trial_count == 4:
        print('FINISHED FRAMING TASK. BEGINNING RECALL LOOP')
        recall_loop()

    return




'''
CDS RTS
'''

# all_cds_rts() called after every choice response regardless of 6 sec timer parameter
def all_cds_rts():
    global all_cd
    global all_cds
    global all_cd
    global all_rt
    global all_rts
    
    all_cd = my_timer
    all_cds.append(all_cd)
    
    all_rts.append((36000 - all_cds[-1])*0.1)
    return


def get_recall_loop_cds_rts():
    global recall_loop_cd
    global recall_loop_cds
    global recall_loop_rt
    global recall_loop_rts

    recall_loop_cd = my_timer
    recall_loop_cds.append(recall_loop_cd)

    recall_loop_rt = (36000 - recall_loop_cds[-1])*0.1
    recall_loop_rts.append(recall_loop_rt)


def Q1_cds_rts():
    global Q1_cd
    global Q1_cds
    global Q1_rt
    global Q1_rts

    Q1_cd = my_timer
    Q1_cds.append(Q1_cd)

    Q1_rt = (36000 - Q1_cds[-1])*0.1
    Q1_rts.append(Q1_rt)


# Called on every true choice trial (choice made in <= 6 sec)
def true_choice_cds_rts():
    global true_choice_cd
    global true_choice_cds
    global true_choice_rt
    global true_choice_rts
    global all_cds
    
    true_choice_cd = my_timer
    true_choice_cds.append(true_choice_cd)
    
    true_choice_rt = (36000 - all_cds[-1])*0.1
    true_choice_rts.append(true_choice_rt)
    return
    

# Called on every trial (choice made after 6 sec)
def false_choice_cds_rts():
    global false_choice_cd
    global false_choice_cds
    global false_choice_rt
    global false_choice_rts
    global all_cds

    false_choice_cd = my_timer
    false_choice_cds.append(false_choice_cd)

    false_choice_rt = (36000 - all_cds[-1])*0.1
    false_choice_rts.append(false_choice_rt)
    return

# Called on every true game trial (choice made in <= 6 sec)
def true_game_trial_cds_rts():
    global true_game_trial_cd
    global true_game_trial_cds
    global true_game_trial_rt
    global true_game_trial_rts
    global all_cds

    true_game_trial_cd = my_timer
    true_game_trial_cds.append(true_game_trial_cd)

    true_game_trial_rt = (36000 - all_cds[-1])*0.1
    true_game_trial_rts.append(true_game_trial_rt)
    return


# Called on every false game trial (choice made after 6 sec)
def false_game_trial_cds_rts():
    global false_game_trial_cd
    global false_game_trial_cds
    global false_game_trial_rt
    global false_game_trial_rts
    global all_cds

    false_game_trial_cd = my_timer
    false_game_trial_cds.append(false_game_trial_cd)

    false_game_trial_rt = (36000 - all_cds[-1])*0.1
    false_game_trial_rts.append(false_game_trial_rt)
    return


# Called on every true catch trial (choice made in <= 6 sec)
def true_catch_trial_cds_rts():
    global true_catch_trial_cd
    global true_catch_trial_cds
    global true_catch_trial_rt
    global true_catch_trial_rts
    global all_cds

    true_catch_trial_cd = my_timer
    true_catch_trial_cds.append(true_catch_trial_cd)

    true_catch_trial_rt = (36000 - all_cds[-1])*0.1
    true_catch_trial_rts.append(true_catch_trial_rt)
    return


# Called on every false catch trial (choice made after 6 sec)
def false_catch_trial_cds_rts():
    global false_catch_trial_cd
    global false_catch_trial_cds
    global false_catch_trial_rt
    global false_catch_trial_rts
    global all_cds

    false_catch_trial_cd = my_timer
    false_catch_trial_cds.append(false_catch_trial_cd)

    false_catch_trial_rt = (36000 - all_cds[-1])*0.1
    false_catch_trial_rts.append(false_catch_trial_rt)
    return


'''
def true_catch_gamble_weighted_cds_rts():
    global true_catch_gamble_weighted_cd
    global true_catch_gamble_weighted_cds
    global true_catch_gamble_weighted_rt
    global true_catch_gamble_weighted_rts
    global all_cds

    true_catch_gamble_weighted_cd = my_timer
    true_catch_gamble_weighted_cds.append(true_catch_gamble_weighted_cd)

    true_catch_gamble_weighted_rt = (36000 - all_cds[-1])*0.1
    true_catch_gamble_weighted_rts.append(true_catch_gamble_weighted_rt)
    return


def false_catch_gamble_weighted_cds_rts():
    global false_catch_gamble_weighted_cd
    global false_catch_gamble_weighted_cds
    global false_catch_gamble_weighted_rt
    global false_catch_gamble_weighted_rts
    global all_cds

    false_catch_gamble_weighted_cd = my_timer
    false_catch_gamble_weighted_cds.append(false_catch_gamble_weighted_cd)

    false_catch_gamble_weighted_rt = (36000 - all_cds[-1])*0.1
    false_catch_gamble_weighted_rts.append(false_catch_gamble_weighted_rt)
    return
'''


def true_catch_sure_weighted_cds_rts():
    global true_catch_sure_weighted_cd
    global true_catch_sure_weighted_cds
    global true_catch_sure_weighted_rt
    global true_catch_sure_weighted_rts
    global all_cds

    true_catch_sure_weighted_cd = my_timer
    true_catch_sure_weighted_cds.append(true_catch_sure_weighted_cd)

    true_catch_sure_weighted_rt = (36000 - all_cds[-1])*0.1
    true_catch_sure_weighted_rts.append(true_catch_sure_weighted_rt)
    return


def false_catch_sure_weighted_cds_rts():
    global false_catch_sure_weighted_cd
    global false_catch_sure_weighted_cds
    global false_catch_sure_weighted_rt
    global false_catch_sure_weighted_rts
    global all_cds

    false_catch_sure_weighted_cd = my_timer
    false_catch_sure_weighted_cds.append(false_catch_sure_weighted_cd)

    false_catch_sure_weighted_rt = (36000 - all_cds[-1])*0.1
    false_catch_sure_weighted_rts.append(false_catch_sure_weighted_rt)
    return



def true_recall_choice_cds_rts():
    global true_recall_choices_cd
    global true_recall_choices_cds
    global true_recall_choices_rt
    global true_recall_choices_rts

    true_recall_choices_cd = my_timer
    true_recall_choices_cds.append(true_recall_choices_cd)

    true_recall_choices_rt = (36000 - true_recall_choices_cds[-1])*0.1
    true_recall_choices_rts.append(true_recall_choices_rt)


def false_recall_choice_cds_rts():
    global false_recall_choices_cd
    global false_recall_choices_cds
    global false_recall_choices_rt
    global false_recall_choices_rts

    false_recall_choices_cd = my_timer
    false_recall_choices_cds.append(false_recall_choices_cd)

    false_recall_choices_rt = (36000 - false_recall_choices_cds[-1])*0.1
    false_recall_choices_rts.append(false_recall_choices_rt)





'''
CHOICE TIMERS
'''

def recall_choice_timer():
    global recall_time2choices
    global recall_true_trial
    global recall_false_trial

    time_limit = 10

    if recall_time2choices[-1] < time_limit:
        recall_true_trial = True
        return True
    if recall_time2choices[-1] > time_limit:
        recall_false_trial = True
        return False
    return

        

# 6 sec Response_timer = countdown time of last response - current countdown time; returns True or False
def choice_timer():
    global time2choices
    global true_trial
    global false_trial

    time_limit = 10

    if time2choices[-1] < time_limit:
        true_trial = True
        return True
    if time2choices[-1] > time_limit:
        false_trial = True
        return False
    return



'''
TIME TO CHOICES FUNCTIONS
'''

def time2choices_append():
    global time2choice
    global time2choices
    global all_rts
    time2choice = all_rts[-1] - all_rts[-2]
    time2choices.append(time2choice)
    return

def recall_time2choices_append():
    global recall_time2choice
    global recall_time2choices
    global all_rts
    recall_time2choice = all_rts[-1] - all_rts[-2]
    recall_time2choices.append(recall_time2choice)
    return

def Qs_time2choices_append():
    global Qs_time2choice
    global Qs_time2choices
    global all_rts
    Qs_time2choice = all_rts[-1] - all_rts[-2]
    Qs_time2choices.append(Qs_time2choice)
    return





'''
APPENDING FUNCTIONS
'''

def recall_choices_append(ab):
    global recall_choice
    global recall_choices
    recall_choices.append(ab)

def true_recall_choices_append(ab):
    global true_recall_choice
    global true_recall_choices
    true_recall_choices.append(ab)

def false_recall_choices_append(ab):
    global false_recall_choice
    global false_recall_choices
    false_recall_choices.append(ab)

def true_choices_append(ab):
    global true_choice
    global true_choices
    true_choices.append(ab)
    return

def false_choices_append(ab):
    global false_choice
    global false_choices
    false_choices.append(ab)
    return

def true_game_trial_choices_append(ab):
    global true_game_trial_choice
    global true_game_trial_choices
    true_game_trial_choices.append(ab)
    return

def false_game_trial_choices_append(ab):
    global false_game_trial_choice
    global false_game_trial_choices
    false_game_trial_choices.append(ab)
    return

def true_catch_trial_choices_append(ab):
    global true_catch_trial_choice
    global true_catch_trial_choices
    true_catch_trial_choices.append(ab)
    return

def false_catch_trial_choices_append(ab):
    global false_catch_trial_choice
    global false_catch_trial_choices
    false_catch_trial_choices.append(ab)
    return




'''
TRUE CONSECUTIVE TRIAL COUNTER & RECALL CONSECUTIVE CHOICE CHECKER
'''

def three_consec_true_choices():
    global true_consec_trial_count
    global recall_true_trial
    global recall_false_trial
    global all_choice

    if recall_choice_timer() and true_consec_trial_count == 0:
        true_consec_trial_count += 1
        
    elif recall_choice_timer() and all_choice == recall_choices[-1] and true_consec_trial_count < 3:
        true_consec_trial_count += 1

    if recall_choice_timer() == False:
        true_consec_trial_count = 0


def choice_checker():
    global end
    global true_recall_trial_count
    global true_recall_choices
    global recall_choices
    global true_consec_trial_count

        
    if str(true_recall_choices[-3:]) == "['A', 'A', 'A']" and true_consec_trial_count == 3 or str(true_recall_choices[-3:]) == "['B', 'B', 'B']" and true_consec_trial_count == 3:
        end = True
        turtle.clearscreen()
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('You have completed the task.', font=style, align='center')
        turtle.hideturtle()
        create_data_file()
        #os.system('venv\Scripts\deactivate')
    else:
        recall_loop()
    return







'''
RECALL QUESTIONS
'''

def question5(choice):
    global Q5_answer
    global Q5_answers
    global total_trial_count
    global events
    global trial_types
    global all_choices
    global time2choices

    Q_num = str(5)

    total_trial_count += 1
    
    if choice == 'A':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
If you had chosen medicine B instead, what would be the \n\
percent chance of no one being saved?', font=style, align='center')
        turtle.hideturtle()
    elif choice == 'B':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
If you had chosen medicine A instead, how many people \n\
would not have been saved?', font=style, align='center')
        turtle.hideturtle()
        
    while not Q5_answer:
        Q5_answer = turtle.textinput('Input', 'Response:')
        
    if Q5_answer:
        all_cds_rts()
        events.append('Recall Question ' + Q_num)
        trial_types.append(3)
        trial_types.append('')
        get_recall_loop_cds_rts()
        Qs_time2choices_append()
        time2choices.append(all_rts[-1] - all_rts[-2])
        recall_time2choices_append()
        all_choices.append(Q5_answer)
        Q5_answers.append(Q5_answer)
        Q5_answer = ''
        
    turtle.clear()
    choice_checker()
    return

def question4(choice):
    global Q4_answer
    global Q4_answers
    global total_trial_count
    global events
    global trial_types
    global all_choices
    global recall_choices
    global time2choices

    Q_num = str(4)

    total_trial_count += 1
    
    if choice == 'A':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
If you had chosen medicine B instead, what would be the \n\
percent chance of everyone being saved?', font=style, align='center')
        turtle.hideturtle()
    elif choice == 'B':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
If you had chosen medicine A instead, how many people \n\
would have been saved?', font=style, align='center')
        turtle.hideturtle()
    while not Q4_answer:
        Q4_answer = turtle.textinput('Input', 'Response:')

    if Q4_answer:
        all_cds_rts()
        events.append('Recall Question ' + Q_num)
        trial_types.append(3)
        get_recall_loop_cds_rts()
        Qs_time2choices_append()
        time2choices.append(all_rts[-1] - all_rts[-2])
        recall_time2choices_append()
        all_choices.append(Q4_answer)
        Q4_answers.append(Q4_answer)
        Q4_answer = ''
        
    turtle.clear()
    question5(recall_choices[-1])
    return

def question3(choice):
    global Q3_answer
    global Q3_answers
    global total_trial_count
    global events
    global trial_types
    global all_choices
    global recall_choices
    global time2choices

    Q_num = str(3)
    
    total_trial_count += 1
    
    if choice == 'A':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
Based on the medicine you chose, how many people will not be saved?', font=style, align='center')
        turtle.hideturtle()
    elif choice == 'B':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
Based on the medicine you chose, what is the \n\
percent chance that no one will be saved?', font=style, align='center')
        turtle.hideturtle()
        
    while not Q3_answer:
        Q3_answer = turtle.textinput('Input', 'Response:')

    if Q3_answer:
        all_cds_rts()
        events.append('Recall Question ' + Q_num)
        trial_types.append(3)
        get_recall_loop_cds_rts()
        Qs_time2choices_append()
        time2choices.append(all_rts[-1] - all_rts[-2])
        recall_time2choices_append()
        all_choices.append(Q3_answer)
        Q3_answers.append(Q3_answer)
        Q3_answer = ''
        
    turtle.clear()
    question4(recall_choices[-1])

    return

def question2(choice):
    global Q2_answer
    global Q2_answers
    global total_trial_count
    global events
    global trial_types
    global all_choices
    global recall_choices
    global time2choices

    Q_num = str(2)


    total_trial_count += 1
    
    if choice == 'A':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
Based on the medicine you chose, how many people will be saved?', font=style, align='center')
        turtle.hideturtle()
    elif choice == 'B':
        turtle.color('black')
        style = ('Arial', 20, 'bold')
        turtle.write('\
Based on the medicine you chose, what is the \n\
percent chance that everyone will be saved?', font=style, align='center')
        turtle.hideturtle()
        
    while not Q2_answer:
        Q2_answer = turtle.textinput('Input', 'Response:')

    if Q2_answer:
        all_cds_rts()
        events.append('Recall Question ' + Q_num)
        trial_types.append(3)
        get_recall_loop_cds_rts()
        Qs_time2choices_append()
        time2choices.append(all_rts[-1] - all_rts[-2])
        recall_time2choices_append()
        all_choices.append(Q2_answer)
        Q2_answers.append(Q2_answer)
        Q2_answer = ''

    turtle.clear()
    question3(recall_choices[-1])
    return

def question1():
    global Q1_answer
    global Q1_answers
    global total_trial_count
    global events
    global trial_types
    global all_choices
    global recall_choices
    global time2choices

    Q_num = str(1)

    total_trial_count += 1
    
    turtle.color('black')
    style = ('Arial', 20, 'bold')
    turtle.write('\
How many people are at risk of dying from the dangerous new disease?', font=style, align='center')
    turtle.hideturtle()
    
    while not Q1_answer:
        Q1_answer = turtle.textinput('Input', 'Response:')

    if Q1_answer and len(Q1_answers) == 0:
        all_cds_rts()
        events.append('Recall Question ' + Q_num)
        trial_types.append(3)
        number = str(1)
        get_recall_loop_cds_rts()
        Qs_time2choices_append()
        time2choices.append(all_rts[-1] - all_rts[-2])
        recall_time2choices_append()
        all_choices.append(Q1_answer)
        Q1_answers.append(Q1_answer)
        Q1_answer = ''
    
    if Q1_answer and len(Q1_answers) > 0:
        all_cds_rts()
        events.append('Recall Question ' + Q_num)
        trial_types.append(3)
        number = str(1)
        get_recall_loop_cds_rts()
        Qs_time2choices_append()
        time2choices.append(all_rts[-1] - all_rts[-2])
        recall_time2choices_append()
        all_choices.append(Q1_answer)
        Q1_answers.append(Q1_answer)
        Q1_answer = ''
        
    turtle.clear()
    question2(recall_choices[-1])
    return




'''
BUTTON FUNCTIONS
'''


def recall_choice_a():
    global true_trial_count
    global false_trial_count
    
    global recall_trial_count
    global true_recall_trial_count
    global false_recall_trial_count
    global total_trial_count
    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()
    
    all_choice = 'A'


    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    get_recall_loop_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    recall_time2choices_append()
    
    recall_choices_append(all_choice)
    total_trial_count += 1
    recall_trial_count += 1
    
    three_consec_true_choices()

# Checks if choice made on time and captures its information
    if recall_choice_timer() == True:
        true_recall_trial_count += 1
        true_trial_count += 1
        true_recall_choice_cds_rts()
        true_choice_cds_rts()
        true_choices_append(all_choice)
        true_recall_choices_append(all_choice)
                
    if recall_choice_timer() == False:
        false_recall_trial_count += 1
        false_trial_count += 1
        false_recall_choice_cds_rts()
        false_choice_cds_rts()
        false_choices_append(all_choice)
        false_recall_choices.append(all_choice)


    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(2)

    events.append('CC')

    turtle.clearscreen()
    question1()
    return


def recall_choice_b():
    global true_trial_count
    global false_trial_count
    
    global recall_trial_count
    global true_recall_trial_count
    global false_recall_trial_count
    global total_trial_count
    
    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'B'


    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    get_recall_loop_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    recall_time2choices_append()
    recall_choices_append(all_choice)
    total_trial_count += 1
    recall_trial_count += 1
    
    three_consec_true_choices()


# Checks if choice made on time and captures its information
    if recall_choice_timer() == True:
        true_recall_trial_count += 1
        true_trial_count += 1
        true_recall_choice_cds_rts()
        true_choice_cds_rts()
        true_choices_append(all_choice)
        true_recall_choices_append(all_choice)
                
    if recall_choice_timer() == False:
        false_recall_trial_count += 1
        false_trial_count += 1
        false_recall_choice_cds_rts()
        false_choice_cds_rts()
        false_choices_append(all_choice)
        false_recall_choices.append(all_choice)
        
    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(2)

    events.append('CC')
    
    turtle.clearscreen()
    question1()
    return


# BUTTONS FOR SURE WEIGHTED CATCH TRIALS

def catch_sure_weighted_initiative_a():
    global true_trial_count
    global false_trial_count
    
    global true_game_trial_count
    global false_game_trial_count
    
    global catch_sure_weighted_trial_count
    
    global true_catch_trial_count
    global false_catch_trial_count
    global true_catch_sure_weighted_trial_count
    global false_catch_sure_weighted_trial_count

    global total_trial_count
    global catch_trial_count

    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'A'

    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    
    total_trial_count += 1
    catch_trial_count += 1
    catch_sure_weighted_trial_count += 1

# Checks if choice made on time and captures its information
    if choice_timer() == True:
        true_trial_count += 1
        true_catch_trial_count += 1
        true_catch_sure_weighted_trial_count += 1

        true_choice_cds_rts()
        true_catch_trial_cds_rts()
        true_catch_sure_weighted_cds_rts()

        true_choices_append(all_choice)
        true_catch_trial_choices_append(all_choice)
        
    if choice_timer() == False:
        false_trial_count += 1
        false_catch_trial_count += 1
        false_catch_sure_weighted_trial_count += 1

        # catch trial function for same button would call true_choice
        false_choice_cds_rts()
        false_catch_trial_cds_rts()
        false_catch_sure_weighted_cds_rts()

        # capture choice to all_choices, false_choices, and false_game_trial_choices
        false_choices_append(all_choice)
        false_catch_trial_choices_append(all_choice)

    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(1)
    
    trial_types.append('')
    
    events.append('CC')

    trial_decider()
    return


def catch_sure_weighted_initiative_b():
    global true_trial_count
    global false_trial_count
    
    global true_game_trial_count
    global false_game_trial_count
    
    global catch_sure_weighted_trial_count
    
    global true_catch_trial_count
    global false_catch_trial_count
    global true_catch_sure_weighted_trial_count
    global false_catch_sure_weighted_trial_count

    global total_trial_count
    global catch_trial_count

    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'B'

    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    
    total_trial_count += 1
    catch_trial_count += 1
    catch_sure_weighted_trial_count += 1

# Checks if choice made on time and captures its information
    if choice_timer() == True:
        true_trial_count += 1
        true_catch_trial_count += 1
        true_catch_sure_weighted_trial_count += 1

        true_choice_cds_rts()
        true_catch_trial_cds_rts()
        true_catch_sure_weighted_cds_rts()

        true_choices_append(all_choice)
        true_catch_trial_choices_append(all_choice)
                
    if choice_timer() == False:
        false_trial_count += 1
        false_catch_trial_count += 1
        false_catch_sure_weighted_trial_count += 1

        # catch trial function for same button would call true_choice
        false_choice_cds_rts()
        false_catch_trial_cds_rts()
        false_catch_sure_weighted_cds_rts()

        # capture choice to all_choices, false_choices, and false_game_trial_choices
        false_choices_append(all_choice)
        false_catch_trial_choices_append(all_choice)

    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(1)
    
    trial_types.append('')
    
    events.append('CC')

    trial_decider()
    return

'''
# BUTTONS FOR GAMBLE WEIGHTED CATCH TRIALS
def catch_gamble_weighted_initiative_a():
    global true_trial_count
    global false_trial_count
    
    global true_game_trial_count
    global false_game_trial_count

    global catch_gamble_weighted_trial_count
        
    global true_catch_trial_count
    global false_catch_trial_count
    global true_catch_gamble_weighted_trial_count
    global false_catch_gamble_weighted_trial_count

    global total_trial_count
    global catch_trial_count

    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'A'

    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    
    total_trial_count += 1
    catch_trial_count += 1
    catch_gamble_weighted_trial_count += 1

# Checks if choice made on time and captures its information
    if choice_timer() == True:
        true_trial_count += 1
        true_catch_trial_count += 1
        true_catch_gamble_weighted_trial_count += 1

        true_choice_cds_rts()
        true_catch_trial_cds_rts()
        true_catch_gamble_weighted_cds_rts()

        true_choices_append(all_choice)
        true_catch_trial_choices_append(all_choice)
        
    if choice_timer() == False:
        false_trial_count += 1
        false_catch_trial_count += 1
        false_catch_gamble_weighted_trial_count += 1

        # catch trial function for same button would call true_choice
        false_choice_cds_rts()
        false_catch_trial_cds_rts()
        false_catch_gamble_weighted_cds_rts()

        # capture choice to all_choices, false_choices, and false_game_trial_choices
        false_choices_append(all_choice)
        false_catch_trial_choices_append(all_choice)

    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(1)
    
    trial_types.append('')
    
    events.append('CC')

    trial_decider()
    return


def catch_gamble_weighted_initiative_b():
    global true_trial_count
    global false_trial_count
    
    global true_game_trial_count
    global false_game_trial_count
    
    global catch_gamble_weighted_trial_count
    
    global true_catch_trial_count
    global false_catch_trial_count
    global true_catch_gamble_weighted_trial_count
    global false_catch_gamble_weighted_trial_count

    global total_trial_count
    global catch_trial_count

    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'B'

    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    
    total_trial_count += 1
    catch_trial_count += 1
    catch_gamble_weighted_trial_count += 1

# Checks if choice made on time and captures its information
    if choice_timer() == True:
        true_trial_count += 1
        true_catch_trial_count += 1
        true_catch_gamble_weighted_trial_count += 1

        true_choice_cds_rts()
        true_catch_trial_cds_rts()
        true_catch_gamble_weighted_cds_rts()

        true_choices_append(all_choice)
        true_catch_trial_choices_append(all_choice)
                
    if choice_timer() == False:
        false_trial_count += 1
        false_catch_trial_count += 1
        false_catch_gamble_weighted_trial_count += 1

        # catch trial function for same button would call true_choice
        false_choice_cds_rts()
        false_catch_trial_cds_rts()
        false_catch_gamble_weighted_cds_rts()

        # capture choice to all_choices, false_choices, and false_game_trial_choices
        false_choices_append(all_choice)
        false_catch_trial_choices_append(all_choice)

    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(1)
    
    trial_types.append('')
    
    events.append('CC')

    trial_decider()
    return
'''

def game_initiative_a():
    global true_trial_count
    global false_trial_count
    
    global true_game_trial_count
    global false_game_trial_count

    global true_catch_trial_count
    global false_catch_trial_count
    global true_game_trial_count
    global false_game_trial_count

    global total_trial_count
    global game_trial_count

    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'A'


    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    
    total_trial_count += 1
    game_trial_count += 1


# Checks if choice made on time and captures its information
    if choice_timer():
        true_trial_count += 1
        true_game_trial_count += 1

        true_choice_cds_rts()
        true_game_trial_cds_rts()

        true_choices_append(all_choice)
        true_game_trial_choices_append(all_choice)
                
    if choice_timer() == False:
        false_trial_count += 1
        false_game_trial_count += 1

        # catch trial function for same button would call true_choice
        false_choice_cds_rts()
        false_game_trial_cds_rts()

        # capture choice to all_choices, false_choices, and false_game_trial_choices
        false_choices_append(all_choice)
        false_game_trial_choices_append(all_choice)

    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(0)
    
    trial_types.append('')

    events.append('CC')

    trial_decider()
    return




def game_initiative_b():
    global true_trial_count
    global false_trial_count
    
    global true_game_trial_count
    global false_game_trial_count

    global true_catch_trial_count
    global false_catch_trial_count
    global true_game_trial_count
    global false_game_trial_count

    global total_trial_count
    global game_trial_count

    global all_choice
    global all_choices
    global events

    global trial_types
    global time2choices

    turtle.clearscreen()

    all_choice = 'B'

    # capture all cd and rt times and reset variables all_cd and all_rt
    all_cds_rts()
    time2choices.append('')
    time2choices.append(all_rts[-1] - all_rts[-2])
    
    total_trial_count += 1
    game_trial_count += 1

# Checks if choice made on time and captures its information
    if choice_timer():
        true_trial_count += 1
        true_game_trial_count += 1

        true_choice_cds_rts()
        true_game_trial_cds_rts()

        true_choices_append(all_choice)
        true_game_trial_choices_append(all_choice)
                
    if choice_timer() == False:
        false_trial_count += 1
        false_game_trial_count += 1

        # catch trial function for same button would call true_choice
        false_choice_cds_rts()
        false_game_trial_cds_rts()

        # capture choice to all_choices, false_choices, and false_game_trial_choices
        false_choices_append(all_choice)
        false_game_trial_choices_append(all_choice)
        
    all_choices.append('')
    all_choices.append(all_choice)
    trial_types.append(0)
    
    trial_types.append('')

    events.append('CC')

    trial_decider()
    return





'''
FUNCTIONS PRESENTING CHOICE BUTTONS
'''

def recall_trial():
    turtle.clear()
    button1 = tk.Button(canvas.master, text="\n\
            A) 200 people will be saved            \
\n", font=arial20, command=recall_choice_a)
    canvas.create_window(-320, 0, window=button1)

    button2 = tk.Button(canvas.master, text="B) 33.3% chance that everyone will \
be saved\n and a \n 66.6% chance that no one will be saved\
", font=arial20, command=recall_choice_b)
    canvas.create_window(300, 0, window=button2)
    return



# CATCH TRIAL SURE WEIGHTED BUTTONS CODE
def catch_trial_sure_weighted():
    turtle.clear()
    button1 = tk.Button(canvas.master, text="\n\
            A) 570 people will be saved            \
\n", font=arial20, command=catch_sure_weighted_initiative_a)
    canvas.create_window(0, -175, window=button1)

    button2 = tk.Button(canvas.master, text="B) 5% chance that everyone will \
be saved \n and a \n 95% chance that no one will be saved\
", font=arial20, command=catch_sure_weighted_initiative_b)
    canvas.create_window(0, 150, window=button2)
    return


'''
# CATCH TRIAL GAMBLE WEIGHTED BUTTONS CODE
def catch_trial_gamble_weighted():
    turtle.clear()
    button1 = tk.Button(canvas.master, text="\nA) 30 people will be saved\
\n", font=arial20, command=catch_gamble_weighted_initiative_a)
    canvas.create_window(0, -175, window=button1)

    button2 = tk.Button(canvas.master, text="B) 95% chance that everyone will \
be saved \n and a \n 5% chance that no one will be saved\
", font=arial20, command=catch_gamble_weighted_initiative_b)
    canvas.create_window(0, 150, window=button2)
    return
'''


def game_trial():
    turtle.clear()
    button1 = tk.Button(canvas.master, text="\n\
            A) 200 people will be saved            \
\n", font=arial20, command=game_initiative_a)
    canvas.create_window(-320, 0, window=button1)

    button2 = tk.Button(canvas.master, text="B) 33.3% chance that everyone will \
be saved\n and a \n 66.6% chance that no one will be saved\
", font=arial20, command=game_initiative_b)
    canvas.create_window(300, 0, window=button2)
    return





'''
VIGNETTES
'''

def recall_loop():
    global events
    turtle.hideturtle()
    style = ('Arial', 20, 'bold')
    turtle.write('Imagine a dangerous new disease \
has been going around. \n\
Without medicine, 600 people will die. \n\
In order to save these people, a team of researchers is developing two medicines, \n\
A and B, with different potential outcomes. \n\n\
Which medicine do you choose?', font=style, align='center')
    turtle.hideturtle()

    sleep(8)
    all_cds_rts()
    events.append('Recall VE')
    get_recall_loop_cds_rts()
    
    recall_trial()

    
def game_disease_vignette():
    global events
    turtle.hideturtle()
    style = ('Arial', 20, 'bold')
    turtle.write('Imagine a dangerous new disease \
has been going around. \n\
Without medicine, 600 people will die. \n\
In order to save these people, a team of researchers is developing two medicines, \n\
A and B, with different potential outcomes. \n\n\
Which medicine do you choose?', font=style, align='center')
    turtle.hideturtle()

    sleep(8)
    all_cds_rts()
    events.append('Game VE')
    
    game_trial()


def catch_disease_vignette():
    global events
    turtle.hideturtle()
    style = ('Arial', 20, 'bold')
    turtle.write('Imagine a dangerous new disease \
has been going around. \n\
Without medicine, 600 people will die. \n\
In order to save these people, a team of researchers is developing two medicines, \n\
A and B, with different potential outcomes. \n\n\
Which medicine do you choose?', font=style, align='center')
    turtle.hideturtle()

    sleep(8)
    all_cds_rts()
    events.append('Catch VE')

    # Button options called within vignette function
    catch_trial_sure_weighted()




'''
INITIAL TASK INSTRUCTIONS & COUNTDOWN SEQUENCE
'''

def three_21():

    button3.destroy()

    turtle.goto(0, 0)

    for i in [3, 2, 1]:
        turtle.clear()
        turtle.hideturtle()
        style2 = ('Arial', 50, 'bold')
        turtle.write(i, font=style2, align='center')
        turtle.hideturtle()
        sleep(1)
        turtle.clear()

    all_cds_rts()
    events.append('321 end')
    trial_types.append('')
    time2choices.append('')
  
    game_disease_vignette()
            
def introduction():
    
    turtle.clear()
    style = ('Arial', 20, 'bold')
    turtle.write('Please read the following scenario and select \
one of the options that follow within 10 seconds.', font=style, align='center')
    turtle.hideturtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, -85)
    #turtle.hideturtle()
    turtle.write('Click "START" to begin.', font=style, align='center')
    button3.pack()
    canvas.create_window(0, 150, window=button3)
    turtle.hideturtle()
    

def get_id():
    global ID
    global all_choices
    global id_cd
    global all_cds
    global id_rt
    global all_rts
    global trial_types
    global time2choices
    
    # Condition is met only at the start of the program where ID = '' and len(all_choices) == 0
    if not ID:
        # len(all_choices) will no longer == 0
        style = ('Arial', 20, 'bold')
        turtle.write('Enter your Participant ID.', font=style, align='center')
        turtle.hideturtle()
        while not ID:
            ID = turtle.textinput('Input', 'Participant ID:')

    if ID and len(all_choices) == 0:
        id_cd = my_timer
        all_cds.append(id_cd)

        all_choices.append(ID)
        
        id_rt = 0
        all_rts.append(id_rt)
        events.append('ID Input')
        trial_types.append('Get ID')
        trial_types.append('')
        all_choices.append('')
        time2choices.append('')
        
    return


screen = Screen()
screen.title('Experimental Session')
screen.bgcolor('white')
screen.setup(width=1.0, height=1.0)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
arial20 = tkFont.Font(family='Arial', size=20, weight=tkFont.BOLD)
arial50 = tkFont.Font(family='Arial', size=50, weight=tkFont.BOLD)


# Start the countdown
countdown_thread = threading.Thread(target=timer)
countdown_thread.start()

fns = [game_disease_vignette, catch_disease_vignette]

button3 = tk.Button(canvas.master, text="START", font=arial20, command=three_21)

get_id()
introduction()

screen.listen()
screen.mainloop()
