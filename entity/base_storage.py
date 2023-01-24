

from entity.abstract_storage import AbstractStorage
from exceptions import NotEnoughProduct, NotEnoughSpace

class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, amount: int) -> None:
        # Todo: Проверить, что места достаточно
         if self.get_free_space() < amount:
             raise NotEnoughSpace

        # Todo: Добавить товар
         if name in self.__items:
             self.__items[name] += amount
         else:
             self.__items[name] = amount

    def remove(self, name: str, amount: int) -> None:
        # Todo: Проверить, есть ли такой товар
         if name not in self.__items or self.__items[name] < amount:
             raise NotEnoughSpace


        # Todo: Вычислить необходимое количество товара. Если товара станет 0 удалить товар из списка
         self.__items[name] -= amount
         if self.__items[name] == 0:
             self.__items.pop(name)

    def get_free_space(self) -> int:
        # Todo: Посчитать сумму значений в словаре __items. Вычесть ее из __capacity
         return self.__capacity - sum(self.__items.values())


    def get_items(self) -> Dict[str, int]:
        return self.__items



    def get_unique_items_count(self):
        return len(self.__items)

