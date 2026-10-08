import time
import psutil

def monitor_bandwidth(interval=1):
    # Get initial bytes sent/received
    old_value = psutil.net_io_counters()
    
    while True:
        time.sleep(interval)
        new_value = psutil.net_io_counters()
        
        # Calculate speed in KB/s
        download_speed = (new_value.bytes_recv - old_value.bytes_recv) / 1024 / interval
        upload_speed = (new_value.bytes_sent - old_value.bytes_sent) / 1024 / interval
        
        print(f"Download: {download_speed:.2f} KB/s | Upload: {upload_speed:.2f} KB/s")
        old_value = new_value

if __name__ == "__main__":
    print("Monitoring interface traffic... (Ctrl+C to stop)")
    monitor_bandwidth()

def calculate_time(start, stop):
  
    # to calculate unavailability time
    difference = stop - start
    seconds = float(str(difference.total_seconds()))
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]