import re
import threading 
import cmd_excute
from itertools import combinations 
from PyQt5.QtCore import QObject, pyqtSignal
# Define command
# Actions: 4 bits  

#  Lệnh + đối tượng + vị trí
#  Đối tượng + vị trí + lệnh
#  Lệnh + đối tượng
#  Đối tượng + lệnh + giá trị

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class UpdateUI(QObject):
    changedValue = pyqtSignal(str, bool)

cmd_dict = {
    # Lenh
    'Bat'       : 0,
    'Tat'       : 0,
    'Sang Hon'   : 0,
    'Mo Di'      : 0,
    'Toi Hon'    : 0,
    'Chuyen'    : 0,
    'Len'       : 0,
    'Xuong'     : 0,
    'Keo Len'    : 0,
    'Keo Xuong'  : 0,
    'Dong'      : 0,
    'Mo'        : 0,
    'Tang'      : 0,
    'Giam'      : 0,

    # Doi tuong
    'Den'       : 1,
    'Tivi'      : 1,
    'Quat'      : 1,
    'Rem Cua'    : 1,
    'Thang May'  : 1,
    'Cua'       : 1,

    # Vi tri
    'Phong Khach'     : 2,
    'Phong Ngu'       : 2,
    'Phong Bep'       : 2,
    'Phong Tam'       : 2,

    # Gia tri
    'Do Sang'    : 3,

    # So
    '1'         : 4,
    '2'         : 4,
    '3'         : 4,
    '4'         : 4,
    '5'         : 4,
    '6'         : 4,
    '7'         : 4,
    '8'         : 4,
    '9'         : 4,
    '10'        : 4,
    '11'        : 4,
    '12'        : 4,
    '13'        : 4,
    '14'        : 4,
    '15'        : 4,
    '16'        : 4,
    '17'        : 4,
    '18'        : 4,
    '19'        : 4,
    '20'        : 4,
    '21'        : 4,
    '22'        : 4,
    '23'        : 4,
    '24'        : 4,
    '25'        : 4,
    '26'        : 4,
    '27'        : 4,
    '28'        : 4,
    '29'        : 4,
    '30'        : 4
}

# Cau lenh thuc te

rules = [[0,3,1,2],
         [0,1,2],
         [1,2,0],
        #  [0,1],
         [1,0,4]]
cmd = []
res = []
conn_ui = UpdateUI()
def sublistExists(list1, list2):
    comb = combinations(list1, len(list2))
    # print(list(comb))
    if tuple(list2) in list(comb):
        return True
    else:
        return False
def get_cmd(text):
    global res
    global cmd
    res.append(text)
    cmd.append(cmd_dict[text])
    for rule in rules:
        if sublistExists(cmd,rule):
            res2 = ''
            code = 0x0
            for i in rule:
                start = cmd.index(i)
                seg = res[start]
                cmd = cmd[start:]
                res = res[start:]
                res2 +=  seg + ' '
                if i == 0:
                    code += cmd_excute.action_code[seg] << 8
                elif i == 1:
                    code += cmd_excute.device_code[seg] << 20
                elif i == 2:
                    code += cmd_excute.id_code[seg] << 16
                elif i == 4:
                    code += int(seg)
            cmd_excute.send_cmd(code)
            res.clear()
            cmd.clear()
            conn_ui.changedValue.emit(res2, True)
            return res2
    print("                                                                                  " + ' '.join(res))
    conn_ui.changedValue.emit(' '.join(res), False)
    return ''
def reset_cmd():
    # threading.Timer(20.0, reset_cmd).start()
    res.clear()
    cmd.clear()
# reset_cmd()
if __name__ == "__main__":
    import time
    time.sleep(2)
    text = "Den"
    result= get_cmd(text)
    print("==>",result)
    text = "Phong Khach"
    result= get_cmd(text)
    print("==>",result)
    text = "Bat"
    result= get_cmd(text)
    print("==>",result)
    
    