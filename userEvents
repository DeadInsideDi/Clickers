from ctypes import WINFUNCTYPE, c_int, Structure, cast, POINTER, windll,c_void_p
from ctypes.wintypes import LPARAM, WPARAM, DWORD, PULONG, LONG, LPMSG
from win32gui import PumpWaitingMessages
import win32con,threading,win32api,time
from typing import Callable,Union,Literal,List


class MouseHookStruct(Structure):
  _fields_=[
    ('x',LONG),
    ('y',LONG),
    ('mouseData',DWORD),
    ('flags',DWORD),
    ('time',DWORD),
    ('dwExtraInfo',PULONG)
  ]
  
class MouseEvent:
  id:Union[str,int]='',
  x:LONG=0,
  y:LONG=0,
  mouseData:DWORD=0,
  flags:DWORD=0,
  time:DWORD=0,
  dwExtraInfo:PULONG={}
  prevX:int=0,
  prevY:int=0

class KeyboardHookStruct(Structure):
  _fields_ = [
    ("vkCode", DWORD),
    ("scanCode", DWORD),
    ("flags", DWORD),
    ("time", DWORD),
    ("dwExtraInfo", POINTER(c_void_p))
  ]

class KeyboardEvent:
  key:str='',
  pressed:bool=False,
  vkCode:LONG=0,
  scanCode:DWORD=0,
  flags:DWORD=0,
  time:DWORD=0,
  dwExtraInfo:POINTER(c_void_p)={}




WMEVENTS = {
  512: 'MOUSEMOVE',
  513: 'LBUTTONDOWN',
  514: 'LBUTTONUP',
  516: 'RBUTTONDOWN',
  517: 'RBUTTONUP',
  519: 'MBUTTONDOWN',
  520: 'MBUTTONUP',
  522: 'MOUSESCROLL'
}

