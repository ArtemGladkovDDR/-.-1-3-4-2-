from abc import ABC, abstractmethod


class Table(ABC):
    """Абстрактный класс для стола."""

    def __init__(self, material: str, color: str, legs: int) -> None:
        """
        Инициализация класса Table.

        :param material: Материал стола.
        :param color: Цвет стола.
        :param legs: Количество ножек стола.

        :raises ValueError: Если количество ножек меньше 0.
        """
        if legs < 0:
            raise ValueError("Количество ножек не может быть отрицательным.")

        self.material = material
        self.color = color
        self.legs = legs

    @abstractmethod
    def place_item(self, item: str) -> None:
        """
        Поместить предмет на стол.

        :param item: Название предмета для размещения.
        """
        pass

    @abstractmethod
    def clean(self) -> None:
        """Очистить стол от грязи и пыли."""
        pass


class Tree(ABC):
    """Абстрактный класс для дерева."""

    def __init__(self, species: str, height: float, age: int) -> None:
        """
        Инициализация класса Tree.

        :param species: Вид дерева.
        :param height: Высота дерева в метрах.
        :param age: Возраст дерева в годах.

        :raises ValueError: Если высота или возраст дерева меньше 0.
        """
        if height < 0 or age < 0:
            raise ValueError("Высота и возраст не могут быть отрицательными.")

        self.species = species
        self.height = height
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличить возраст дерева.

        :param years: Количество лет, на которое увеличить возраст.
        """
        pass

    @abstractmethod
    def drop_leaves(self) -> None:
        """Сбрасывать листья дерева в осенний период."""
        pass


class SocialNetwork(ABC):
    """Абстрактный класс для социальной сети."""

    def __init__(self, name: str, user_limit: int) -> None:
        """
        Инициализация класса SocialNetwork.

        :param name: Название социальной сети.
        :param user_limit: Максимальное количество пользователей.

        :raises ValueError: Если лимит пользователей меньше 0.
        """
        if user_limit <= 0:
            raise ValueError("Лимит пользователей должен быть положительным.")

        self.name = name
        self.user_limit = user_limit
        self.users = []

    @abstractmethod
    def add_user(self, username: str) -> None:
        """
        Добавить пользователя в социальную сеть.

        :param username: Имя пользователя для добавления.
        """
        pass

    @abstractmethod
    def remove_user(self, username: str) -> None:
        """
        Удалить пользователя из социальной сети.

        :param username: Имя пользователя для удаления.
        """
        pass
