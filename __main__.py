import win32api, win32con
import time
import os

VK_CODE = {
       'c':0x43,
       'v':0x56,
       'left_control':0xA2,
}
#left_control + c, left_control + v
def press():
    '''
    one press, one release.
    accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
    '''
    click(a_x,a_y)
    time.sleep(0.05)
    click(a_x,a_y)

    win32api.keybd_event(VK_CODE['left_control'], 0,0,0)
    win32api.keybd_event(VK_CODE['c'], 0,0,0)

    time.sleep(0.5)
    win32api.keybd_event(VK_CODE['left_control'],0 ,win32con.KEYEVENTF_KEYUP ,0)
    win32api.keybd_event(VK_CODE['c'],0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(0.5)

    click(b_x,b_y)

    win32api.keybd_event(VK_CODE['left_control'], 0,0,0)
    win32api.keybd_event(VK_CODE['v'], 0,0,0)

    time.sleep(0.5)
    win32api.keybd_event(VK_CODE['left_control'],0 ,win32con.KEYEVENTF_KEYUP ,0)
    win32api.keybd_event(VK_CODE['v'],0 ,win32con.KEYEVENTF_KEYUP ,0)
    click(c_x,c_y)
    time.sleep(1)


def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def find_location():
    while 1:
        mouse_p = win32api.GetCursorPos()
        print(mouse_p[0],mouse_p[1])
        os.system('cls')
        if mouse_p[0] == 0 and mouse_p[1] == 0:
            break;

time.sleep(1)

a_x = 223
a_y = 225
b_x = 307
b_y = 225
c_x = 192
c_y = 290
d_x = 423
d_y = 936

find_location()

while 1:
    for i in range(20):
        click(d_x,d_y)
        time.sleep(1.5)
        mouse_p = win32api.GetCursorPos()
        if mouse_p[0] == 0 and mouse_p[1] == 0:
            break;
    if mouse_p[0] == 0 and mouse_p[1] == 0:
        break;
    press()
