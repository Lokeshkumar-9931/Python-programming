class myclass:

    def __init__(self,value):
        self._value=value

    def show(self):
       print(f"value is {self._value}")   
            
    @property  #it is getter 
    def ten_value(self):
      return 10* self._value  
  
    @ten_value.setter   #it is setter
    def ten_value(self,new_value):
      self._value=new_value/10  

obj=myclass(10)
obj.ten_value=67
obj.show()
print(obj.ten_value)
      