VKEVENTS = {
  1: 'LBUTTON', 
  2: 'RBUTTON', 
  3: 'CANCEL', 
  4: 'MBUTTON', 
  8: 'BACK', 
  9: 'TAB', 
  12: 'CLEAR', 
  13: 'RETURN', 
  16: 'SHIFT', 
  17: 'CONTROL', 
  18: 'MENU', 
  19: 'PAUSE', 
  20: 'CAPITAL', 
  21: 'HANGUL', 
  23: 'JUNJA', 
  24: 'FINAL', 
  25: 'KANJI', 
  27: 'ESCAPE', 
  28: 'CONVERT', 
  29: 'NONCONVERT', 
  30: 'ACCEPT', 
  31: 'MODECHANGE', 
  32: 'SPACE', 
  33: 'PRIOR', 
  34: 'NEXT', 
  35: 'END', 
  36: 'HOME', 
  37: 'LEFT', 
  38: 'UP', 
  39: 'RIGHT', 
  40: 'DOWN', 
  41: 'SELECT', 
  42: 'PRINT', 
  43: 'EXECUTE', 
  44: 'SNAPSHOT', 
  45: 'INSERT', 
  46: 'DELETE', 
  47: 'HELP', 
  91: 'LWIN', 
  92: 'RWIN', 
  93: 'APPS', 
  96: 'NUMPAD0', 
  97: 'NUMPAD1', 
  98: 'NUMPAD2', 
  99: 'NUMPAD3', 
  100: 'NUMPAD4', 
  101: 'NUMPAD5', 
  102: 'NUMPAD6', 
  103: 'NUMPAD7', 
  104: 'NUMPAD8', 
  105: 'NUMPAD9', 
  106: 'MULTIPLY', 
  107: 'ADD', 
  108: 'SEPARATOR', 
  109: 'SUBTRACT', 
  110: 'DECIMAL', 
  111: 'DIVIDE', 
  112: 'F1', 
  113: 'F2', 
  114: 'F3', 
  115: 'F4', 
  116: 'F5', 
  117: 'F6', 
  118: 'F7', 
  119: 'F8', 
  120: 'F9', 
  121: 'F10', 
  122: 'F11', 
  123: 'F12', 
  124: 'F13', 
  125: 'F14', 
  126: 'F15', 
  127: 'F16', 
  128: 'F17', 
  129: 'F18', 
  130: 'F19', 
  131: 'F20', 
  132: 'F21', 
  133: 'F22', 
  134: 'F23', 
  135: 'F24', 
  144: 'NUMLOCK', 
  145: 'SCROLL', 
  160: 'LSHIFT', 
  161: 'RSHIFT', 
  162: 'LCONTROL', 
  163: 'RCONTROL', 
  164: 'LMENU', 
  165: 'RMENU', 
  229: 'PROCESSKEY', 
  246: 'ATTN', 
  247: 'CRSEL', 
  248: 'EXSEL', 
  249: 'EREOF', 
  250: 'PLAY', 
  251: 'ZOOM', 
  252: 'NONAME', 
  253: 'PA1', 
  254: 'OEM_CLEAR', 
  5: 'XBUTTON1', 
  6: 'XBUTTON2', 
  173: 'VOLUME_MUTE', 
  174: 'VOLUME_DOWN', 
  175: 'VOLUME_UP', 
  176: 'MEDIA_NEXT_TRACK', 
  177: 'MEDIA_PREV_TRACK', 
  179: 'MEDIA_PLAY_PAUSE', 
  166: 'BROWSER_BACK', 
  167: 'BROWSER_FORWARD',
  192: '`',
  49: '1',
  50: '2',
  51: '3',
  52: '4',
  53: '5',
  54: '6',
  55: '7',
  56: '8',
  57: '9',
  48: '0',
  189: '-',
  187: '=',
  81: 'q',
  87: 'w',
  69: 'e',
  82: 'r',
  84: 't',
  89: 'y',
  85: 'u',
  73: 'i',
  79: 'o',
  80: 'p',
  219: '[',
  221: ']',
  220: '\\',
  65: 'a',
  83: 's',
  68: 'd',
  70: 'f',
  71: 'g',
  72: 'h',
  74: 'j',
  75: 'k',
  76: 'l',
  186: ';',
  222: "'",
  90: 'z',
  88: 'x',
  67: 'c',
  86: 'v',
  66: 'b',
  78: 'n',
  77: 'm',
  188: ',',
  190: '.',
  191: '/',
  448: '~',
  305: '!',
  306: '@',
  307: '#',
  308: '$',
  309: '%',
  310: '^',
  311: '&',
  312: '*',
  313: '(',
  304: ')',
  445: '_',
  443: '+',
  337: 'Q',
  343: 'W',
  325: 'E',
  338: 'R',
  340: 'T',
  345: 'Y',
  341: 'U',
  329: 'I',
  335: 'O',
  336: 'P',
  475: '{',
  477: '}',
  476: '|',
  321: 'A',
  339: 'S',
  324: 'D',
  326: 'F',
  327: 'G',
  328: 'H',
  330: 'J',
  331: 'K',
  332: 'L',
  442: ':',
  478: '"',
  346: 'Z',
  344: 'X',
  323: 'C',
  342: 'V',
  322: 'B',
  334: 'N',
  333: 'M',
  444: '<',
  446: '>',
  447: '?'
}

CodeByChar = {
  '\b':8,
  '\t':9,
  '\n': 13,
  ' ': 32,
  '`': 192,
  '1': 49,
  '2': 50,
  '3': 51,
  '4': 52,
  '5': 53,
  '6': 54,
  '7': 55,
  '8': 56,
  '9': 57,
  '0': 48,
  '-': 189,
  '=': 187,
  'q': 81,
  'w': 87,
  'e': 69,
  'r': 82,
  't': 84,
  'y': 89,
  'u': 85,
  'i': 73,
  'o': 79,
  'p': 80,
  '[': 219,
  ']': 221,
  '\\': 220,
  'a': 65,
  's': 83,
  'd': 68,
  'f': 70,
  'g': 71,
  'h': 72,
  'j': 74,
  'k': 75,
  'l': 76,
  ';': 186,
  "'": 222,
  'z': 90,
  'x': 88,
  'c': 67,
  'v': 86,
  'b': 66,
  'n': 78,
  'm': 77,
  ',': 188,
  '.': 190,
  '/': 191,
  '~': 448,
  '!': 305,
  '@': 306,
  '#': 307,
  '$': 308,
  '%': 309,
  '^': 310,
  '&': 311,
  '*': 312,
  '(': 313,
  ')': 304,
  '_': 445,
  '+': 443,
  'Q': 337,
  'W': 343,
  'E': 325,
  'R': 338,
  'T': 340,
  'Y': 345,
  'U': 341,
  'I': 329,
  'O': 335,
  'P': 336,
  '{': 475,
  '}': 477,
  '|': 476,
  'A': 321,
  'S': 339,
  'D': 324,
  'F': 326,
  'G': 327,
  'H': 328,
  'J': 330,
  'K': 331,
  'L': 332,
  ':': 442,
  '"': 478,
  'Z': 346,
  'X': 344,
  'C': 323,
  'V': 342,
  'B': 322,
  'N': 334,
  'M': 333,
  '<': 444,
  '>': 446,
  '?': 447
}


