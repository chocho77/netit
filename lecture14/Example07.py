def full_name(first: str,last: str,middle: str = None):
    if middle is not None:
        print(f'{first} {middle} {last}')
    else:
        print(f"{first} {last}")

full_name("Chavdar", "Momchilov", "Ventsislavov")
full_name(first="Chavdar", middle="Ventsislavov", last="Momchilov")
full_name("Chavdar", "Momchilov")
full_name(first="Georgi",middle="Ivanov",last="Petrov")
full_name(first="Georgi", last="Petrov")
