class DataBase:
    pk = 1
    title = 'Классы и объекты'
    author = 'Сергей Балакирев'
    views = 14356
    comments = 12


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


class Car:
    pass


# setattr(Class, 'attribute', value) - добавляет атрибут и его значение в указанный класс

setattr(Car, 'model', 'Тойота')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')


# print(Car.__dict__['color'])


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


# getattr(Class, attribute, returned_value(optional)) - получает значение атрибута, если он существует и None или
# значение в обратной ситуации
# print(getattr(Notes, 'author', False))


class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Италия'
tb1.days = 5

TravelBlog.total_blogs += 1


# print(tb1.__dict__)


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
del fig1.color

#print(*fig1.__dict__.keys())


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'
p1 = Person()
#print(hasattr(p1.__dict__, 'job'))


class MediaPlayer:
    def open(self, file):
        self.filename = file
    def play(self):
         print(f'Воспроизведение {self.filename}')

media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open('filemedia1')
#media1.play()

media1.open('filemedia2')
#media1.play()


#print(media1.__dict__, media2.__dict__, sep='\n')

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        [print(i) for i in self.__dict__['data'][Graph.LIMIT_Y[0]:Graph.LIMIT_Y[-1]] if i in range()]


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
