from typing import Dict

def sort_dic(d: Dict):
   lv = []
   lk = []
   for key, val in d.items():
       lk.append(key)
       lv.append(val) 

   print(lk)  
   print(lv)


def create_dic():
    d1 = {
        'key-1': 1,
        'key-2': 2,
        'key-3': 3,
    }

    d2 = {
        'key-4': 4,
        'key-5': 5,
        'key-6': 6,
    }

    l = [d1, d2]

    for el in l:
        sort_dic(el)
    


if __name__ == '__main__':
    create_dic()





