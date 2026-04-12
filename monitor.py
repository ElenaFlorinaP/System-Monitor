import time
import psutil
import platform
import network

system = platform.system()
version = platform.version()

print(f"System {system} version {version}\n")



def display_usage(cpu_usage, memory_usage, stars = 20):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '*' * int(cpu_percent * stars) + '-' * (stars - int(cpu_percent * stars))

    memory_percent = (memory_usage / 100.0)
    memory_bar = '*' * int(memory_percent * stars) + '-' * (stars - int(memory_percent * stars))

    print(f"\rCPU usage: |{cpu_bar}| {cpu_usage:.1f}%   RAM: |{memory_bar}| {memory_usage:.1f}%  NET: |{network.check_internet()}|", end="" )
    

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)


