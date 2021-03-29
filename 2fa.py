import signal

def handle_interrupt(sig, frame):
    try:
        curses.endwin()
    except:
        pass
    print("\x1b[?1000;1006;1015l\x1b[?25h\x1b[?47l\x1b8")
    exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

print("\x1b7", end = "")
print("\x1b[?47h", end = "") #Switch screen buffer
print("\x1b[?25l", end = "") #Hide cursor
print("\x1b[?1000;1006;1015h") #Track mouse
import curses
import sys
android = "android" in sys.version
import subprocess
import time
import pyperclip
import re
term = curses.initscr()
term.nodelay(True)

codes = {
    "Name": "<KEY>",
    "Some bullshit": "MUOINFE4NBWXN7EW",
}


l = max(*[len(c) for c in codes]) + 12

global selected, last_sel

selected = -1
last_sel = -1

def print_shit():
    global selected, last_sel
    st = "\x1b[0m\x1b[2;3J\x1b[H"
    t = str(int(time.time() / 30))
    n = -1
    for code in codes:
        n += 1
        f = subprocess.run(["oathtool", "-c", t, "-b", codes[code]], capture_output = 1).stdout.decode().strip()
        st += f"\x1b[94;1m{code}\x1b[0m:".ljust(l) + " "
        if selected == n:
            st += f"\x1b[92;1m{f[:3]} {f[3:]}\x1b[0m\n\r"
            if last_sel != selected:
                if android:
                    subprocess.Popen(["termux-clipboard-set", f])
                else:
                    pyperclip.copy(f)
                last_sel = selected
        else:
            st += f"{f[:3]} {f[3:]}\n\r"
    print(f"{st}\x1b[93;1m{30 - int(time.time()) % 30}s left\x1b[0m", end = "\n\r\x1b[8m")

term.getch()
while True:
    if int(time.time()) % 30 == 0:
        selected = ""
    print_shit()
    st = ""
    #while not st:
    lt = int(time.time())
    while lt == int(time.time()):
        ch = term.getch()
        while ch != -1:
            st += chr(ch)
            ch = term.getch()
        if st:
            break
        time.sleep(0.01)
    if re.search(r"\d+;\d+;\d+[mM]", st):
        selected = int(st.split(";")[-1][:-1]) - 1
    elif st == "\x1b[A":
        selected = min(max(selected - 1, 0), len(codes) - 1)
    elif st == "\x1b[B":
        selected = min(max(selected + 1, 0), len(codes) - 1)
#    elif st:
#        print("\x1b[0m`" + " ".join(st) + "'\r\n")
#        term.getch()
#        time.sleep(10)
