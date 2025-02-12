# This code was written by Joey Malvinni, in utter terror at the error: "Connection reset by peer." 
# The logs on the Raspberry Pi did not help whatsoever, and in fact succeeded in sowing more confusion.
# The actual fix was the completely power off the Raspberry Pi (even turning off the backup battery) and restarting.
# 2/11/2025

from os import path

exists = False
log_path = "./logs.txt"

def log_to_file(text):
    global exists
    if not exists and not path.exists(log_path):
        open(log_path, "x")
    elif path.exists(log_path):
        exists = True

    with open(log_path, "a") as f:
        f.write("[info] " + text + '\n')

def error_to_file(text):
    global exists
    if not exists and not path.exists(log_path):
        open(log_path, "x")
    elif path.exists(log_path):
        exists = True

    with open(log_path, "a") as f:
        f.write("[ERR] " + text + '\n')