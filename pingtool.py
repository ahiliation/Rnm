def do_ping(host, timeout=2):
    try:
        response = ping(host, count=1, timeout=timeout, verbose=False)
        if response.success():
            latency_ms = response.rtt_avg_ms
            ttl = getattr(response, 'ttl', 0)
            return (latency_ms, ttl, True)
    except Exception:
        pass
    return (0, 0, False)