import pyautogui as p
import time

p.keyDown('win')
p.press('q')
p.keyUp('win')

p.typewrite('google chrome')

time.sleep(1.0)

p.press('enter')

# p.press('win')

time.sleep(1.0)

p.keyDown('alt')
p.press('space')
p.keyUp('alt')

time.sleep(2.0)

p.press('x')

time.sleep(2.0)

p.typewrite('gmail.com')

p.press('Enter')

time.sleep(12.0)


# print(p.position())
p.click(x=57, y=374)

time.sleep(5.0)

p.typewrite('rejin.jacob@onmyowntechnology.com')

time.sleep(5.0)

p.press('Tab')

time.sleep(5.0)

p.press('Tab')

time.sleep(5.0)

p.press('Tab')

time.sleep(5.0)

p.typewrite('Hi sir. This is my HW')

time.sleep(5.0)

p.keyDown('Ctrl')
p.press('Enter')
p.keyUp('Ctrl')


