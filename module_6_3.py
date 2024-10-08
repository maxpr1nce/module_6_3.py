class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел (отсылка)

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полета на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализируем родительский класс Horse
        Eagle.__init__(self)  # Инициализируем родительский класс Eagle

    def move(self, dx, dy):
        self.run(dx)  # Запускаем метод run для изменения дистанции
        self.fly(dy)  # Запускаем метод fly для изменения высоты

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение в виде кортежа

    def voice(self):
        print(self.sound)  # Печатаем звук, унаследованный от класса

# Пример использования классов
pegasus = Pegasus()
pegasus.voice()  # Печатает звук пегаса, унаследованный от Eagle
pegasus.move(10, 20)  # Пегас движется на 10 по x и на 20 по y
print(pegasus.get_pos())  # Выводит текущее положение: (10, 20)