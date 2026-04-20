import tkinter as tk
import threading
import monitor

stop_signal = threading.Event()
monitor_thread = threading.Thread(target=monitor.start_agent, args=(stop_signal,),daemon=True)

def start_monitor():
    global monitor_thread, stop_signal

    webhook_url = entry_webhook.get()

    if not webhook_url:
        label_status.config(text="Status: ERROR!Enter the link: ", fg = "orange")
        return
    if not stop_signal or not monitor_thread.is_alive():
        stop_signal = threading.Event()
        monitor_thread = threading.Thread(
            target = monitor.start_agent,
            args = (stop_signal, webhook_url),
            daemon = True
        )
        monitor_thread.start()
        label_status.config(text="Status: ACTIVE ", fg="green")
    

def stop_monitor():
    global monitor_thread
    if monitor_thread is not None and monitor_thread.is_alive():
        stop_signal.set()
        label_status.config(text = "Status: INACTIVE", fg = "red")

window = tk.Tk()
window.title("System monitor - Control Panel")
window.geometry("400x250")

title_label = tk.Label(window, text = "Monitoring System", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

label_status = tk.Label(window, text="Status: STOPPED" , fg="red", font=("Arial",10))
label_status.pack(pady=5)

button_frame = tk.Frame(window)
button_frame.pack()

label_webhook = tk.Label(window, text="Link Discord Webhook: ")
label_webhook.pack(pady=5)

entry_webhook = tk.Entry(window,width=45)
entry_webhook.pack(pady=5)

btn_start = tk.Button(button_frame, text="START", bg="green", width=10, command=start_monitor)
btn_start.grid(row=0, column=0, padx=5)

btn_stop = tk.Button(button_frame, text="STOP" , bg="red", width=10, command=stop_monitor)
btn_stop.grid(row=0,column=1,padx=5)
window.mainloop()