user32 = windll.user32

class MouseListener:
  def __init__(self, 
    on_event:Union[Callable[[object], Union[int,None]],List[Callable[[object], Union[int,None]]],None]=None,
    on_move:Union[Callable[[int,int], Union[int,None]],List[Callable[[int,int], Union[int,None]]],None]=None,
    on_click:Union[Callable[[int,int,str,bool], Union[int,None]],List[Callable[[int,int,str,bool], Union[int,None]]],None]=None,
    on_scroll:Union[Callable[[int,int,int,int], Union[int,None]],List[Callable[[int,int,int,int], Union[int,None]]],None]=None,
    auto_start:bool=False,count_last_mouse_pos:bool=False
    # ,block_event:Literal['default','move','click','scroll']=None
  ):
    beautify_mode = on_move is not None or on_click is not None or on_scroll is not None
    self.events = {}
    if isinstance(on_event,list):
      for i in range(len(on_event)):
        self.events[i] = on_event[i]
    elif on_event is None:
      if not beautify_mode: auto_start = False
    else:
      self.events[0] = on_event
    
    if beautify_mode:
      self.on_move_events = {}
      if isinstance(on_move,list):
        for i in range(len(on_move)):
          self.on_move_events[i] = on_move[i]
      elif on_move is not None:
        self.on_move_events[0] = on_move
        
      self.on_click_events = {}
      if isinstance(on_click,list):
        for i in range(len(on_click)):
          self.on_click_events[i] = on_click[i]
      elif on_click is not None:
        self.on_click_events[0] = on_click
        
      self.on_scroll_events = {}
      if isinstance(on_scroll,list):
        for i in range(len(on_scroll)):
          self.on_scroll_events[i] = on_scroll[i]
      elif on_scroll is not None:
        self.on_scroll_events[0] = on_scroll
    
    self.lastPositionX = 0
    self.lastPositionY = 0
    self.isTurnOnMouseListener = threading.Event()
    self.isWorkingMouseListener= threading.Event()
    self.isTurnOnMouseListener.set()
    if auto_start: self.isWorkingMouseListener.set()
  
    self.hook_id = None
    if count_last_mouse_pos: self.run = self._run1
    elif beautify_mode:  self.run = self._run2
    else: self.run = self._run0
    threading.Thread(target=self.run).start()

  def start(self):
    if len(self.events) > 0:
      self.isWorkingMouseListener.set()
    
  def stop(self):
    self.isWorkingMouseListener.clear()
    user32.UnhookWindowsHookEx(self.hook_id)
    self.hook_id = None
  
  def terminate(self):
    self.isWorkingMouseListener.clear()
    self.isTurnOnMouseListener.clear()
    self.hook_id = None
  
  def addEvent(self,on_event:Callable,key_event:str='',type_event:Literal['default','move','click','scroll']='default'):
    if type_event == 'default':
      key_event = key_event or len(self.events.keys())
      self.events[key_event] = on_event
    elif type_event == 'move':
      key_event = key_event or len(self.on_move_events.keys())
      self.on_move_events[key_event] = on_event
    elif type_event == 'click':
      key_event = key_event or len(self.on_click_events.keys())
      self.on_click_events[key_event] = on_event
    elif type_event == 'scroll':
      key_event = key_event or len(self.on_scroll_events.keys())
      self.on_scroll_events[key_event] = on_event
      
    if not self.isWorkingMouseListener.is_set(): self.start()
      
  def removeEvent(self,key_event:str,type_event:Literal['default','move','click','scroll']='default'):
    if type_event == 'default':
      if key_event in self.events:
        if len(self.events) == 1: self.stop()
        del self.events[key_event]
    elif type_event == 'move':
      if key_event in self.on_move_events:
        if len(self.on_move_events) == 1: self.stop()
        del self.on_move_events[key_event]
    elif type_event == 'click':
      if key_event in self.on_click_events:
        if len(self.on_click_events) == 1: self.stop()
        del self.on_click_events[key_event]
    elif type_event == 'scroll':
      if key_event in self.on_scroll_events:
        if len(self.on_scroll_events) == 1: self.stop()
        del self.on_scroll_events[key_event]
    
  def _run0(self):
    @WINFUNCTYPE(LPARAM, c_int, WPARAM, POINTER(MouseHookStruct))
    def mouseHook(nCode, wParam, lParam):
      msg = lParam.contents
      msg.id = wParam
      isBlockEvent = False
      for event in self.events.values(): isBlockEvent = isBlockEvent or event(msg)
      if isBlockEvent: return 1
      return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    while self.isTurnOnMouseListener.is_set():
      while self.hook_id: PumpWaitingMessages()
      time.sleep(0.1)
      if self.isWorkingMouseListener.is_set():
        self.hook_id = user32.SetWindowsHookExW(win32con.WH_MOUSE_LL, mouseHook, None, 0)
  
  def _run1(self):
    @WINFUNCTYPE(LPARAM, c_int, WPARAM, POINTER(MouseHookStruct))
    def mouseHook(nCode, wParam, lParam):
      msg = lParam.contents
      msg.id = wParam
      msg.prevX = msg.x-self.lastPositionX
      msg.prevY = msg.y-self.lastPositionY
      isBlockEvent = False
      for event in self.events.values(): isBlockEvent = isBlockEvent or event(msg)
      self.lastPositionX = msg.x
      self.lastPositionY = msg.y
      if isBlockEvent: return 1
      return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    while self.isTurnOnMouseListener.is_set():
      while self.hook_id: PumpWaitingMessages()
      time.sleep(0.1)
      if self.isWorkingMouseListener.is_set():
        self.hook_id = user32.SetWindowsHookExW(win32con.WH_MOUSE_LL, mouseHook, None, 0)
  
  def _run2(self):
    @WINFUNCTYPE(LPARAM, c_int, WPARAM, POINTER(MouseHookStruct))
    def mouseHook(nCode, wParam, lParam):
      msg = lParam.contents
      msg.id = WMEVENTS[wParam]
      x, y = (msg.x, msg.y)
      data = TokenUserEvents[wParam]
      typeEvent = data[0]
      isBlockEvent = False
      
      for event in self.events.values(): isBlockEvent = isBlockEvent or event(msg)
      if typeEvent == 'move':
        for event in self.on_move_events.values(): isBlockEvent = isBlockEvent or event(x,y)
      elif typeEvent == 'click':
        for event in self.on_click_events.values(): isBlockEvent = isBlockEvent or event(x,y,data[1],data[2])
      elif typeEvent == 'scroll':
        for event in self.on_scroll_events.values(): isBlockEvent = isBlockEvent or event(x,y,0,(-1 if msg.mouseData == 4287102976 else 1))
      
      if isBlockEvent: return 1
      return user32.CallNextHookEx(None, nCode, wParam, lParam)

    TokenUserEvents = { 
      512:['move'],                 # 'WM_MOUSEMOVE' 
      513:['click','Left',True],    # 'WM_LBUTTONDOWN'
      514:['click','Left',False],   # 'WM_LBUTTONUP'
      516:['click','Right',True],   # 'WM_RBUTTONDOWN'
      517:['click','Right',False],  # 'WM_RBUTTONUP'
      519:['click','Middle',True],  # 'WM_MBUTTONDOWN'
      520:['click','Middle',False], # 'WM_MBUTTONUP'
      522:['scroll']                # 'WM_MOUSELAST'
    }
    
    while self.isTurnOnMouseListener.is_set():
      while self.hook_id: PumpWaitingMessages()
      time.sleep(0.1)
      if self.isWorkingMouseListener.is_set():
        self.hook_id = user32.SetWindowsHookExW(win32con.WH_MOUSE_LL, mouseHook, None, 0)



