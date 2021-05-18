#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Tue Jan 21 20:00:02 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'EDE_even'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/Data_Raw/HKU_PANDM_EDE_ShirleyLI/Documents/EDE_v1_ShirleyLI/EDE_v1_odd_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Exp_Instruction_Begin"
Exp_Instruction_BeginClock = core.Clock()
Beginning_Instruction = visual.TextStim(win=win, name='Beginning_Instruction',
    text='Welcome to the Experiment!\n\nThere are many fearful face and neutral face images stored in the computer database.Each time the computer program will randomly select 30 face images.You will see 10 of these 30 face images.\n\nFor each of the 10 images, you will identify the emotion of the face.After viewing all 10 faces, you will be asked to estimate what percentage of the 30 faces are fearful or neutral based on the 10 faces you have seen.\n\nPress the Space bar to Continue.\n\n',
    font='Arial',
    pos=(0.01, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
next_frame = keyboard.Keyboard()

# Initialize components for Routine "practice_text"
practice_textClock = core.Clock()
prac_text = visual.TextStim(win=win, name='prac_text',
    text='You will start with a practice round! \nPress the Space bar to Continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "Instruction_I"
Instruction_IClock = core.Clock()
InstructionText2 = visual.TextStim(win=win, name='InstructionText2',
    text='default text',
    font='Arial Block',
    pos=(0.26, 0.022), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_response = keyboard.Keyboard()
constantText = visual.TextStim(win=win, name='constantText',
    text='Followed by a Purple fixation, you will see a face.\nYour task is to indicate if the face is             or not.\n\nPress the Space bar to Continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Resp_Instruction"
Resp_InstructionClock = core.Clock()
changing_text = visual.TextStim(win=win, name='changing_text',
    text='default text',
    font='Arial',
    pos=(0.12, 0.14), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
changing_text_2 = visual.TextStim(win=win, name='changing_text_2',
    text='default text',
    font='Arial',
    pos=(0.16, 0.09), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Constant_text = visual.TextStim(win=win, name='Constant_text',
    text="Press 'V' if Yes, the face is \nPress 'B' if No, the face is             \nPlease use your dominant hand only.\n\nRespond as quick and accurate as possible.\n\nWhen you are ready, press the Space bar to begin",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "PracticeTrial"
PracticeTrialClock = core.Clock()
thisLoop_p = 0

PurpleFixation_2 = visual.ShapeStim(
    win=win, name='PurpleFixation_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[138,43,226], fillColorSpace='rgb255',
    opacity=1, depth=-2.0, interpolate=True)
StimImage_2 = visual.ImageStim(
    win=win,
    name='StimImage_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
WhiteFixation_2 = visual.ShapeStim(
    win=win, name='WhiteFixation_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
key_resp_3 = keyboard.Keyboard()
maskbefore = visual.ImageStim(
    win=win,
    name='maskbefore', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
maskafter = visual.ImageStim(
    win=win,
    name='maskafter', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)

# Initialize components for Routine "QnRating"
QnRatingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0.01, 0.245), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
constantText_Qn = visual.TextStim(win=win, name='constantText_Qn',
    text='Based on the past 10 trials, \nWhat percentage of                      in the image set?\n\nClick on the scale below. To submit your response, please click on the number shown in the box.',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.2], low=0, high=100, labels=['0%', ' 100%'], scale='')

# Initialize components for Routine "ActualRun"
ActualRunClock = core.Clock()
ActualR_text = visual.TextStim(win=win, name='ActualR_text',
    text="Now, let's begin with the actual rounds!\nPress the space bar to continue.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "Instruction_I"
Instruction_IClock = core.Clock()
InstructionText2 = visual.TextStim(win=win, name='InstructionText2',
    text='default text',
    font='Arial Block',
    pos=(0.26, 0.022), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_response = keyboard.Keyboard()
constantText = visual.TextStim(win=win, name='constantText',
    text='Followed by a Purple fixation, you will see a face.\nYour task is to indicate if the face is             or not.\n\nPress the Space bar to Continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Resp_Instruction"
Resp_InstructionClock = core.Clock()
changing_text = visual.TextStim(win=win, name='changing_text',
    text='default text',
    font='Arial',
    pos=(0.12, 0.14), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
changing_text_2 = visual.TextStim(win=win, name='changing_text_2',
    text='default text',
    font='Arial',
    pos=(0.16, 0.09), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Constant_text = visual.TextStim(win=win, name='Constant_text',
    text="Press 'V' if Yes, the face is \nPress 'B' if No, the face is             \nPlease use your dominant hand only.\n\nRespond as quick and accurate as possible.\n\nWhen you are ready, press the Space bar to begin",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "BlockStopper"
BlockStopperClock = core.Clock()
thisBlock = 0

# Initialize components for Routine "trial"
trialClock = core.Clock()
thisLoop = 0

PurpleFixation = visual.ShapeStim(
    win=win, name='PurpleFixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[138,43,226], fillColorSpace='rgb255',
    opacity=1, depth=-2.0, interpolate=True)
StimImage = visual.ImageStim(
    win=win,
    name='StimImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
WhiteFixation = visual.ShapeStim(
    win=win, name='WhiteFixation', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Trial_KeyResp = keyboard.Keyboard()
maskbefore2 = visual.ImageStim(
    win=win,
    name='maskbefore2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
maskafter2 = visual.ImageStim(
    win=win,
    name='maskafter2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "QnRating"
QnRatingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0.01, 0.245), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
constantText_Qn = visual.TextStim(win=win, name='constantText_Qn',
    text='Based on the past 10 trials, \nWhat percentage of                      in the image set?\n\nClick on the scale below. To submit your response, please click on the number shown in the box.',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.2], low=0, high=100, labels=['0%', ' 100%'], scale='')

# Initialize components for Routine "short_break"
short_breakClock = core.Clock()
break_screen = visual.TextStim(win=win, name='break_screen',
    text='Please take a short break\n\nPress the SPACE key when you are ready to continue\n\nRemember to respond as quick and accurate as possible\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_break = keyboard.Keyboard()

# Initialize components for Routine "Instruction_I"
Instruction_IClock = core.Clock()
InstructionText2 = visual.TextStim(win=win, name='InstructionText2',
    text='default text',
    font='Arial Block',
    pos=(0.26, 0.022), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_response = keyboard.Keyboard()
constantText = visual.TextStim(win=win, name='constantText',
    text='Followed by a Purple fixation, you will see a face.\nYour task is to indicate if the face is             or not.\n\nPress the Space bar to Continue.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Resp_Instruction"
Resp_InstructionClock = core.Clock()
changing_text = visual.TextStim(win=win, name='changing_text',
    text='default text',
    font='Arial',
    pos=(0.12, 0.14), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
changing_text_2 = visual.TextStim(win=win, name='changing_text_2',
    text='default text',
    font='Arial',
    pos=(0.16, 0.09), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Constant_text = visual.TextStim(win=win, name='Constant_text',
    text="Press 'V' if Yes, the face is \nPress 'B' if No, the face is             \nPlease use your dominant hand only.\n\nRespond as quick and accurate as possible.\n\nWhen you are ready, press the Space bar to begin",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "BlockStopperb"
BlockStopperbClock = core.Clock()
thisBlockb = 0

# Initialize components for Routine "trialb"
trialbClock = core.Clock()
thisLoopb = 0

PurpleFixationb = visual.ShapeStim(
    win=win, name='PurpleFixationb', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[138,43,226], fillColorSpace='rgb255',
    opacity=1, depth=-2.0, interpolate=True)
StimImageb = visual.ImageStim(
    win=win,
    name='StimImageb', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
WhiteFixationb = visual.ShapeStim(
    win=win, name='WhiteFixationb', vertices='cross',
    size=(0.1, 0.1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Trial_KeyRespb = keyboard.Keyboard()
maskbeforeb = visual.ImageStim(
    win=win,
    name='maskbeforeb', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
maskafterb = visual.ImageStim(
    win=win,
    name='maskafterb', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)

# Initialize components for Routine "QnRating"
QnRatingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0.01, 0.245), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
constantText_Qn = visual.TextStim(win=win, name='constantText_Qn',
    text='Based on the past 10 trials, \nWhat percentage of                      in the image set?\n\nClick on the scale below. To submit your response, please click on the number shown in the box.',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.2], low=0, high=100, labels=['0%', ' 100%'], scale='')

# Initialize components for Routine "Exp_Ending"
Exp_EndingClock = core.Clock()
EndingMsg = visual.TextStim(win=win, name='EndingMsg',
    text='Thank you for your participation! ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Exp_Instruction_Begin"-------
# update component parameters for each repeat
next_frame.keys = []
next_frame.rt = []
# keep track of which components have finished
Exp_Instruction_BeginComponents = [Beginning_Instruction, next_frame]
for thisComponent in Exp_Instruction_BeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Exp_Instruction_BeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Exp_Instruction_Begin"-------
while continueRoutine:
    # get current time
    t = Exp_Instruction_BeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Exp_Instruction_BeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Beginning_Instruction* updates
    if Beginning_Instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Beginning_Instruction.frameNStart = frameN  # exact frame index
        Beginning_Instruction.tStart = t  # local t and not account for scr refresh
        Beginning_Instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Beginning_Instruction, 'tStartRefresh')  # time at next scr refresh
        Beginning_Instruction.setAutoDraw(True)
    
    # *next_frame* updates
    waitOnFlip = False
    if next_frame.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        next_frame.frameNStart = frameN  # exact frame index
        next_frame.tStart = t  # local t and not account for scr refresh
        next_frame.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next_frame, 'tStartRefresh')  # time at next scr refresh
        next_frame.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(next_frame.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if next_frame.status == STARTED and not waitOnFlip:
        theseKeys = next_frame.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Exp_Instruction_BeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Exp_Instruction_Begin"-------
for thisComponent in Exp_Instruction_BeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Beginning_Instruction.started', Beginning_Instruction.tStartRefresh)
thisExp.addData('Beginning_Instruction.stopped', Beginning_Instruction.tStopRefresh)
# the Routine "Exp_Instruction_Begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_text"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
practice_textComponents = [prac_text, key_resp_4]
for thisComponent in practice_textComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_textClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practice_text"-------
while continueRoutine:
    # get current time
    t = practice_textClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_textClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_text* updates
    if prac_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_text.frameNStart = frameN  # exact frame index
        prac_text.tStart = t  # local t and not account for scr refresh
        prac_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_text, 'tStartRefresh')  # time at next scr refresh
        prac_text.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys = theseKeys.name  # just the last key pressed
            key_resp_4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_textComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_text"-------
for thisComponent in practice_textComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prac_text.started', prac_text.tStartRefresh)
thisExp.addData('prac_text.stopped', prac_text.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_text" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Practice.xlsx'),
    seed=None, name='Practice')
thisExp.addLoop(Practice)  # add the loop to the experiment
thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in Practice:
    currentLoop = Practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction_I"-------
    # update component parameters for each repeat
    InstructionText2.setColor(textColor, colorSpace='rgb')
    InstructionText2.setText(Instruction_I)
    instruction_response.keys = []
    instruction_response.rt = []
    # keep track of which components have finished
    Instruction_IComponents = [InstructionText2, instruction_response, constantText]
    for thisComponent in Instruction_IComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instruction_IClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Instruction_I"-------
    while continueRoutine:
        # get current time
        t = Instruction_IClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instruction_IClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionText2* updates
        if InstructionText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionText2.frameNStart = frameN  # exact frame index
            InstructionText2.tStart = t  # local t and not account for scr refresh
            InstructionText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionText2, 'tStartRefresh')  # time at next scr refresh
            InstructionText2.setAutoDraw(True)
        
        # *instruction_response* updates
        waitOnFlip = False
        if instruction_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_response.frameNStart = frameN  # exact frame index
            instruction_response.tStart = t  # local t and not account for scr refresh
            instruction_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_response, 'tStartRefresh')  # time at next scr refresh
            instruction_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instruction_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_response.status == STARTED and not waitOnFlip:
            theseKeys = instruction_response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *constantText* updates
        if constantText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            constantText.frameNStart = frameN  # exact frame index
            constantText.tStart = t  # local t and not account for scr refresh
            constantText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(constantText, 'tStartRefresh')  # time at next scr refresh
            constantText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction_I"-------
    for thisComponent in Instruction_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('InstructionText2.started', InstructionText2.tStartRefresh)
    Practice.addData('InstructionText2.stopped', InstructionText2.tStopRefresh)
    Practice.addData('constantText.started', constantText.tStartRefresh)
    Practice.addData('constantText.stopped', constantText.tStopRefresh)
    # the Routine "Instruction_I" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Resp_Instruction"-------
    # update component parameters for each repeat
    changing_text.setColor(textColor, colorSpace='rgb')
    changing_text.setText(Instruction_I)
    changing_text_2.setColor(textColor, colorSpace='rgb')
    changing_text_2.setText(Instruction2
)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    Resp_InstructionComponents = [changing_text, changing_text_2, Constant_text, key_resp_2]
    for thisComponent in Resp_InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Resp_InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Resp_Instruction"-------
    while continueRoutine:
        # get current time
        t = Resp_InstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Resp_InstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *changing_text* updates
        if changing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            changing_text.frameNStart = frameN  # exact frame index
            changing_text.tStart = t  # local t and not account for scr refresh
            changing_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changing_text, 'tStartRefresh')  # time at next scr refresh
            changing_text.setAutoDraw(True)
        
        # *changing_text_2* updates
        if changing_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            changing_text_2.frameNStart = frameN  # exact frame index
            changing_text_2.tStart = t  # local t and not account for scr refresh
            changing_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changing_text_2, 'tStartRefresh')  # time at next scr refresh
            changing_text_2.setAutoDraw(True)
        
        # *Constant_text* updates
        if Constant_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Constant_text.frameNStart = frameN  # exact frame index
            Constant_text.tStart = t  # local t and not account for scr refresh
            Constant_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Constant_text, 'tStartRefresh')  # time at next scr refresh
            Constant_text.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Resp_InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Resp_Instruction"-------
    for thisComponent in Resp_InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('changing_text.started', changing_text.tStartRefresh)
    Practice.addData('changing_text.stopped', changing_text.tStopRefresh)
    Practice.addData('changing_text_2.started', changing_text_2.tStartRefresh)
    Practice.addData('changing_text_2.stopped', changing_text_2.tStopRefresh)
    Practice.addData('Constant_text.started', Constant_text.tStartRefresh)
    Practice.addData('Constant_text.stopped', Constant_text.tStopRefresh)
    # the Routine "Resp_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PracticeTrials = data.TrialHandler(nReps=10, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TrialType_p.xlsx', selection=str(thisLoop_p)+":"+str(thisLoop_p+10)),
        seed=None, name='PracticeTrials')
    thisExp.addLoop(PracticeTrials)  # add the loop to the experiment
    thisPracticeTrial = PracticeTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    for thisPracticeTrial in PracticeTrials:
        currentLoop = PracticeTrials
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                exec('{} = thisPracticeTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "PracticeTrial"-------
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        thisLoop_p +=1
        if thisLoop_p%10==0:
            PracticeTrials.finished=1
        StimImage_2.contrast = Contrast
        
        StimImage_2.setImage(StimImageFile)
        import random
        WhiteDuration = random.uniform(3,4)
        thisExp.addData('White_random_duration_p', WhiteDuration)
        key_resp_3.keys = []
        key_resp_3.rt = []
        maskbefore.contrast = Contrast
        maskbefore.setImage(Masks)
        maskafter.setImage(Masks)
        maskafter.contrast = Contrast
        # keep track of which components have finished
        PracticeTrialComponents = [PurpleFixation_2, StimImage_2, WhiteFixation_2, key_resp_3, maskbefore, maskafter]
        for thisComponent in PracticeTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "PracticeTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = PracticeTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PurpleFixation_2* updates
            if PurpleFixation_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                PurpleFixation_2.frameNStart = frameN  # exact frame index
                PurpleFixation_2.tStart = t  # local t and not account for scr refresh
                PurpleFixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PurpleFixation_2, 'tStartRefresh')  # time at next scr refresh
                PurpleFixation_2.setAutoDraw(True)
            if PurpleFixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PurpleFixation_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    PurpleFixation_2.tStop = t  # not accounting for scr refresh
                    PurpleFixation_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PurpleFixation_2, 'tStopRefresh')  # time at next scr refresh
                    PurpleFixation_2.setAutoDraw(False)
            
            # *StimImage_2* updates
            if StimImage_2.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                StimImage_2.frameNStart = frameN  # exact frame index
                StimImage_2.tStart = t  # local t and not account for scr refresh
                StimImage_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(StimImage_2, 'tStartRefresh')  # time at next scr refresh
                StimImage_2.setAutoDraw(True)
            if StimImage_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > StimImage_2.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    StimImage_2.tStop = t  # not accounting for scr refresh
                    StimImage_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(StimImage_2, 'tStopRefresh')  # time at next scr refresh
                    StimImage_2.setAutoDraw(False)
            
            # *WhiteFixation_2* updates
            if WhiteFixation_2.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                # keep track of start time/frame for later
                WhiteFixation_2.frameNStart = frameN  # exact frame index
                WhiteFixation_2.tStart = t  # local t and not account for scr refresh
                WhiteFixation_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WhiteFixation_2, 'tStartRefresh')  # time at next scr refresh
                WhiteFixation_2.setAutoDraw(True)
            if WhiteFixation_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > WhiteFixation_2.tStartRefresh + 2.8-frameTolerance:
                    # keep track of stop time/frame for later
                    WhiteFixation_2.tStop = t  # not accounting for scr refresh
                    WhiteFixation_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(WhiteFixation_2, 'tStopRefresh')  # time at next scr refresh
                    WhiteFixation_2.setAutoDraw(False)
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_3.tStartRefresh + 3.2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_3.tStop = t  # not accounting for scr refresh
                    key_resp_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                    key_resp_3.status = FINISHED
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['v', 'b'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if key_resp_3.keys == []:  # then this was the first keypress
                        key_resp_3.keys = theseKeys.name  # just the first key pressed
                        key_resp_3.rt = theseKeys.rt
                        # was this 'correct'?
                        if (key_resp_3.keys == str(CorrectResp)) or (key_resp_3.keys == CorrectResp):
                            key_resp_3.corr = 1
                        else:
                            key_resp_3.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *maskbefore* updates
            if maskbefore.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                maskbefore.frameNStart = frameN  # exact frame index
                maskbefore.tStart = t  # local t and not account for scr refresh
                maskbefore.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(maskbefore, 'tStartRefresh')  # time at next scr refresh
                maskbefore.setAutoDraw(True)
            if maskbefore.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maskbefore.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    maskbefore.tStop = t  # not accounting for scr refresh
                    maskbefore.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(maskbefore, 'tStopRefresh')  # time at next scr refresh
                    maskbefore.setAutoDraw(False)
            
            # *maskafter* updates
            if maskafter.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                # keep track of start time/frame for later
                maskafter.frameNStart = frameN  # exact frame index
                maskafter.tStart = t  # local t and not account for scr refresh
                maskafter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(maskafter, 'tStartRefresh')  # time at next scr refresh
                maskafter.setAutoDraw(True)
            if maskafter.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > maskafter.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    maskafter.tStop = t  # not accounting for scr refresh
                    maskafter.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(maskafter, 'tStopRefresh')  # time at next scr refresh
                    maskafter.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeTrial"-------
        for thisComponent in PracticeTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        PracticeTrials.addData('PurpleFixation_2.started', PurpleFixation_2.tStartRefresh)
        PracticeTrials.addData('PurpleFixation_2.stopped', PurpleFixation_2.tStopRefresh)
        PracticeTrials.addData('StimImage_2.started', StimImage_2.tStartRefresh)
        PracticeTrials.addData('StimImage_2.stopped', StimImage_2.tStopRefresh)
        PracticeTrials.addData('WhiteFixation_2.started', WhiteFixation_2.tStartRefresh)
        PracticeTrials.addData('WhiteFixation_2.stopped', WhiteFixation_2.tStopRefresh)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(CorrectResp).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for PracticeTrials (TrialHandler)
        PracticeTrials.addData('key_resp_3.keys',key_resp_3.keys)
        PracticeTrials.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            PracticeTrials.addData('key_resp_3.rt', key_resp_3.rt)
        PracticeTrials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
        PracticeTrials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
        PracticeTrials.addData('maskbefore.started', maskbefore.tStartRefresh)
        PracticeTrials.addData('maskbefore.stopped', maskbefore.tStopRefresh)
        PracticeTrials.addData('maskafter.started', maskafter.tStartRefresh)
        PracticeTrials.addData('maskafter.stopped', maskafter.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 10 repeats of 'PracticeTrials'
    
    # get names of stimulus parameters
    if PracticeTrials.trialList in ([], [None], None):
        params = []
    else:
        params = PracticeTrials.trialList[0].keys()
    # save data for this loop
    PracticeTrials.saveAsExcel(filename + '.xlsx', sheetName='PracticeTrials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    PracticeTrials.saveAsText(filename + 'PracticeTrials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "QnRating"-------
    # update component parameters for each repeat
    text.setColor(Color, colorSpace='rgb')
    text.setText(Questionnaire)
    rating.reset()
    # keep track of which components have finished
    QnRatingComponents = [text, constantText_Qn, rating]
    for thisComponent in QnRatingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    QnRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "QnRating"-------
    while continueRoutine:
        # get current time
        t = QnRatingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=QnRatingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *constantText_Qn* updates
        if constantText_Qn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            constantText_Qn.frameNStart = frameN  # exact frame index
            constantText_Qn.tStart = t  # local t and not account for scr refresh
            constantText_Qn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(constantText_Qn, 'tStartRefresh')  # time at next scr refresh
            constantText_Qn.setAutoDraw(True)
        # *rating* updates
        if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating.frameNStart = frameN  # exact frame index
            rating.tStart = t  # local t and not account for scr refresh
            rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
            rating.setAutoDraw(True)
        continueRoutine &= rating.noResponse  # a response ends the trial
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in QnRatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "QnRating"-------
    for thisComponent in QnRatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice.addData('text.started', text.tStartRefresh)
    Practice.addData('text.stopped', text.tStopRefresh)
    Practice.addData('constantText_Qn.started', constantText_Qn.tStartRefresh)
    Practice.addData('constantText_Qn.stopped', constantText_Qn.tStopRefresh)
    # store data for Practice (TrialHandler)
    Practice.addData('rating.response', rating.getRating())
    Practice.addData('rating.rt', rating.getRT())
    Practice.addData('rating.started', rating.tStart)
    Practice.addData('rating.stopped', rating.tStop)
    # the Routine "QnRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'Practice'

# get names of stimulus parameters
if Practice.trialList in ([], [None], None):
    params = []
else:
    params = Practice.trialList[0].keys()
# save data for this loop
Practice.saveAsExcel(filename + '.xlsx', sheetName='Practice',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
Practice.saveAsText(filename + 'Practice.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "ActualRun"-------
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
# keep track of which components have finished
ActualRunComponents = [ActualR_text, key_resp_5]
for thisComponent in ActualRunComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ActualRunClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "ActualRun"-------
while continueRoutine:
    # get current time
    t = ActualRunClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ActualRunClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ActualR_text* updates
    if ActualR_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ActualR_text.frameNStart = frameN  # exact frame index
        ActualR_text.tStart = t  # local t and not account for scr refresh
        ActualR_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ActualR_text, 'tStartRefresh')  # time at next scr refresh
        ActualR_text.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if key_resp_5.keys == []:  # then this was the first keypress
                key_resp_5.keys = theseKeys.name  # just the first key pressed
                key_resp_5.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ActualRunComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ActualRun"-------
for thisComponent in ActualRunComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ActualR_text.started', ActualR_text.tStartRefresh)
thisExp.addData('ActualR_text.stopped', ActualR_text.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "ActualRun" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
BlockSequence1 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('NFN_odd.xlsx'),
    seed=None, name='BlockSequence1')
thisExp.addLoop(BlockSequence1)  # add the loop to the experiment
thisBlockSequence1 = BlockSequence1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockSequence1.rgb)
if thisBlockSequence1 != None:
    for paramName in thisBlockSequence1:
        exec('{} = thisBlockSequence1[paramName]'.format(paramName))

for thisBlockSequence1 in BlockSequence1:
    currentLoop = BlockSequence1
    # abbreviate parameter names if possible (e.g. rgb = thisBlockSequence1.rgb)
    if thisBlockSequence1 != None:
        for paramName in thisBlockSequence1:
            exec('{} = thisBlockSequence1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction_I"-------
    # update component parameters for each repeat
    InstructionText2.setColor(textColor, colorSpace='rgb')
    InstructionText2.setText(Instruction_I)
    instruction_response.keys = []
    instruction_response.rt = []
    # keep track of which components have finished
    Instruction_IComponents = [InstructionText2, instruction_response, constantText]
    for thisComponent in Instruction_IComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instruction_IClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Instruction_I"-------
    while continueRoutine:
        # get current time
        t = Instruction_IClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instruction_IClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionText2* updates
        if InstructionText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionText2.frameNStart = frameN  # exact frame index
            InstructionText2.tStart = t  # local t and not account for scr refresh
            InstructionText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionText2, 'tStartRefresh')  # time at next scr refresh
            InstructionText2.setAutoDraw(True)
        
        # *instruction_response* updates
        waitOnFlip = False
        if instruction_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_response.frameNStart = frameN  # exact frame index
            instruction_response.tStart = t  # local t and not account for scr refresh
            instruction_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_response, 'tStartRefresh')  # time at next scr refresh
            instruction_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instruction_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_response.status == STARTED and not waitOnFlip:
            theseKeys = instruction_response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *constantText* updates
        if constantText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            constantText.frameNStart = frameN  # exact frame index
            constantText.tStart = t  # local t and not account for scr refresh
            constantText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(constantText, 'tStartRefresh')  # time at next scr refresh
            constantText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction_I"-------
    for thisComponent in Instruction_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BlockSequence1.addData('InstructionText2.started', InstructionText2.tStartRefresh)
    BlockSequence1.addData('InstructionText2.stopped', InstructionText2.tStopRefresh)
    BlockSequence1.addData('constantText.started', constantText.tStartRefresh)
    BlockSequence1.addData('constantText.stopped', constantText.tStopRefresh)
    # the Routine "Instruction_I" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Resp_Instruction"-------
    # update component parameters for each repeat
    changing_text.setColor(textColor, colorSpace='rgb')
    changing_text.setText(Instruction_I)
    changing_text_2.setColor(textColor, colorSpace='rgb')
    changing_text_2.setText(Instruction2
)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    Resp_InstructionComponents = [changing_text, changing_text_2, Constant_text, key_resp_2]
    for thisComponent in Resp_InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Resp_InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Resp_Instruction"-------
    while continueRoutine:
        # get current time
        t = Resp_InstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Resp_InstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *changing_text* updates
        if changing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            changing_text.frameNStart = frameN  # exact frame index
            changing_text.tStart = t  # local t and not account for scr refresh
            changing_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changing_text, 'tStartRefresh')  # time at next scr refresh
            changing_text.setAutoDraw(True)
        
        # *changing_text_2* updates
        if changing_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            changing_text_2.frameNStart = frameN  # exact frame index
            changing_text_2.tStart = t  # local t and not account for scr refresh
            changing_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changing_text_2, 'tStartRefresh')  # time at next scr refresh
            changing_text_2.setAutoDraw(True)
        
        # *Constant_text* updates
        if Constant_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Constant_text.frameNStart = frameN  # exact frame index
            Constant_text.tStart = t  # local t and not account for scr refresh
            Constant_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Constant_text, 'tStartRefresh')  # time at next scr refresh
            Constant_text.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Resp_InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Resp_Instruction"-------
    for thisComponent in Resp_InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BlockSequence1.addData('changing_text.started', changing_text.tStartRefresh)
    BlockSequence1.addData('changing_text.stopped', changing_text.tStopRefresh)
    BlockSequence1.addData('changing_text_2.started', changing_text_2.tStartRefresh)
    BlockSequence1.addData('changing_text_2.stopped', changing_text_2.tStopRefresh)
    BlockSequence1.addData('Constant_text.started', Constant_text.tStartRefresh)
    BlockSequence1.addData('Constant_text.stopped', Constant_text.tStopRefresh)
    # the Routine "Resp_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Single_Block = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Qn_NFN.xlsx', selection=str(thisBlock)+":"+str(thisBlock+5)),
        seed=None, name='Single_Block')
    thisExp.addLoop(Single_Block)  # add the loop to the experiment
    thisSingle_Block = Single_Block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSingle_Block.rgb)
    if thisSingle_Block != None:
        for paramName in thisSingle_Block:
            exec('{} = thisSingle_Block[paramName]'.format(paramName))
    
    for thisSingle_Block in Single_Block:
        currentLoop = Single_Block
        # abbreviate parameter names if possible (e.g. rgb = thisSingle_Block.rgb)
        if thisSingle_Block != None:
            for paramName in thisSingle_Block:
                exec('{} = thisSingle_Block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "BlockStopper"-------
        # update component parameters for each repeat
        thisBlock+=1
        if thisBlock%5==0:
            Single_Block.finished=1
        # keep track of which components have finished
        BlockStopperComponents = []
        for thisComponent in BlockStopperComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlockStopperClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "BlockStopper"-------
        while continueRoutine:
            # get current time
            t = BlockStopperClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlockStopperClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlockStopperComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BlockStopper"-------
        for thisComponent in BlockStopperComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "BlockStopper" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        Reps_10 = data.TrialHandler(nReps=10, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('AsianTrials2.xlsx', selection=str(thisLoop)+":"+str(thisLoop+10)),
            seed=None, name='Reps_10')
        thisExp.addLoop(Reps_10)  # add the loop to the experiment
        thisRep_10 = Reps_10.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRep_10.rgb)
        if thisRep_10 != None:
            for paramName in thisRep_10:
                exec('{} = thisRep_10[paramName]'.format(paramName))
        
        for thisRep_10 in Reps_10:
            currentLoop = Reps_10
            # abbreviate parameter names if possible (e.g. rgb = thisRep_10.rgb)
            if thisRep_10 != None:
                for paramName in thisRep_10:
                    exec('{} = thisRep_10[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial"-------
            routineTimer.add(4.000000)
            # update component parameters for each repeat
            thisLoop +=1
            if thisLoop%10==0:
                Reps_10.finished=1
            StimImage.contrast = Contrast
            
            StimImage.setImage(StimImageFile)
            import random
            WhiteDuration = random.uniform(3,4)
            thisExp.addData('White_random_duration', WhiteDuration)
            Trial_KeyResp.keys = []
            Trial_KeyResp.rt = []
            maskbefore2.contrast = Contrast
            maskbefore2.setImage(Masks)
            maskafter2.contrast = Contrast
            maskafter2.setImage(Masks)
            # keep track of which components have finished
            trialComponents = [PurpleFixation, StimImage, WhiteFixation, Trial_KeyResp, maskbefore2, maskafter2]
            for thisComponent in trialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "trial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PurpleFixation* updates
                if PurpleFixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    PurpleFixation.frameNStart = frameN  # exact frame index
                    PurpleFixation.tStart = t  # local t and not account for scr refresh
                    PurpleFixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PurpleFixation, 'tStartRefresh')  # time at next scr refresh
                    PurpleFixation.setAutoDraw(True)
                if PurpleFixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PurpleFixation.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        PurpleFixation.tStop = t  # not accounting for scr refresh
                        PurpleFixation.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PurpleFixation, 'tStopRefresh')  # time at next scr refresh
                        PurpleFixation.setAutoDraw(False)
                
                # *StimImage* updates
                if StimImage.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    StimImage.frameNStart = frameN  # exact frame index
                    StimImage.tStart = t  # local t and not account for scr refresh
                    StimImage.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(StimImage, 'tStartRefresh')  # time at next scr refresh
                    StimImage.setAutoDraw(True)
                if StimImage.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > StimImage.tStartRefresh + 0.1-frameTolerance:
                        # keep track of stop time/frame for later
                        StimImage.tStop = t  # not accounting for scr refresh
                        StimImage.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(StimImage, 'tStopRefresh')  # time at next scr refresh
                        StimImage.setAutoDraw(False)
                
                # *WhiteFixation* updates
                if WhiteFixation.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                    # keep track of start time/frame for later
                    WhiteFixation.frameNStart = frameN  # exact frame index
                    WhiteFixation.tStart = t  # local t and not account for scr refresh
                    WhiteFixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(WhiteFixation, 'tStartRefresh')  # time at next scr refresh
                    WhiteFixation.setAutoDraw(True)
                if WhiteFixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > WhiteFixation.tStartRefresh + 2.8-frameTolerance:
                        # keep track of stop time/frame for later
                        WhiteFixation.tStop = t  # not accounting for scr refresh
                        WhiteFixation.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(WhiteFixation, 'tStopRefresh')  # time at next scr refresh
                        WhiteFixation.setAutoDraw(False)
                
                # *Trial_KeyResp* updates
                waitOnFlip = False
                if Trial_KeyResp.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    Trial_KeyResp.frameNStart = frameN  # exact frame index
                    Trial_KeyResp.tStart = t  # local t and not account for scr refresh
                    Trial_KeyResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Trial_KeyResp, 'tStartRefresh')  # time at next scr refresh
                    Trial_KeyResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Trial_KeyResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Trial_KeyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Trial_KeyResp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Trial_KeyResp.tStartRefresh + 3.2-frameTolerance:
                        # keep track of stop time/frame for later
                        Trial_KeyResp.tStop = t  # not accounting for scr refresh
                        Trial_KeyResp.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Trial_KeyResp, 'tStopRefresh')  # time at next scr refresh
                        Trial_KeyResp.status = FINISHED
                if Trial_KeyResp.status == STARTED and not waitOnFlip:
                    theseKeys = Trial_KeyResp.getKeys(keyList=['v', 'b'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        if Trial_KeyResp.keys == []:  # then this was the first keypress
                            Trial_KeyResp.keys = theseKeys.name  # just the first key pressed
                            Trial_KeyResp.rt = theseKeys.rt
                            # was this 'correct'?
                            if (Trial_KeyResp.keys == str(CorrectResp)) or (Trial_KeyResp.keys == CorrectResp):
                                Trial_KeyResp.corr = 1
                            else:
                                Trial_KeyResp.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *maskbefore2* updates
                if maskbefore2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    maskbefore2.frameNStart = frameN  # exact frame index
                    maskbefore2.tStart = t  # local t and not account for scr refresh
                    maskbefore2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(maskbefore2, 'tStartRefresh')  # time at next scr refresh
                    maskbefore2.setAutoDraw(True)
                if maskbefore2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > maskbefore2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        maskbefore2.tStop = t  # not accounting for scr refresh
                        maskbefore2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(maskbefore2, 'tStopRefresh')  # time at next scr refresh
                        maskbefore2.setAutoDraw(False)
                
                # *maskafter2* updates
                if maskafter2.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                    # keep track of start time/frame for later
                    maskafter2.frameNStart = frameN  # exact frame index
                    maskafter2.tStart = t  # local t and not account for scr refresh
                    maskafter2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(maskafter2, 'tStartRefresh')  # time at next scr refresh
                    maskafter2.setAutoDraw(True)
                if maskafter2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > maskafter2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        maskafter2.tStop = t  # not accounting for scr refresh
                        maskafter2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(maskafter2, 'tStopRefresh')  # time at next scr refresh
                        maskafter2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Reps_10.addData('PurpleFixation.started', PurpleFixation.tStartRefresh)
            Reps_10.addData('PurpleFixation.stopped', PurpleFixation.tStopRefresh)
            Reps_10.addData('StimImage.started', StimImage.tStartRefresh)
            Reps_10.addData('StimImage.stopped', StimImage.tStopRefresh)
            Reps_10.addData('WhiteFixation.started', WhiteFixation.tStartRefresh)
            Reps_10.addData('WhiteFixation.stopped', WhiteFixation.tStopRefresh)
            # check responses
            if Trial_KeyResp.keys in ['', [], None]:  # No response was made
                Trial_KeyResp.keys = None
                # was no response the correct answer?!
                if str(CorrectResp).lower() == 'none':
                   Trial_KeyResp.corr = 1;  # correct non-response
                else:
                   Trial_KeyResp.corr = 0;  # failed to respond (incorrectly)
            # store data for Reps_10 (TrialHandler)
            Reps_10.addData('Trial_KeyResp.keys',Trial_KeyResp.keys)
            Reps_10.addData('Trial_KeyResp.corr', Trial_KeyResp.corr)
            if Trial_KeyResp.keys != None:  # we had a response
                Reps_10.addData('Trial_KeyResp.rt', Trial_KeyResp.rt)
            Reps_10.addData('Trial_KeyResp.started', Trial_KeyResp.tStartRefresh)
            Reps_10.addData('Trial_KeyResp.stopped', Trial_KeyResp.tStopRefresh)
            Reps_10.addData('maskbefore2.started', maskbefore2.tStartRefresh)
            Reps_10.addData('maskbefore2.stopped', maskbefore2.tStopRefresh)
            Reps_10.addData('maskafter2.started', maskafter2.tStartRefresh)
            Reps_10.addData('maskafter2.stopped', maskafter2.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 10 repeats of 'Reps_10'
        
        # get names of stimulus parameters
        if Reps_10.trialList in ([], [None], None):
            params = []
        else:
            params = Reps_10.trialList[0].keys()
        # save data for this loop
        Reps_10.saveAsExcel(filename + '.xlsx', sheetName='Reps_10',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Reps_10.saveAsText(filename + 'Reps_10.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "QnRating"-------
        # update component parameters for each repeat
        text.setColor(Color, colorSpace='rgb')
        text.setText(Questionnaire)
        rating.reset()
        # keep track of which components have finished
        QnRatingComponents = [text, constantText_Qn, rating]
        for thisComponent in QnRatingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        QnRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "QnRating"-------
        while continueRoutine:
            # get current time
            t = QnRatingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=QnRatingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *constantText_Qn* updates
            if constantText_Qn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                constantText_Qn.frameNStart = frameN  # exact frame index
                constantText_Qn.tStart = t  # local t and not account for scr refresh
                constantText_Qn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(constantText_Qn, 'tStartRefresh')  # time at next scr refresh
                constantText_Qn.setAutoDraw(True)
            # *rating* updates
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating.frameNStart = frameN  # exact frame index
                rating.tStart = t  # local t and not account for scr refresh
                rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
                rating.setAutoDraw(True)
            continueRoutine &= rating.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QnRatingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "QnRating"-------
        for thisComponent in QnRatingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Single_Block.addData('text.started', text.tStartRefresh)
        Single_Block.addData('text.stopped', text.tStopRefresh)
        Single_Block.addData('constantText_Qn.started', constantText_Qn.tStartRefresh)
        Single_Block.addData('constantText_Qn.stopped', constantText_Qn.tStopRefresh)
        # store data for Single_Block (TrialHandler)
        Single_Block.addData('rating.response', rating.getRating())
        Single_Block.addData('rating.rt', rating.getRT())
        Single_Block.addData('rating.started', rating.tStart)
        Single_Block.addData('rating.stopped', rating.tStop)
        # the Routine "QnRating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5 repeats of 'Single_Block'
    
    # get names of stimulus parameters
    if Single_Block.trialList in ([], [None], None):
        params = []
    else:
        params = Single_Block.trialList[0].keys()
    # save data for this loop
    Single_Block.saveAsExcel(filename + '.xlsx', sheetName='Single_Block',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    Single_Block.saveAsText(filename + 'Single_Block.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'BlockSequence1'

# get names of stimulus parameters
if BlockSequence1.trialList in ([], [None], None):
    params = []
else:
    params = BlockSequence1.trialList[0].keys()
# save data for this loop
BlockSequence1.saveAsExcel(filename + '.xlsx', sheetName='BlockSequence1',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
BlockSequence1.saveAsText(filename + 'BlockSequence1.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "short_break"-------
# update component parameters for each repeat
end_break.keys = []
end_break.rt = []
# keep track of which components have finished
short_breakComponents = [break_screen, end_break]
for thisComponent in short_breakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
short_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "short_break"-------
while continueRoutine:
    # get current time
    t = short_breakClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=short_breakClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break_screen* updates
    if break_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break_screen.frameNStart = frameN  # exact frame index
        break_screen.tStart = t  # local t and not account for scr refresh
        break_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_screen, 'tStartRefresh')  # time at next scr refresh
        break_screen.setAutoDraw(True)
    
    # *end_break* updates
    waitOnFlip = False
    if end_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_break.frameNStart = frameN  # exact frame index
        end_break.tStart = t  # local t and not account for scr refresh
        end_break.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_break, 'tStartRefresh')  # time at next scr refresh
        end_break.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_break.status == STARTED and not waitOnFlip:
        theseKeys = end_break.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in short_breakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "short_break"-------
for thisComponent in short_breakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('break_screen.started', break_screen.tStartRefresh)
thisExp.addData('break_screen.stopped', break_screen.tStopRefresh)
# the Routine "short_break" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
BlockSequence2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FNF_odd.xlsx'),
    seed=None, name='BlockSequence2')
thisExp.addLoop(BlockSequence2)  # add the loop to the experiment
thisBlockSequence2 = BlockSequence2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockSequence2.rgb)
if thisBlockSequence2 != None:
    for paramName in thisBlockSequence2:
        exec('{} = thisBlockSequence2[paramName]'.format(paramName))

for thisBlockSequence2 in BlockSequence2:
    currentLoop = BlockSequence2
    # abbreviate parameter names if possible (e.g. rgb = thisBlockSequence2.rgb)
    if thisBlockSequence2 != None:
        for paramName in thisBlockSequence2:
            exec('{} = thisBlockSequence2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction_I"-------
    # update component parameters for each repeat
    InstructionText2.setColor(textColor, colorSpace='rgb')
    InstructionText2.setText(Instruction_I)
    instruction_response.keys = []
    instruction_response.rt = []
    # keep track of which components have finished
    Instruction_IComponents = [InstructionText2, instruction_response, constantText]
    for thisComponent in Instruction_IComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Instruction_IClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Instruction_I"-------
    while continueRoutine:
        # get current time
        t = Instruction_IClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Instruction_IClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionText2* updates
        if InstructionText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionText2.frameNStart = frameN  # exact frame index
            InstructionText2.tStart = t  # local t and not account for scr refresh
            InstructionText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionText2, 'tStartRefresh')  # time at next scr refresh
            InstructionText2.setAutoDraw(True)
        
        # *instruction_response* updates
        waitOnFlip = False
        if instruction_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_response.frameNStart = frameN  # exact frame index
            instruction_response.tStart = t  # local t and not account for scr refresh
            instruction_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_response, 'tStartRefresh')  # time at next scr refresh
            instruction_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instruction_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruction_response.status == STARTED and not waitOnFlip:
            theseKeys = instruction_response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # *constantText* updates
        if constantText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            constantText.frameNStart = frameN  # exact frame index
            constantText.tStart = t  # local t and not account for scr refresh
            constantText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(constantText, 'tStartRefresh')  # time at next scr refresh
            constantText.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction_IComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction_I"-------
    for thisComponent in Instruction_IComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BlockSequence2.addData('InstructionText2.started', InstructionText2.tStartRefresh)
    BlockSequence2.addData('InstructionText2.stopped', InstructionText2.tStopRefresh)
    BlockSequence2.addData('constantText.started', constantText.tStartRefresh)
    BlockSequence2.addData('constantText.stopped', constantText.tStopRefresh)
    # the Routine "Instruction_I" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Resp_Instruction"-------
    # update component parameters for each repeat
    changing_text.setColor(textColor, colorSpace='rgb')
    changing_text.setText(Instruction_I)
    changing_text_2.setColor(textColor, colorSpace='rgb')
    changing_text_2.setText(Instruction2
)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    Resp_InstructionComponents = [changing_text, changing_text_2, Constant_text, key_resp_2]
    for thisComponent in Resp_InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Resp_InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Resp_Instruction"-------
    while continueRoutine:
        # get current time
        t = Resp_InstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Resp_InstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *changing_text* updates
        if changing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            changing_text.frameNStart = frameN  # exact frame index
            changing_text.tStart = t  # local t and not account for scr refresh
            changing_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changing_text, 'tStartRefresh')  # time at next scr refresh
            changing_text.setAutoDraw(True)
        
        # *changing_text_2* updates
        if changing_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            changing_text_2.frameNStart = frameN  # exact frame index
            changing_text_2.tStart = t  # local t and not account for scr refresh
            changing_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(changing_text_2, 'tStartRefresh')  # time at next scr refresh
            changing_text_2.setAutoDraw(True)
        
        # *Constant_text* updates
        if Constant_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Constant_text.frameNStart = frameN  # exact frame index
            Constant_text.tStart = t  # local t and not account for scr refresh
            Constant_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Constant_text, 'tStartRefresh')  # time at next scr refresh
            Constant_text.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Resp_InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Resp_Instruction"-------
    for thisComponent in Resp_InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BlockSequence2.addData('changing_text.started', changing_text.tStartRefresh)
    BlockSequence2.addData('changing_text.stopped', changing_text.tStopRefresh)
    BlockSequence2.addData('changing_text_2.started', changing_text_2.tStartRefresh)
    BlockSequence2.addData('changing_text_2.stopped', changing_text_2.tStopRefresh)
    BlockSequence2.addData('Constant_text.started', Constant_text.tStartRefresh)
    BlockSequence2.addData('Constant_text.stopped', Constant_text.tStopRefresh)
    # the Routine "Resp_Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Single_Blockb = data.TrialHandler(nReps=5, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Qn_FNF.xlsx', selection=str(thisBlockb)+":"+str(thisBlockb+5)),
        seed=None, name='Single_Blockb')
    thisExp.addLoop(Single_Blockb)  # add the loop to the experiment
    thisSingle_Blockb = Single_Blockb.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSingle_Blockb.rgb)
    if thisSingle_Blockb != None:
        for paramName in thisSingle_Blockb:
            exec('{} = thisSingle_Blockb[paramName]'.format(paramName))
    
    for thisSingle_Blockb in Single_Blockb:
        currentLoop = Single_Blockb
        # abbreviate parameter names if possible (e.g. rgb = thisSingle_Blockb.rgb)
        if thisSingle_Blockb != None:
            for paramName in thisSingle_Blockb:
                exec('{} = thisSingle_Blockb[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "BlockStopperb"-------
        # update component parameters for each repeat
        thisBlockb+=1
        if thisBlockb%5==0:
            Single_Blockb.finished=1
        # keep track of which components have finished
        BlockStopperbComponents = []
        for thisComponent in BlockStopperbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlockStopperbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "BlockStopperb"-------
        while continueRoutine:
            # get current time
            t = BlockStopperbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlockStopperbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlockStopperbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BlockStopperb"-------
        for thisComponent in BlockStopperbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "BlockStopperb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        Reps_10b = data.TrialHandler(nReps=10, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('AsianTrials1.xlsx', selection=str(thisLoopb)+":"+str(thisLoopb+10)),
            seed=None, name='Reps_10b')
        thisExp.addLoop(Reps_10b)  # add the loop to the experiment
        thisReps_10b = Reps_10b.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisReps_10b.rgb)
        if thisReps_10b != None:
            for paramName in thisReps_10b:
                exec('{} = thisReps_10b[paramName]'.format(paramName))
        
        for thisReps_10b in Reps_10b:
            currentLoop = Reps_10b
            # abbreviate parameter names if possible (e.g. rgb = thisReps_10b.rgb)
            if thisReps_10b != None:
                for paramName in thisReps_10b:
                    exec('{} = thisReps_10b[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trialb"-------
            routineTimer.add(4.000000)
            # update component parameters for each repeat
            thisLoopb +=1
            if thisLoopb%10==0:
                Reps_10b.finished=1
            StimImageb.contrast = Contrast
            
            StimImageb.setImage(StimImageFile)
            import random
            WhiteDurationb = random.uniform(3,4)
            thisExp.addData('White_random_duration', WhiteDurationb)
            Trial_KeyRespb.keys = []
            Trial_KeyRespb.rt = []
            maskbeforeb.contrast = Contrast
            maskbeforeb.setImage(Masks)
            maskafterb.contrast = Contrast
            maskafterb.setImage(Masks)
            # keep track of which components have finished
            trialbComponents = [PurpleFixationb, StimImageb, WhiteFixationb, Trial_KeyRespb, maskbeforeb, maskafterb]
            for thisComponent in trialbComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trialbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            continueRoutine = True
            
            # -------Run Routine "trialb"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialbClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trialbClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *PurpleFixationb* updates
                if PurpleFixationb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    PurpleFixationb.frameNStart = frameN  # exact frame index
                    PurpleFixationb.tStart = t  # local t and not account for scr refresh
                    PurpleFixationb.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(PurpleFixationb, 'tStartRefresh')  # time at next scr refresh
                    PurpleFixationb.setAutoDraw(True)
                if PurpleFixationb.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > PurpleFixationb.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        PurpleFixationb.tStop = t  # not accounting for scr refresh
                        PurpleFixationb.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(PurpleFixationb, 'tStopRefresh')  # time at next scr refresh
                        PurpleFixationb.setAutoDraw(False)
                
                # *StimImageb* updates
                if StimImageb.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    StimImageb.frameNStart = frameN  # exact frame index
                    StimImageb.tStart = t  # local t and not account for scr refresh
                    StimImageb.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(StimImageb, 'tStartRefresh')  # time at next scr refresh
                    StimImageb.setAutoDraw(True)
                if StimImageb.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > StimImageb.tStartRefresh + 0.1-frameTolerance:
                        # keep track of stop time/frame for later
                        StimImageb.tStop = t  # not accounting for scr refresh
                        StimImageb.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(StimImageb, 'tStopRefresh')  # time at next scr refresh
                        StimImageb.setAutoDraw(False)
                
                # *WhiteFixationb* updates
                if WhiteFixationb.status == NOT_STARTED and tThisFlip >= 1.2-frameTolerance:
                    # keep track of start time/frame for later
                    WhiteFixationb.frameNStart = frameN  # exact frame index
                    WhiteFixationb.tStart = t  # local t and not account for scr refresh
                    WhiteFixationb.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(WhiteFixationb, 'tStartRefresh')  # time at next scr refresh
                    WhiteFixationb.setAutoDraw(True)
                if WhiteFixationb.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > WhiteFixationb.tStartRefresh + 2.8-frameTolerance:
                        # keep track of stop time/frame for later
                        WhiteFixationb.tStop = t  # not accounting for scr refresh
                        WhiteFixationb.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(WhiteFixationb, 'tStopRefresh')  # time at next scr refresh
                        WhiteFixationb.setAutoDraw(False)
                
                # *Trial_KeyRespb* updates
                waitOnFlip = False
                if Trial_KeyRespb.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    Trial_KeyRespb.frameNStart = frameN  # exact frame index
                    Trial_KeyRespb.tStart = t  # local t and not account for scr refresh
                    Trial_KeyRespb.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Trial_KeyRespb, 'tStartRefresh')  # time at next scr refresh
                    Trial_KeyRespb.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Trial_KeyRespb.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Trial_KeyRespb.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Trial_KeyRespb.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Trial_KeyRespb.tStartRefresh + 3.2-frameTolerance:
                        # keep track of stop time/frame for later
                        Trial_KeyRespb.tStop = t  # not accounting for scr refresh
                        Trial_KeyRespb.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Trial_KeyRespb, 'tStopRefresh')  # time at next scr refresh
                        Trial_KeyRespb.status = FINISHED
                if Trial_KeyRespb.status == STARTED and not waitOnFlip:
                    theseKeys = Trial_KeyRespb.getKeys(keyList=['v', 'b'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        if Trial_KeyRespb.keys == []:  # then this was the first keypress
                            Trial_KeyRespb.keys = theseKeys.name  # just the first key pressed
                            Trial_KeyRespb.rt = theseKeys.rt
                            # was this 'correct'?
                            if (Trial_KeyRespb.keys == str(CorrectResp)) or (Trial_KeyRespb.keys == CorrectResp):
                                Trial_KeyRespb.corr = 1
                            else:
                                Trial_KeyRespb.corr = 0
                            # a response ends the routine
                            continueRoutine = False
                
                # *maskbeforeb* updates
                if maskbeforeb.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    maskbeforeb.frameNStart = frameN  # exact frame index
                    maskbeforeb.tStart = t  # local t and not account for scr refresh
                    maskbeforeb.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(maskbeforeb, 'tStartRefresh')  # time at next scr refresh
                    maskbeforeb.setAutoDraw(True)
                if maskbeforeb.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > maskbeforeb.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        maskbeforeb.tStop = t  # not accounting for scr refresh
                        maskbeforeb.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(maskbeforeb, 'tStopRefresh')  # time at next scr refresh
                        maskbeforeb.setAutoDraw(False)
                
                # *maskafterb* updates
                if maskafterb.status == NOT_STARTED and tThisFlip >= 0.9-frameTolerance:
                    # keep track of start time/frame for later
                    maskafterb.frameNStart = frameN  # exact frame index
                    maskafterb.tStart = t  # local t and not account for scr refresh
                    maskafterb.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(maskafterb, 'tStartRefresh')  # time at next scr refresh
                    maskafterb.setAutoDraw(True)
                if maskafterb.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > maskafterb.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        maskafterb.tStop = t  # not accounting for scr refresh
                        maskafterb.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(maskafterb, 'tStopRefresh')  # time at next scr refresh
                        maskafterb.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialbComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trialb"-------
            for thisComponent in trialbComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            Reps_10b.addData('PurpleFixationb.started', PurpleFixationb.tStartRefresh)
            Reps_10b.addData('PurpleFixationb.stopped', PurpleFixationb.tStopRefresh)
            Reps_10b.addData('StimImageb.started', StimImageb.tStartRefresh)
            Reps_10b.addData('StimImageb.stopped', StimImageb.tStopRefresh)
            Reps_10b.addData('WhiteFixationb.started', WhiteFixationb.tStartRefresh)
            Reps_10b.addData('WhiteFixationb.stopped', WhiteFixationb.tStopRefresh)
            # check responses
            if Trial_KeyRespb.keys in ['', [], None]:  # No response was made
                Trial_KeyRespb.keys = None
                # was no response the correct answer?!
                if str(CorrectResp).lower() == 'none':
                   Trial_KeyRespb.corr = 1;  # correct non-response
                else:
                   Trial_KeyRespb.corr = 0;  # failed to respond (incorrectly)
            # store data for Reps_10b (TrialHandler)
            Reps_10b.addData('Trial_KeyRespb.keys',Trial_KeyRespb.keys)
            Reps_10b.addData('Trial_KeyRespb.corr', Trial_KeyRespb.corr)
            if Trial_KeyRespb.keys != None:  # we had a response
                Reps_10b.addData('Trial_KeyRespb.rt', Trial_KeyRespb.rt)
            Reps_10b.addData('Trial_KeyRespb.started', Trial_KeyRespb.tStartRefresh)
            Reps_10b.addData('Trial_KeyRespb.stopped', Trial_KeyRespb.tStopRefresh)
            Reps_10b.addData('maskbeforeb.started', maskbeforeb.tStartRefresh)
            Reps_10b.addData('maskbeforeb.stopped', maskbeforeb.tStopRefresh)
            Reps_10b.addData('maskafterb.started', maskafterb.tStartRefresh)
            Reps_10b.addData('maskafterb.stopped', maskafterb.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 10 repeats of 'Reps_10b'
        
        # get names of stimulus parameters
        if Reps_10b.trialList in ([], [None], None):
            params = []
        else:
            params = Reps_10b.trialList[0].keys()
        # save data for this loop
        Reps_10b.saveAsExcel(filename + '.xlsx', sheetName='Reps_10b',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        Reps_10b.saveAsText(filename + 'Reps_10b.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # ------Prepare to start Routine "QnRating"-------
        # update component parameters for each repeat
        text.setColor(Color, colorSpace='rgb')
        text.setText(Questionnaire)
        rating.reset()
        # keep track of which components have finished
        QnRatingComponents = [text, constantText_Qn, rating]
        for thisComponent in QnRatingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        QnRatingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "QnRating"-------
        while continueRoutine:
            # get current time
            t = QnRatingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=QnRatingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *constantText_Qn* updates
            if constantText_Qn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                constantText_Qn.frameNStart = frameN  # exact frame index
                constantText_Qn.tStart = t  # local t and not account for scr refresh
                constantText_Qn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(constantText_Qn, 'tStartRefresh')  # time at next scr refresh
                constantText_Qn.setAutoDraw(True)
            # *rating* updates
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating.frameNStart = frameN  # exact frame index
                rating.tStart = t  # local t and not account for scr refresh
                rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
                rating.setAutoDraw(True)
            continueRoutine &= rating.noResponse  # a response ends the trial
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QnRatingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "QnRating"-------
        for thisComponent in QnRatingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Single_Blockb.addData('text.started', text.tStartRefresh)
        Single_Blockb.addData('text.stopped', text.tStopRefresh)
        Single_Blockb.addData('constantText_Qn.started', constantText_Qn.tStartRefresh)
        Single_Blockb.addData('constantText_Qn.stopped', constantText_Qn.tStopRefresh)
        # store data for Single_Blockb (TrialHandler)
        Single_Blockb.addData('rating.response', rating.getRating())
        Single_Blockb.addData('rating.rt', rating.getRT())
        Single_Blockb.addData('rating.started', rating.tStart)
        Single_Blockb.addData('rating.stopped', rating.tStop)
        # the Routine "QnRating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 5 repeats of 'Single_Blockb'
    
    # get names of stimulus parameters
    if Single_Blockb.trialList in ([], [None], None):
        params = []
    else:
        params = Single_Blockb.trialList[0].keys()
    # save data for this loop
    Single_Blockb.saveAsExcel(filename + '.xlsx', sheetName='Single_Blockb',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    Single_Blockb.saveAsText(filename + 'Single_Blockb.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1 repeats of 'BlockSequence2'

# get names of stimulus parameters
if BlockSequence2.trialList in ([], [None], None):
    params = []
else:
    params = BlockSequence2.trialList[0].keys()
# save data for this loop
BlockSequence2.saveAsExcel(filename + '.xlsx', sheetName='BlockSequence2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
BlockSequence2.saveAsText(filename + 'BlockSequence2.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Exp_Ending"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
Exp_EndingComponents = [EndingMsg]
for thisComponent in Exp_EndingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Exp_EndingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Exp_Ending"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Exp_EndingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Exp_EndingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndingMsg* updates
    if EndingMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndingMsg.frameNStart = frameN  # exact frame index
        EndingMsg.tStart = t  # local t and not account for scr refresh
        EndingMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndingMsg, 'tStartRefresh')  # time at next scr refresh
        EndingMsg.setAutoDraw(True)
    if EndingMsg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndingMsg.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            EndingMsg.tStop = t  # not accounting for scr refresh
            EndingMsg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EndingMsg, 'tStopRefresh')  # time at next scr refresh
            EndingMsg.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Exp_EndingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Exp_Ending"-------
for thisComponent in Exp_EndingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndingMsg.started', EndingMsg.tStartRefresh)
thisExp.addData('EndingMsg.stopped', EndingMsg.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
