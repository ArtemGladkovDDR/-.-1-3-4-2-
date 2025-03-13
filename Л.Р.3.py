class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажных книг."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive integer.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, Количество страниц: {self.pages}"


class AudioBook(Book):
    """Класс для аудиокниг."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Duration must be a positive number.")
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self.duration:.2f} часов"


paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

print(paper_book)  # Вывод: Книга Война и мир. Автор Лев Толстой, Количество страниц: 1225
print(audio_book)  # Вывод: Книга 1984. Автор Джордж Оруэлл, Продолжительность: 11.50 часов

