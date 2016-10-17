import time
import webbrowser

breaks_take = 0
total_breaks = 3

print("This program started on " + time.ctime())
while (breaks_take < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    breaks_take += 1
