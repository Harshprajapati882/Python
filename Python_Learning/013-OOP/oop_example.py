"""OOP example demonstrating classes, inheritance, properties, and special methods."""


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name!r}, age={self.age})"

    def birthday(self):
        self.age += 1


class Employee(Person):
    def __init__(self, name: str, age: int, role: str, salary: float):
        super().__init__(name, age)
        self.role = role
        self._salary = salary

    def __repr__(self):
        return f"Employee({self.name!r}, {self.age}, {self.role!r})"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError('salary must be >= 0')
        self._salary = value

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['name'], data.get('age', 0), data.get('role', ''), data.get('salary', 0.0))

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18


if __name__ == '__main__':
    e = Employee('Alice', 30, 'Engineer', 90000)
    print(e)
    print('repr:', repr(e))
    print('is adult:', Employee.is_adult(e.age))
    e.birthday()
    print('after birthday:', e.age)
    e.salary = 95000
    print('salary:', e.salary)
