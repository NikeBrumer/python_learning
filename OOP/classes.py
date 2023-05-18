# class DataBase:
#     pk = 1
#     title = 'Классы и объекты'
#     author = 'Сергей Балакирев'
#     views = 14356
#     comments = 12
#
#
# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
#
#
# class Car:
#     pass
#
#
# # setattr(Class, 'attribute', value) - добавляет атрибут и его значение в указанный класс
#
# setattr(Car, 'model', 'Тойота')
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111УУ77')
#
#
# # print(Car.__dict__['color'])
#
#
# class Notes:
#     uid = 1005435
#     title = "Шутка"
#     author = "И.С. Бах"
#     pages = 2
#
#
# # getattr(Class, attribute, returned_value(optional)) - получает значение атрибута, если он существует и None или
# # значение в обратной ситуации
# # print(getattr(Notes, 'author', False))
#
#
# class TravelBlog:
#     total_blogs = 0
#
#
# tb1 = TravelBlog()
# tb1.name = 'Италия'
# tb1.days = 5
#
# TravelBlog.total_blogs += 1
#
#
# # print(tb1.__dict__)
#
#
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
# del fig1.color
#
#
# # print(*fig1.__dict__.keys())
#
#
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
#
# p1 = Person()
#
#
# # print(hasattr(p1.__dict__, 'job'))
#
#
# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# # media1.play()
#
# media1.open('filemedia2')
#
#
# # media1.play()
#
#
# # print(media1.__dict__, media2.__dict__, sep='\n')
#
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         [print(i) for i in self.__dict__['data'][Graph.LIMIT_Y[0]:Graph.LIMIT_Y[-1]] if i in range()]
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# # graph_1.draw()

class Translator:
    def add(self, eng, rus):
        if 'dict_words' not in self.__dict__:
            self.dict_words = {}
        if eng not in self.dict_words:
            self.dict_words[eng] = []
        if rus not in self.dict_words[eng]:
            self.dict_words[eng].append(rus)

    def remove(self, eng):
        self.dict_words.pop(eng)

    def translate(self, eng):
        return self.dict_words[eng] if eng in self.dict_words else None


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('go', 'ходить')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')


# print(*tr.translate('go'))

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        lst_points = (self.a, self.b, self.c)
        if not all(map(lambda x: type(x) in (int, float), lst_points)):
            return 1
        if not all(map(lambda x: x > 0, lst_points)):
            return 1
        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.b + self.a:
            return 2
        return 3


# a, b, c = map(int, input().split())  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())

class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show:
            print(' '.join(map(str, self.data)))
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
