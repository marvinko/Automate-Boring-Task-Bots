#! python3
import pyautogui
import time

for x in pyautogui.KEYBOARD_KEYS:
	print(x)

def clicksearch():
	search_button = pyautogui.locateCenterOnScreen('search_button.png')
	pyautogui.click(search_button)

def resetwindow():
	pyautogui.hotkey('win','tab')
	pyautogui.hotkey('win','tab')

def search(*keys):
	search_clicked = False
	while not search_clicked:
		try:
			clicksearch()
			search_clicked = True
		except Exception as e:
			resetwindow()
	else:
		pyautogui.hotkey(*keys)
		pyautogui.press('enter')


if __name__ == '__main__':
	search('s','e','r','v','e','r')
	


# win_button = pyautogui.locateCenterOnScreen('win_button.png')
# pyautogui.click(win_button)
# soundserver_button = pyautogui.locateCenterOnScreen('soundserver.png')
# pyautogui.click(soundserver_button)
