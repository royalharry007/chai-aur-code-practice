class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.__salary= salary
    
    def show(self):
        print(self.__salary)

        
        
emp = Employee("harry","100000") # creating the object of the class 
print(emp.name)
emp.show()
print(emp.salary)  

#encapsulation are the way to make the make only accesible inside the class not accesible 
#outside the class 
