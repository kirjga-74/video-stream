""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'stream_menu_panel | {user_id}'),
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data=f'set_close'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
#		python code
#		script_name: Game_Intro.py
#
#		author: 101Computing
#		description: Background music for intro 
#

from earsketch import *

init()
setTempo(120)

clip1 = EIGHT_BIT_ATARI_SFX_004
clip2 = EIGHT_BIT_ATARI_LEAD_011
clip3 = EIGHT_BIT_ATARI_LEAD_010

pointA = 1.75
repeat = 3
pointD = pointA + repeat 

#fitMedia(Clip,Track,StartMeasure,EndMeasure)
fitMedia(clip1,1,1,2)
for i in range(0,repeat):
  fitMedia(clip2,2,pointA + i,pointA + i + 1)

fitMedia(clip3,3,pointA,pointD + 1)

#setEffect(Track,effect,parmeter,value)
setEffect(3, VOLUME, GAIN, -10)

#setEffect(Track,effect,parmeter,value,start measure,value,end measure)
#Fade in
setEffect(1, VOLUME, GAIN, -40, 1, 0, 1.75)
#Delay Effect
setEffect(1, DELAY, DELAY_TIME, 250)
setEffect(2, DELAY, DELAY_TIME, 250)
#Fade Out
setEffect(3, VOLUME, GAIN, -10, pointD, -60, pointD+1)

finish() 
     
      InlineKeyboardButton(text="🎶", callback_data=f'setEffect | {user_id}'),
      InlineKeyboardButton(text="⏹", callback_data=f'set_stop | {user_id}'),
      InlineKeyboardButton(text="⏸", callback_data=f'set_pause | {user_id}'),
      InlineKeyboardButton(text="▶️", callback_data=f'set_resume | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔇", callback_data=f'set_mute | {user_id}'),
      InlineKeyboardButton(text="🔊", callback_data=f'set_unmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="🔙 Go Back", callback_data='stream_home_panel'),
    ]
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="set_close"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="stream_menu_panel"
      )
    ]
  ]
)
