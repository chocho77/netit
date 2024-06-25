def ouput_data(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs["name"])
    print(kwargs["num"])
    print(kwargs["b"])
    print(kwargs)

ouput_data(1, 2 , 3, name="John Smith", num = 5, b = True)
ouput_data(1, 2 , 3 , 4, name="Chavdar", num = 6, b = False)





