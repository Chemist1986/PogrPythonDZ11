import time

class MyString:
    def __init__(self, value, author):
       

        self.value = value
        self.author = author
        self.creation_time = time.time()

    def get_author(self):
        return self.author

    def get_creation_time(self):
        return self.creation_time

    def __str__(self):
        return f"Строка: {self.value}, Автор: {self.author}, Время создания: {self.creation_time}"


my_str = MyString("Пример строки", "John Doe")
print(my_str)  
print(my_str.get_author())  
print(my_str.get_creation_time())  