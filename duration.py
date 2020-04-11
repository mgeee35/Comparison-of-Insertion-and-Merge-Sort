import time


def start_time():
    start = time.time()
    return start


def stop_time():
    stop = time.time()
    return stop


def calc_duration(t1, t2):
    return round(t2 - t1, 15)