class car():
    def __init__(self,model,color,compile,price):
        self.model = model
        self.color = color
        self.compile = compile
        self.price = price

bmw = car("bmw","black","2022",100000000)
print(bmw.price)