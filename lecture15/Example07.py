from typing import Dict

def sort_dic(d: Dict):
   lv = []
   lk = []
   for key, val in d.items():
       lk.append(key)
       lv.append(val) 

   print(sorted(lk))  
   print(sorted(lv))


def create_dic():
    d1 = {
        'key-3': 3,
        'key-2': 2,
        'key-1': 1,
    }

    d2 = {
        'key-6': 6,
        'key-5': 5,
        'key-4': 4,
    }

    d3 = {
        'key-15': 15,
        'key-3': 3,
        'key-2': 2,
        'key-9': 9,
        'key-12': 12,

    }

    l = [d1, d2, d3]

    for el in l:
        sort_dic(el)
    


if __name__ == '__main__':
    create_dic()





