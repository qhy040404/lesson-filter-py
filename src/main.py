import json
import sys
from tkinter import *
from tkinter import messagebox

import constants
import sso

root = Tk()
Label(root, text='账号:').grid(row=0, column=0)
Label(root, text='密码:').grid(row=1, column=0)
account = StringVar()
passwd = StringVar()
e1 = Entry(root, textvariable=account)
e2 = Entry(root, textvariable=passwd, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def check():
    s = sso.login(e1.get(), e2.get())

    s.get(constants.portal)

    lessons = []
    teachers = []

    lessons_text = s.post(constants.lesson_url, constants.default_post_body,
                          headers={'Content-Type': 'application/json;charset=UTF-8'}).text
    lessons_obj: list = json.loads(lessons_text)
    i: dict
    for i in lessons_obj:
        if i["KKXND"] == "2022-2023":
            if i["KCMC"] not in lessons:
                lessons.append(i["KCMC"])
            if i["JSXM"] not in teachers:
                teachers.append(i["JSXM"])
    msg = str(lessons) + "\n" + str(teachers)
    messagebox.showinfo("选课", msg)
    root.quit()
    sys.exit()


Button(root, text='查询', width=10, command=check) \
    .grid(row=3, column=0, padx=10, pady=5, sticky=W)
Button(root, text='退出', width=10, command=root.quit) \
    .grid(row=3, column=1, padx=10, pady=5, sticky=E)
mainloop()
