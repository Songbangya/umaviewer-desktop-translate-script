import time
import pyautogui
import tkinter as tk
from pyperclip import paste, copy
from tkinter import messagebox


def script_click():
    pyautogui.PAUSE = 0.02
    directory = "files/"
    bone_origin = ['Hip', 'Thigh_L', 'Knee_L', 'Ankle_L', 'Thigh_R', 'Knee_R', 'Ankle_R',
                'Spine', 'Chest', 'Head', 'Shoulder_L', 'Arm_L', 'Elbow_L', 'Wrist_L',
                   'Shoulder_R', 'Arm_R', 'Elbow_R', 'Wrist_R']
    bone_change = ["センター", "左足", "左ひざ", "左足首", "右足", "右ひざ", "右足首", "上半身",
                   "上半身2", "頭", "左肩", "左腕", "左ひじ", "左手首", "右肩", "右腕", "右ひじ", "右手首"]

    # 找到骨骼列表并点击
    try:
        position = pyautogui.locateOnScreen(directory+"firstbonename.png", confidence=0.9)
        bone_list_pos_x = position.left
        bone_list_pos_y = position.top
        pyautogui.click(bone_list_pos_x, bone_list_pos_y)
    except pyautogui.ImageNotFoundException:
        messagebox.showinfo("warn", "please make sure that pmxeditor switches to the bone interface and is displayed completely on the screen")

    # 找到修改骨骼名称处
    position = pyautogui.locateOnScreen(directory+"bonename.png", confidence=0.9)
    bone_name_pos_x = position.left + 90
    bone_name_pos_y = position.top + 10

    num = 0
    bone_num = 0
    origin_value = bone_origin[0]
    while True:
        num += 1
        # 前20轮循环，骨骼列表一直在向下走
        if num <= 20:
            bone_list_pos_y += 12
            pyautogui.click(bone_list_pos_x, bone_list_pos_y)
        # 之后的骨骼列表不动，只需回原位按down键
        else:
            pyautogui.click(bone_list_pos_x, bone_list_pos_y)
            pyautogui.press("down")
        # 去修改骨骼名称处  复制并回传骨骼名称
        pyautogui.click(bone_name_pos_x, bone_name_pos_y)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
        text = paste()
        # 检测如果需要修改，修改
        if text == origin_value:
            value = bone_change[bone_num]
            print(text, value)
            copy(value)
            time.sleep(0.5)
            pyautogui.hotkey("ctrl", "v")
            if text == "Wrist_R":
                break
            bone_num += 1
            origin_value = bone_origin[bone_num]


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Script")
    root.geometry("300x100")

    button = tk.Button(root, text="click here to start", command=script_click)
    button.place(x=80, y=30)

    root.mainloop()