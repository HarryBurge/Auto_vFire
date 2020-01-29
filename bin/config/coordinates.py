'''
This is where when any script needs to execute a command into vFire it will
need to be able to actually know where to click. This is what this file is for.

Please change coordinates for desired outcome.
'''

__author__ = 'Harry Burge'
__date__ = '29/01/2020'

# Imports
import pyautogui, time

# --Actual code--

def find_coords(list):
    '''
    params:-
        [str, ...] : List of actions that need coords
    returns:-
        [(float,float), ...] : Corresponding coords
    '''
    coords = []

    for i in list:
        if i == "Admin": coords.append((36,75))
        elif i == "Admin-Arrow": coords.append((73,75))

        elif i == "SysAdmin" : coords.append((110, 75))

        elif i == "WorkflowTemplate" : coords.append((166, 75))

        elif i == "CallTemplate" : coords.append((255, 75))

        elif i == "Designer" : coords.append((281, 75))
        elif i == "Designer-FindScreen" : coords.append((47,187))
        elif i == "Designer-ViewScreen" : coords.append((142, 187))
        elif i == "Designer-Skins" : coords.append((213, 187))

        elif i == "CMDBItems" : coords.append((340, 75))

        elif i == "Search" : coords.append((398, 75))
        elif i == "Search-Arrow" : coords.append((435, 75))


    return coords


def find_img_coords(list):
    coords = []

    for i in list:
        if i == "Admin" : coords.append(pyautogui.center(pyautogui.locateOnScreen('imgs/Admin.PNG')))

    return coords

print(pyautogui.center(pyautogui.locateOnScreen('imgs/Admin.PNG')))
print(find_img_coords(["Admin"]))
