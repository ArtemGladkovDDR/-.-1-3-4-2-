class Animal:
    """Базовый класс для животных."""

    def __init__(self, name: str, species: str) -> None:
        """
        Инициализация базового класса животного.

        :param name: Имя животного.
        :param species: Вид животного.
        """
        self._name = name  # Инкапсуляция для недопущения изменений имени
        self._species = species  # Инкапсуляция для недопущения изменений вида

    @property
    def name(self) -> str:
        return self._name

    @property
    def species(self) -> str:
        return self._species

    def make_sound(self) -> str:
        """Возвращает звук, который издает животное. Метод должен переопределяться в дочерних классах."""
        return "Джет звук животного."

    def __str__(self) -> str:
        return f"{self.species} по имени {self.name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r})"


class Dog(Animal):
    """Класс для собак."""

    def __init__(self, name: str, breed: str) -> None:
        """
        Инициализация собаки, расширяя базовый класс Animal.

        :param name: Имя собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, species="Собака")
        self._breed = breed  # Инкапсуляция для недопущения изменений породы

    @property
    def breed(self) -> str:
        return self._breed

    def make_sound(self) -> str:
        """
        Переопределение метода make_sound для возвращения звука собаки.

        :return: Звук, который издает собака.
        """
        return "Гав!"  # Собаки лают

    def __str__(self) -> str:
        return f"{super().__str__()}, порода: {self.breed}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, breed={self.breed!r})"


class Cat(Animal):
    """Класс для кошек."""

    def __init__(self, name: str, color: str) -> None:
        """
        Инициализация кошки, расширяя базовый класс Animal.

        :param name: Имя кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, species="Кошка")
        self._color = color  # Инкапсуляция для недопущения изменений цвета

    @property
    def color(self) -> str:
        return self._color

    def make_sound(self) -> str:
        """
        Переопределение метода make_sound для возвращения звука кошки.

        :return: Звук, который издает кошка.
        """
        return "Мяу!"  # Кошки мяукают

    def __str__(self) -> str:
        return f"{super().__str__()}, цвет: {self.color}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, color={self.color!r})"


if __name__ == "__main__":
    # Создание объектов для демонстрации
    dog = Dog(name="Бэлла", breed="Лабрадор")
    cat = Cat(name="Мурзик", color="Черный")

    print(dog)  # Выводит: Собака по имени Бэлла, порода: Лабрадор
    print(dog.make_sound())  # Выводит: Гав!

    print(cat)  # Выводит: Кошка по имени Мурзик, цвет: Черный
    print(cat.make_sound())  # Выводит: Мяу!
