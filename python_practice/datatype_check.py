def iterdict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        elif isinstance(v, list):
            for each_item in v:
                iterdict(each_item)
        elif v and type(v) != str:
            d.update({k: str(v)})
    return d

import time
inp_dict = {'NIC': [{'subsystemId': 'None', 'vendorId': 5555, 'version': None},
                    {'subsystemId': None, 'vendorId': 'None', 'version': '3.4'}], 'BIOS': 'None', 'BMC': None}
t1 = time.time()
a = iterdict(inp_dict)
t2 = t1-time.time()
print("time",t2)
print("result", a)


a = 2

while a:
    print("now a", a)
    a-=1
    if a>0:
        continue
    print("hello", a)