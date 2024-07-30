class Calculator: 
    
    def add(self, num_1: float, num_2: float) -> float:
        return num_1 + num_2
    
    def sustract(self, num_1: float, num_2: float) -> float:
        return num_1 - num_2
    
    def multiply(self, num_1: float, num_2: float) -> float:
        return num_1 * num_2
     
    def divide(self, num_1: float, num_2: float) -> float or str:
      if num_2 == 0:
          return "Cannot divide by 0!"
      
        return num_1 / num_2

    
