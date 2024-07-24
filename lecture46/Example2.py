def main(x, y, *args, **kw):
 print(x)
 print(y)
 print(args)
 print(kw) # print dic
 print(*kw) # print only keys in dic

args = (5, 6)
kw = {'c':7, 'd':8}
main(3, 4, *args,**kw)



