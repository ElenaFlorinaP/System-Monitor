import time
import psutil
import platform

system = platform.system()
version = platform.version()

print(f"System {system} version {version}")

def display_usage(cpu_usage, memory_usage, bars = 30):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '*' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    memory_percent = (memory_usage / 100.0)
    memory_bar = '*' * int(memory_percent * bars) + '-' * (bars - int(memory_percent * bars))

    print(f"\rCPU usage: |{cpu_bar}| {cpu_usage:.1f}%  ", end ="")
    print(f"Memory usage: |{memory_bar}| {memory_usage:.2f}%  ", end= "\r")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)
