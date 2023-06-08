from tkinter import *
import datetime
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo

root = tk.Tk()
root.title("Nextel video player")
root.geometry("800x700+290+10")


frame = tk.Frame(root)
frame.pack()

image_icon = PhotoImage(file="ICON.png")
root.iconphoto(False, image_icon)

lower_frame = tk.Frame(root, bg="#FFFFFF")
lower_frame.pack(fill="both", side=BOTTOM)




def update_duration(event):
    duration = vid_player.video_info(["duration"])

    end_time["text"] = str(datetime.timedelta(seconds=duration))
    progress_slider["to"] = duration


def update_scale(event):
    progress_value.st(vid_player.current_duration())


def load_video():
    fill_path = filedialog.askopenfilename()
    if fill_path:
        vid_player.load(fill_path)
        progress_slider.config(to=0, from_=0)
        play_pause_btn["text"] = "play"
        progress_value.set(0)


def seek(value):
    vid_player.seek(int(value))


def skip(value: int):
    vid_player.seek(int(progress_slider.get())+value)
    progress_value.set(progress_slider.get()+value)


def play_pause():
    if vid_player.is_paused():
        vid_player.play()
        play_pause_btn["text"] = "pause"

    else:
        vid_player.pause
        play_pause_btn["text"] = "play"


def video_ended(event):
    progress_slider.set(progress_slider("to"))
    play_pause_btn["text"] = "play"
    progress_slider.set(0)


load_btn = tk.Button(text="Browse", bg="#FFFFFF",
                     font=("calibri", 12, "bold"), command=load_video)
load_btn.pack(ipadx=12, ipady=4, anchor=tk.NW)

vid_player = TkinterVideo(root, scaled=True)
vid_player.pack(expand=True, fill="both")


Buttonbackward = PhotoImage(file="backward.png")
back = tk.Button(lower_frame, image=Buttonbackward, bd=0,
                 height=50, width=50, command=lambda: skip(-5)).pack(side=LEFT)


play_pause_btn = tk.Button(lower_frame, text="play",
                           width=40, height=5, command=play_pause)
play_pause_btn.pack(expand=True, fill="both", side=LEFT)


Buttonforward = PhotoImage(file="forward.png")
playbutton = tk.Button(lower_frame, image =Buttonforward, bd=0,
                       height=50, width=50, command=lambda: skip(5)).pack(side=LEFT)



start_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
start_time.pack(side="left")

progress_value = tk.IntVar(root)

progress_slider = tk.Scale(root, variable=progress_value,
                           from_=0, to=0,  orient="horizontal", command=seek)
progress_slider.pack(side="left", fill="x", expand=True)

end_time = tk.Label(root, text=str(datetime.timedelta(seconds=0)))
end_time.pack(side="left")




vid_player.bind("<<Duration>>", update_duration)
vid_player.bind("<<secondchanged>>", update_scale)

vid_player.bind("<<Ended>>", video_ended)


root.mainloop()
