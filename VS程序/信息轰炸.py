from pynput.keyboard import Key,Controller
import time
keyboard=Controller()
messages=input("请输入信息：")
times=int(input("请输入次数："))
print("数据已被后台接受，请将光标移动至目标对话框...")
time.sleep(1)
for i in range(11):
    print("距离信息轰炸还需要%d秒"%(10-i))
    time.sleep(1)
for i in range(times):
    keyboard.type(messages)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.01)
print("信息轰炸顺利完成，已退出！")