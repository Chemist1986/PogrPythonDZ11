class Archive:
    number_archive = []
    string_archive = []

    def __init__(self, number, string):
       
        self.number = number
        self.string = string
        self.number_archive.append(number)
        self.string_archive.append(string)

    def get_number_archive(self):
        return self.number_archive

    def get_string_archive(self):
        return self.string_archive

    def __str__(self):
        return f"Число: {self.number}, Строка: {self.string}"



archive1 = Archive(42, "Hello")
print(archive1)  

archive2 = Archive(123, "World")
print(archive2)  
print(archive1.get_number_archive())  
print(archive1.get_string_archive())  