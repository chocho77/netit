def foo(*args, **kw):
    print(args, kw)


foo(1,2,3, name="Ivan" surname="Ivanov") #run-time error

