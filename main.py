from myLib.userEvents import KeyboardListener, MouseController, Button
import time,threading


delay = 0.0000001
button = Button.left
start_stop_key = 'a'
stop_key = 'b'

class ClickMouse(threading.Thread):
  def __init__(self, delay, button):
    super(ClickMouse, self).__init__()
    self.delay = delay
    self.button = button
    self.running = False
    self.program_running = True

  def start_clicking(self):
    print('Started')
    self.running = True

  def stop_clicking(self):
    print('Stoped')
    self.running = False

  def exit(self):
    self.stop_clicking()
    self.program_running = False

  def run(self):
    while self.program_running:
      while self.running:
        mouse.click(self.button)
        time.sleep(self.delay) 
      time.sleep(0.1)
  
mouse = MouseController()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_release(key):
  if key == start_stop_key:
    if click_thread.running: click_thread.stop_clicking()
    else: click_thread.start_clicking()        
  elif key == stop_key:
    click_thread.exit()
    keyboardListener.terminate()


keyboardListener = KeyboardListener(on_release=on_release,auto_start=True)
