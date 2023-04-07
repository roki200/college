class Person:
  def __init__(self, name, surname, age, salary):
    self.name = name
    self.surname = surname
    self.age = age
    self.__salary = salary
  @property
  def get_salary(self):
    return self.__salary

class Worker(Person):
  def __init__(self, name, surname, age, salary, department):
    super().__init__(name, surname, age, salary)
    self.department = department
  @property
  def get_salary(self):
    return self._Person__salary
  def zp(self, percent):
    self.__salary += self.__salary * percent / 100

class Director(Worker):
    def __init__(self, name, surname, age, salary, department, company_name):
        super().__init__(name, surname, age, salary, department)
        self.__company_name = company_name
    
    def make_an_appointment(self, participant):
        print(f"Заплонирована встреча с {participant}")
    
    @property
    def get_company_name(self):
        return self.__company_name

person = Person("Вася", "Пупкин", 19, 800)
#person.get_salary = 600  #Пытаемся изменить зарплату - не получается, так как атрибут приватный
print(person)
tom = Worker('Tom', 'Test', 21, 25000, 'Development')
print(tom.get_salary)
director = Director('Павел', "Дуров", 38, 50000, 'Management', "Telegram Inc.")
participant = "Роки"
director.make_an_appointment(participant)
print(director) 
#director.get_company_name = "XYZ Corp." # вызовет ошибку, т.к. атрибут является защищенным