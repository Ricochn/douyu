import tkinter
import get_danmu
import threading



def back_get_msg():
    print("back_get_msg bdgin")
    get_danmu.get_daunmu(int(entry_room_id.get()))

def change():
    lenth = len(get_danmu.mslist)
    text_danmu.insert(tkinter.END, "change begin")
    while get_danmu.ison:
        if len(get_danmu.mslist) > lenth:
            try:
                text_danmu.insert(tkinter.END, get_danmu.mslist[-1]+"\n")
                lenth = len(get_danmu.mslist)
                text_danmu.focus_force()
            except:
                pass

def submit_event():
    print("启动线程")
    thread1=threading.Thread(target=back_get_msg)
    thread2=threading.Thread(target=change)
    thread1.start()
    thread2.start()

def closeWindow():
    get_danmu.ison = False
    top.destroy()


#顶层窗口
top =  tkinter.Tk()
top.geometry('500x300')
top.protocol('WM_DELETE_WINDOW', closeWindow)

label_room_id = tkinter.Label(top, text="输入房间号：")
entry_room_id = tkinter.Entry(top, background="#aaaaff")
button_submit = tkinter.Button(top, text="提交查看弹幕", command=submit_event)
text_danmu = tkinter.Text(top)

label_room_id.pack()
entry_room_id.pack()
button_submit.pack()
text_danmu.pack()

tkinter.mainloop()