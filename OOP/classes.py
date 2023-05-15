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

print(Car.__dict__['color'])


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


# getattr(Class, attribute, returned_value(optional)) - получает значение атрибута, если он существует и None или
# значение в обратной ситуации
print(getattr(Notes, 'author', False))