class KeyboardListener:
  def __init__(self,
    on_event:Union[Callable[[object], None],List[Callable[[object], None]],None]=None,
    on_press:Union[Callable[[str], None],List[Callable[[str], None]],None]=None,
    on_release:Union[Callable[[str], None],List[Callable[[str], None]],None]=None,
    auto_start:bool=False,id_int_mode:bool=False,beautify_mode:bool=False
  ):
    beautify_mode = on_press is not None or on_release is not None
    self.events = {}
    if isinstance(on_event,list):
      for i in range(len(on_event)):
        self.events[i] = on_event[i]
    elif on_event is None and not beautify_mode:
      auto_start = False
    else:
      self.events[0] = on_event
    
    if beautify_mode:
      self.on_press_events = {}
      if isinstance(on_press,list):
        for i in range(len(on_press)):
          self.on_press_events[i] = on_press[i]
      elif on_press is not None:
        self.on_press_events[0] = on_press
        
      self.on_release_events = {}
      if isinstance(on_release,list):
        for i in range(len(on_release)):
          self.on_release_events[i] = on_release[i]
      elif on_release is not None:
        self.on_release_events[0] = on_release
        
    self.isTurnOnKeyboardListener = threading.Event()
    self.isWorkingKeyboardListener= threading.Event()
    self.isTurnOnKeyboardListener.set()
    if auto_start: self.isWorkingKeyboardListener.set()
  
    self.hook_id = None
    
    if id_int_mode: self.run = self._run1
    elif beautify_mode: self.run = self._run2
    else: self.run = self._run0
    
    threading.Thread(target=self.run).start()

  def start(self):
    if len(self.events) > 0:
      self.isWorkingKeyboardListener.set()
    
  def stop(self):
    self.isWorkingKeyboardListener.clear()
    user32.UnhookWindowsHookEx(self.hook_id)
    self.hook_id = None
  
  def terminate(self):
    self.isWorkingKeyboardListener.clear()
    self.isTurnOnKeyboardListener.clear()
    self.hook_id = None
  
  def addEvent(self,on_event:Callable,type_event:Literal['default','press','release']='default'):
    if type_event == 'default':
      key_event = key_event or len(self.events.keys())
      self.events[key_event] = on_event
    elif type_event == 'press':
      key_event = key_event or len(self.on_press_events.keys())
      self.on_press_events[key_event] = on_event
    elif type_event == 'release':
      key_event = key_event or len(self.on_release_events.keys())
      self.on_release_events[key_event] = on_event
      
    if not self.isWorkingKeyboardListener.is_set(): self.start()
      
    
  def removeEvent(self,key_event:str,type_event:Literal['default','press','release']='default'):
    if type_event == 'default':
      if key_event in self.events:
        if len(self.events) == 1: self.stop()
        del self.events[key_event]
    elif type_event == 'press':
      if key_event in self.on_press_events:
        if len(self.on_press_events) == 1: self.stop()
        del self.on_press_events[key_event]
    elif type_event == 'release':
      if key_event in self.on_release_events:
        if len(self.on_release_events) == 1: self.stop()
        del self.on_release_events[key_event]
    
  def _run0(self):
    @WINFUNCTYPE(c_int, c_int, WPARAM, POINTER(KeyboardHookStruct))
    def keyboardHook(nCode, wParam, lParam):
      msg = lParam.contents
      msg.pressed = True if wParam == 256 else False # win32con.WM_KEYDOWN = 256
      vk_code = msg.vkCode
      if vk_code in VKEVENTS: msg.key = VKEVENTS[vk_code]
      else: msg.key = chr(vk_code)
      for event in self.events.values(): event(msg)
      return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    while self.isTurnOnKeyboardListener.is_set():
      while self.hook_id: PumpWaitingMessages()
      time.sleep(0.1)
      if self.isWorkingKeyboardListener.is_set():
        self.hook_id = user32.SetWindowsHookExW(win32con.WH_KEYBOARD_LL, keyboardHook, None, 0)
  
  def _run1(self):
    @WINFUNCTYPE(c_int, c_int, WPARAM, POINTER(KeyboardHookStruct))
    def keyboardHook(nCode, wParam, lParam):
      msg = {'pressed':True if wParam == 256 else False,'button':lParam.contents.vkCode} # win32con.WM_KEYDOWN
      for event in self.events.values(): event(msg)
      return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    while self.isTurnOnKeyboardListener.is_set():
      while self.hook_id: PumpWaitingMessages()
      time.sleep(0.1)
      if self.isWorkingKeyboardListener.is_set():
        self.hook_id = user32.SetWindowsHookExW(win32con.WH_KEYBOARD_LL, keyboardHook, None, 0)

  def _run2(self):
    @WINFUNCTYPE(c_int, c_int, WPARAM, POINTER(KeyboardHookStruct))
    def keyboardHook(nCode, wParam, lParam):
      vk_code = lParam.contents.vkCode
      key = VKEVENTS[vk_code] if vk_code in VKEVENTS else chr(vk_code)
      if wParam == 256: # win32con.WM_KEYDOWN = 256
        for event in self.on_press_events.values(): event(key)
      else:
        for event in self.on_release_events.values(): event(key)
        
      return user32.CallNextHookEx(None, nCode, wParam, lParam)
    
    while self.isTurnOnKeyboardListener.is_set():
      while self.hook_id: PumpWaitingMessages()
      time.sleep(0.1)
      if self.isWorkingKeyboardListener.is_set():
        self.hook_id = user32.SetWindowsHookExW(win32con.WH_KEYBOARD_LL, keyboardHook, None, 0)

