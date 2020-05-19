import re
# Define command
# Actions: 4 bits  
action_dict = {
    'Bat'       : 0x0,
    'Tat'       : 0x1,
    'SangHon'   : 0x2,
    'MoDi'      : 0x3,
    'ToiHon'    : 0x4,
    'Chuyen'    : 0x5,
    'Len'       : 0x6,
    'Xuong'     : 0x7,
    'KeoLen'    : 0x8,
    'KeoXuong'  : 0x9,
    'Dong'      : 0xa,
    'Mo'        : 0xb
}

# Objects: 4 bits
objs_dict = {
    'Den'       :0x0,
    'Tivi'      :0x1,
    'Quat'      :0x2,
    'Bep'       :0x3,
    'RemCua'    :0x4,
    'ThangMay'  :0x5,
    'Cua'       :0x6
}

# Id: 6 bits
def get_cmd(text):
    obj_pattern = re.compile(r'(Den|Quat|Tivi|Bep|RemCua|ThangMay)$')
    match = re.search(obj_pattern, text)
    if match:
        text = match.group(1)
    pattern = re.compile(r'^(Den|Quat|Tivi|Bep|RemCua|ThangMay)\D*(30|[12][0-9]|[1-9]).*(Bat|Tat|SangHon|MoDi|ToiHon|Chuyen|Len|Xuong|KeoLen|KeoXuong|Dong|Mo)$')
    match = re.search(pattern, text)
    if match:
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        cmd_code = (objs_dict[match.group(1)] << 10) + (action_dict[match.group(3)] << 6) + int(match.group(2))
        res = match.group(1) + match.group(2) + match.group(3)
        text = ''
        return cmd_code, res, text
    else:
        pattern = re.compile(r'^(Den|Quat|Tivi|Bep|RemCua|ThangMay).*(Bat|Tat|SangHon|MoDi|ToiHon|Chuyen|Len|Xuong|KeoLen|KeoXuong|Dong|Mo)$')
        match = re.search(pattern, text)
        if match:
            print(match.group(1))
            print(match.group(2))
            cmd_code = (objs_dict[match.group(1)] << 10) + (action_dict[match.group(2)] << 6)
            res = match.group(1) + match.group(2)
            text = ''
            return cmd_code, res, text
        else:
            print("not match")
            res = ''
            return -1, res, text
# text = "QuatXuongTat"
# code, res, text = get_cmd(text)
# print(hex(code))
# print(res)
# print(text)