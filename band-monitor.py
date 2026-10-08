def monitor_bandwidth(interface, chart_height, chart_width):
    history_dl = deque(maxlen=HISTORY_POINTS)
    history_ul = deque(maxlen=HISTORY_POINTS)
    
    prev = psutil.net_io_counters(pernic=True)[interface]
    
    while running:
        time.sleep(INTERVAL)
        cur = psutil.net_io_counters(pernic=True)[interface]
        
        dl = safe_diff(cur.bytes_recv, prev.bytes_recv) / INTERVAL
        ul = safe_diff(cur.bytes_sent, prev.bytes_sent) / INTERVAL
        prev = cur
        
        history_dl.append(dl)
        history_ul.append(ul)