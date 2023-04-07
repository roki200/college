from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
roki = Person("Roki ", 17)
print(roki)
