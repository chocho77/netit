class Calculator:
    _a: int 
    _b: int

    def __init__(self, a, b):
        self._a = a
        self._b = b
    
    @property
    def a(self)->int:
        return self._a
    
    @a.setter
    def a(self, value)->None:
        self._a = value
    
    @property
    def b(self)->int:
        return self._b
    
    @b.setter
    def b(self, value)->None:
        self._b = value
    

       
    
calc = Calculator(1, 2)
calc1 = Calculator(2, 3)

print(f"ob1 a : {calc.a}, ob1 b : {calc.b}")
print(f"ob2 a : {calc1.a}, ob2 b : {calc1.b}")

print()

calc.a = 2
calc.b = 2
calc1.a = 5
calc1.b = 5

print(f"ob1 a : {calc.a}, ob1 b : {calc.b}")
print(f"ob2 a : {calc1.a}, ob2 b : {calc1.b}")


