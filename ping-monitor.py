import os
import platform
import subprocess
import time
from datetime import datetime

TARGET_HOST = "8.8.8.8"  # Google DNS
PING_INTERVAL = 5        # Seconds between checks
LOG_FILE = "network_monitor_log.txt"

def ping_host(host):
    # Determine the correct ping flag based on the OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    start_time = time.time()
    # Run the system ping command silently
    response = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    latency = round((time.time() - start_time) * 1000, 2)
    
    return response.returncode == 0, latency

def log_status(status, latency):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    state = "ONLINE" if status else "OFFLINE"
    log_message = f"[{timestamp}] Status: {state} | Latency: {latency}ms\n"
    
    print(log_message.strip())
    with open(LOG_FILE, "a") as file:
        file.write(log_message)

print(f"Starting network monitor targeting {TARGET_HOST}...")
try:
    while True:
        is_online, current_latency = ping_host(TARGET_HOST)
        log_status(is_online, current_latency)
        time.sleep(PING_INTERVAL)
except KeyboardInterrupt:
    print("\nMonitoring stopped safely.")
