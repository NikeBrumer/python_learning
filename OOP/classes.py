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
# data_graph = list(map(int, input().split()))


# здесь создаются объекты классов и вызываются нужные методы

# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(False)
# gr.show_table()

class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots

    def get_config(self):
        "returns information of components"
        return f''


# здесь пишите программу
class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

cart.add(TV('LG', 10000))
cart.add(TV('Lenovo', 15000))
cart.add(Table('Nike', 5000))
cart.add(Notebook('HP', 40000))
cart.add(Notebook('Asus', 60000))
cart.add(Cup('Black', 500))


# здесь объявляйте класс SingletonFive
class SingletonFive:
    counter = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.counter < 6:
            cls.counter += 1
            cls.__instance = super().__new__(cls)
            return cls.__instance
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять


# здесь пишется программа
class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines  # число мин вокруг клетки
        self.mine = mine  # наличие мины в текущей клетке
        self.fl_open = True  # состояние клетки (закрыта/открыта)


class GamePole:
    def __init__(self, N, M):
        self.N = N  # размер поля N x N
        self.M = M  # количество мин
        self.pole = [[Cell() for j in range(self.N)] for i in range(self.N)]
        self.init()

    def init(self):
        from random import randint

        for _ in range(self.M):
            i = randint(0, self.N - 1)
            j = randint(0, self.N - 1)
            if not self.pole[i][j].mine:
                self.pole[i][j].mine = True

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    for i, j in indx:
                        if 0 <= x + i < self.N and 0 <= y + j < self.N:
                            if self.pole[x + i][y + j].mine:
                                self.pole[x][y].around_mines += 1

    def show(self):
        [print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', i)) for i in self.pole]


pole_game = GamePole(10, 12)
# pole_game.show()


from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size):
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError("некорректное поле name")
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 2 < len(name) < 50:
            for i in name:
                if i not in cls.CHARS_CORRECT:
                    break
            else:
                return True
        return False


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size):
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError("некорректное поле name")
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 2 < len(name) < 50:
            for i in name:
                if i not in cls.CHARS_CORRECT:
                    break
            else:
                return True
        return False


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин", 5), PasswordInput("Пароль", 10))
html = login.render_template()


############################################################################### 5/28/2023
class Router:

    def __init__(self):
        self.servers = {}
        self.buffer = []

    def link(self, server):
        server.status = True
        self.servers[server] = server.status
        server.router = self

    def unlink(self, server):
        server.status = False
        self.servers[server] = server.status

    def send_data(self):
        online = list(filter(lambda x: x.status, self.servers))
        for inst in self.buffer[:]:
            for serv in online:
                if inst.ip == serv.ip:
                    serv.buffer.append(inst)
                    self.buffer.remove(inst)


class Server:
    ip_serv = 0

    def __new__(cls, *args, **kwargs):
        cls.ip_serv += 1
        return super().__new__(cls)

    def __init__(self):
        self.status = False
        self.ip = Server.ip_serv
        self.buffer = []
        self.router = None

    def send_data(self, data):
        if self.status:
            self.router.buffer.append(data)

    def get_data(self):
        res = self.buffer
        self.buffer = []
        return res

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()

ser = Server()
ser2 = Server()

router.link(ser)
router.link(ser2)

ser.send_data(Data('abc', ser2.get_ip()))
router.send_data()