class Button:
  left:int = 2
  right:int = 8
  middle:int = 32

class MouseController:
  def __init__(self) -> None:
    self.screenWidth = win32api.GetSystemMetrics(0)
    self.screenHeight = win32api.GetSystemMetrics(1)

  def flagLightEvent(self,flags:int=0,x:int=0,y:int=0,info0:int=0,info1:int=0):
    user32.mouse_event(flags, x, y, info0, info1)
  def flagEvent(self,
    x:int=None,y:int=None,MOUSEEVENTF_MOVE:bool=False,
    MOUSEEVENTF_LEFTDOWN:bool=False,MOUSEEVENTF_LEFTUP:bool=False,
    MOUSEEVENTF_RIGHTDOWN:bool=False,MOUSEEVENTF_RIGHTUP:bool=False,
    MOUSEEVENTF_MIDDLEDOWN:bool=False,MOUSEEVENTF_MIDDLEUP:bool=False,
    MOUSEEVENTF_WHEEL:bool=False,MOUSEEVENTF_ABSOLUTE:bool=False
  ):
    flags = 0
    warnPerfomanceMsgArgs = ''
    if x is None: x = 0
    else: warnPerfomanceMsgArgs+=f'x={x}, '
    if y is None: y = 0
    else: warnPerfomanceMsgArgs+=f'y={y}, '
    if MOUSEEVENTF_MOVE: 
      flags+=1
      warnPerfomanceMsgArgs+='MOUSEEVENTF_MOVE=True, '
    if MOUSEEVENTF_LEFTDOWN: 
      flags+=2
      warnPerfomanceMsgArgs+='MOUSEEVENTF_LEFTDOWN=True, '
    if MOUSEEVENTF_LEFTUP: 
      flags+=4
      warnPerfomanceMsgArgs+='MOUSEEVENTF_LEFTUP=True, '
    if MOUSEEVENTF_RIGHTDOWN: 
      flags+=8
      warnPerfomanceMsgArgs+='MOUSEEVENTF_RIGHTDOWN=True, '
    if MOUSEEVENTF_RIGHTUP: 
      flags+=16
      warnPerfomanceMsgArgs+='MOUSEEVENTF_RIGHTUP=True, '
    if MOUSEEVENTF_MIDDLEDOWN: 
      flags+=32
      warnPerfomanceMsgArgs+='MOUSEEVENTF_MIDDLEDOWN=True, '
    if MOUSEEVENTF_MIDDLEUP: 
      flags+=64
      warnPerfomanceMsgArgs+='MOUSEEVENTF_MIDDLEUP=True, '
    if MOUSEEVENTF_WHEEL: 
      flags+=2048
      warnPerfomanceMsgArgs+='MOUSEEVENTF_WHEEL=True, '
    if MOUSEEVENTF_ABSOLUTE: 
      flags+=32768
      warnPerfomanceMsgArgs+='MOUSEEVENTF_ABSOLUTE=True, '
      if x: x = 65536 * x // self.screenWidth + 1
      if y: y = 65536 * y // self.screenHeight + 1

    
    print(f'Instead: ```.flagEvent({warnPerfomanceMsgArgs[:-2]})```\nUse:     ```.flagLightEvent({flags}, {x}, {y}, {0}, {0})```')
    user32.mouse_event(flags, x, y, 0, 0)
    
  def move(self,dx:int=0,dy:int=0): user32.mouse_event(1, dx, dy, 0, 0)
  def moveAbsolute(self,pos:tuple[int, int]): win32api.SetCursorPos(pos)
  def clickLBAbsolute(self,pos:tuple[int, int]): win32api.Set
  
  def press(self,buttonID:Literal[2,8,32]): 
    "2 - LMB, 8 - RMB, 32 - MMB (DOWN)"
    user32.mouse_event(buttonID, 0, 0, 0, 0)
  def release(self,buttonID:Literal[4,16,64]):
    "4 - LMB, 16 - RMB, 64 - MMB (UP)"
    user32.mouse_event(buttonID, 0, 0, 0, 0)
  def click(self,buttonID:Literal[2,8,32]):
    "2 - LMB, 8 - RMB, 32 - MMB"
    user32.mouse_event(buttonID*3, 0, 0, 0, 0)
    
  def pressLB(self):   user32.mouse_event(2, 0, 0, 0, 0)
  def releaseLB(self): user32.mouse_event(4, 0, 0, 0, 0)
  def clickLB(self):   user32.mouse_event(6, 0, 0, 0, 0)  # 2+4=6
  def pressRB(self):   user32.mouse_event(8, 0, 0, 0, 0)
  def releaseRB(self): user32.mouse_event(16, 0, 0, 0, 0)
  def clickRB(self):   user32.mouse_event(24, 0, 0, 0, 0) # 8+16=24
  def pressMB(self):   user32.mouse_event(32, 0, 0, 0, 0)
  def releaseMB(self): user32.mouse_event(64, 0, 0, 0, 0)
  def clickMB(self):   user32.mouse_event(96, 0, 0, 0, 0) # 32+64=96
  def scrollAxisY(self,dy:int=0): user32.mouse_event(2048, 0, 0, dy, 0)
  def scrollAxisX(self,dx:int=0): user32.mouse_event(4096, dx, 0, 0, 0)
  
  @property
  def position(self): return win32api.GetCursorPos()


