class Hui:
    def __init__(self, num):
        self.num = num


lst = [Hui(1), Hui(5), Hui(1), Hui(1)]
print(lst)
for i in lst[:]:
    if i.num == 5:
        lst.remove(i)
print(lst)