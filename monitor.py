import time
import psutil
import platform
import network
import alert

system = platform.system()
version = platform.version()

print(f"System {system} version {version}\n")

cpu_limit = 85.0
ram_limit = 85.0
alert_break = 60

last_ver_net = 0
net_status = "Checking..."

previous_net_status = "Checking..."

last_alert_cpu = 0
last_alert_ram = 0

def display_usage(cpu_usage, memory_usage, stars = 20):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '*' * int(cpu_percent * stars) + '-' * (stars - int(cpu_percent * stars))

    memory_percent = (memory_usage / 100.0)
    memory_bar = '*' * int(memory_percent * stars) + '-' * (stars - int(memory_percent * stars))

    return f"CPU usage: |{cpu_bar}| {cpu_usage:.1f}%   RAM: |{memory_bar}| {memory_usage:.1f}%"
    
def get_network_status():
    global last_ver_net, net_status, previous_net_status 
    current_time = time.time()
    if current_time - last_ver_net >= 5:
        new_status = network.check_internet()
        
        if "ONLINE" in new_status and previous_net_status == "OFFLINE":
            alert.send_discord_message("INTERNET RECONECTAT!")
        
        previous_net_status = new_status
        net_status = new_status
        last_ver_net = current_time

    return f"NETWORK: |{net_status}|"

def check_alerts(cpu, ram):
    global last_alert_cpu, last_alert_ram
    current_time = time.time()
    if cpu >= cpu_limit:
        if current_time - last_alert_cpu >= alert_break:
            alert.send_discord_message(f"CPU ALERT: The processor reached {cpu}%!")
            last_alert_cpu = current_time

    if ram >= ram_limit:
        if current_time - last_alert_ram >= alert_break:
            alert.send_discord_message(f"RAM ALERT: The memory reached: {ram}%!")
            last_alert_ram = current_time
while True:

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    check_alerts(cpu, ram)

    hardware_text = display_usage(cpu, ram, 30)
    network_text = get_network_status()
    print(f"\r{hardware_text}   {network_text}   ", end="")
    time.sleep(0.5)


