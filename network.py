import platform
import subprocess

def check_internet():
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '8.8.8.8']

    result = subprocess.call(command, stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)

    if result == 0:
        return "ONLINE"
    else:
        return "OFFLINE" 
