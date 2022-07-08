class Snake:
    def introduction(self,name,color,age):
        self.name=name
        self.color=color
        self.age=age
        print(f'{self.name}--{self.color}--{self.age}')
vipers=Snake()
python=Snake()
vipers.introduction("Vipers","Green","30yrs")
python.introduction("Python","Brown","15yrs")