def CharToCode(Char:str):
  if Char in CodeByChar: return CodeByChar[Char]
  else: return ord(Char)

      
class KeyboardController:
  def PressByChar(self,key:str): user32.keybd_event(ord(key), 0, 0, 0)
  def ReleaseByChar(self,key:str): user32.keybd_event(ord(key), 0, 2, 0)
  def TapByChar(self,key:str):
    user32.keybd_event(ord(key), 0, 0, 0)
    user32.keybd_event(ord(key), 0, 2, 0)
  def PressByCode(self,key:int): user32.keybd_event(key, 0, 0, 0)
  def ReleaseByCode(self,key:int): user32.keybd_event(key, 0, 2, 0)
  def TapByCode(self,key:int):
    user32.keybd_event(key, 0, 0, 0)
    user32.keybd_event(key, 0, 2, 0)
  def Write(self,keys:str):
    for char in list(keys):
      mods, code = divmod(CharToCode(char), 0x100)
      if mods == 0:
        user32.keybd_event(code, 0, 0, 0)
        user32.keybd_event(code, 0, 2, 0)
      elif mods == 1:
        user32.keybd_event(16, 0, 0, 0)
        user32.keybd_event(code, 0, 0, 0)
        user32.keybd_event(code, 0, 2, 0)
        user32.keybd_event(16, 0, 2, 0)
        
      if code == 13: time.sleep(0.1)

