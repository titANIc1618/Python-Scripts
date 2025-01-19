Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... import time
... 
... # Pomodoro time settings
... WORK_TIME = 25 * 60  # 25 minutes in seconds
... BREAK_TIME = 5 * 60  # 5 minutes in seconds
... cycle_count = 0
... 
... # Timer function
... def start_timer():
...     global cycle_count
...     if cycle_count % 2 == 0:  # Work session
...         count_down(WORK_TIME)
...         cycle_count += 1
...         label.config(text="Work Time!")
...     else:  # Break session
...         count_down(BREAK_TIME)
...         cycle_count += 1
...         label.config(text="Break Time!")
... 
... # Countdown function
... def count_down(count):
...     mins, secs = divmod(count, 60)
...     timer_display.config(text=f"{mins:02d}:{secs:02d}")
...     if count > 0:
...         root.after(1000, count_down, count - 1)
...     else:
...         start_timer()
... 
... # Reset the timer
... def reset_timer():
...     global cycle_count
...     cycle_count = 0
...     timer_display.config(text="00:00")
...     label.config(text="Pomodoro Timer")
...     
... # Create the main window
... root = tk.Tk()
... root.title("Pomodoro Timer")
... 
# Create the label to show "Work Time" or "Break Time"
label = tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 24), fg="blue")
label.pack(pady=20)

# Create the label to show the countdown
timer_display = tk.Label(root, text="00:00", font=("Helvetica", 48), fg="black")
timer_display.pack(pady=10)

# Create the Start button
start_button = tk.Button(root, text="Start", font=("Helvetica", 14), command=start_timer)
start_button.pack(pady=5)

# Create the Reset button
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=reset_timer)
reset_button.pack(pady=5)

# Run the main loop
root.mainloop()
