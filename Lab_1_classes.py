import doctest
from typing import Union

class Construction:
    def __init__(self, external_load: Union[int, float], mass: Union[int, float], bearing_capacity: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Construction"

        :param external_load: Внешняя нагрузка, прикладываемая к конструкции с учетом знака, кН
        :param mass: Масса конструкции, кг
        :param bearing_capacity: Несущая способность конструкции, кН

        Примеры:
        >>> construction1 = Construction(20, 5, 30)  # Инициализация экземпляров класса
        >>> construction2 = Construction(external_load=-40, mass=7, bearing_capacity=35)
        """

        if not isinstance(external_load, (int, float)):
            raise TypeError("Внешняя нагрузка должно быть типа int или float")
        self.external_load = external_load

        if not isinstance(mass, (int, float)):
            raise TypeError("Масса должно быть типа int или float")
        if mass <= 0:
            raise ValueError("Масса конструкции должна быть положительным числом")
        self.mass = mass

        if not isinstance(bearing_capacity, (int, float)):
            raise TypeError("Несущая способность должно быть типа int или float")
        self.bearing_capacity = bearing_capacity
        if bearing_capacity <= 0:
            raise ValueError("Несущая спобность конструкции должна быть положительным числом")
        self.bearing_capacity = bearing_capacity

    def add_load(self, add_load: Union[int, float]) -> None:
        """
        Добавление значения новой внешней нагрузки с учетом знака

        :param add_load: Новая внешняя нагрузка, кН

        :return: Добавление новой нагрузки

        Примеры:
        >>> construction1 = Construction(20, 5, 30)
        >>> construction1.add_load(2)
        """
        if add_load == 0:
            raise ValueError("Добавленная внешняя нагрузка не должна быть равна нулю")
        if not isinstance(add_load, (int, float)):
            raise TypeError("Добавленная внешняя нагрузка должна быть типа int или float")
        ...

    def self_weight_load(self) -> Union[int, float]:
        """
        Расчет нагрузки от собственного веса конструкции

        :return: Нагрузка от собственного веса

        Примеры:
        >>> construction1 = Construction(20, 5, 30)
        >>> construction1.self_weight_load()
        """
        ...

    def bearing_capacity_check(self) -> bool:
        """
        Сравнение полной внешней нагрузки с несущей способностью конструкции

        :return: Проходит ли проверка по несушей способности

        Примеры:
        >>> construction1 = Construction(20, 5, 30)
        >>> construction1.bearing_capacity_check()
        """
        ...

class Mail:
    def __init__(self, name: str, number_of_sent_messages: int, number_of_received_messages: int):
        """
        Создание и подготовка к работе объекта "Mail"

        :param name: Наименование почтового ящика
        :param number_of_sent_messages: Количество отправленных сообщений
        :param number_of_received_messages: Количество полученных сообщений

        Примеры:
        >>> mail = Mail("maksim123@mail.ru", 10, 1000)  # Инициализация экземпляров класса
        """
        if not isinstance(name, str):
            raise TypeError("Наименование почтового ящика должно быть типа str")
        self.name = name

        if not isinstance(number_of_sent_messages, int):
            raise TypeError("Количество отправленных сообщений должно быть типа int")
        if number_of_sent_messages <= 0:
            raise ValueError("Количество отправленных сообщений должно быть положительным числом")
        self.number_of_sent_messages = number_of_sent_messages

        if not isinstance(number_of_received_messages, int):
            raise TypeError("Количество полученных сообщений должно быть типа int")
        if number_of_received_messages <= 0:
            raise ValueError("Количество полученных сообщений должно быть положительным числом")
        self.number_of_received_messages = number_of_received_messages

    def add_sent_messages(self, add_sent_messages: int) -> None:
        """
        Отправка новых сообщений

        :param add_sent_messages: Количество отправленных сообщений

        :return: Добавление количества отправленных сообщений

        Примеры:
        >>> mail = Mail("maksim123@mail.ru", 1, 2000)
        >>> mail.add_sent_messages(3)
        """
        if add_sent_messages < 0:
            raise ValueError("Количество отправленных сообщений - положительное число")
        if not isinstance(add_sent_messages, int):
            raise TypeError("Количество отправленных сообщений должно быть типа int")
        ...

    def add_received_messages(self, add_received_messages: int) -> None:
        """
        Получение новых сообщений

        :param add_received_messages: Количество полученных сообщений
        :raise ValueError: Если количество

        :return: Добавление количества полученных сообщений

        Примеры:
        >>> mail = Mail("maksim123@mail.ru", 12, 1897)
        >>> mail.add_received_messages(50)
        """
        if add_received_messages < 0:
            raise ValueError("Количество полученных сообщений - положительное число")
        if not isinstance(add_received_messages, int):
            raise TypeError("Количество полученных сообщений должно быть типа int")
        ...

class PhotoCamera:
    def __init__(self, volume: int, taken_pictures: int, volume_of_image):
        """
        Создание и подготовка к работе объекта "PhotoCamera"

        :param volume: Объем памяти фотоаппарата, МБ
        :param taken_pictures: Количество сделанных снимков, шт
        :param volume_of_image: Объем памяти, занимаемой одной фотографией, МБ

        Примеры:
        >>> mail = PhotoCamera(256, 10, 1)  # Инициализация экземпляров класса
        """
        if not isinstance(volume, int):
            raise TypeError("Объем памяти фотоаппарата должен быть типа int")
        if volume <= 0:
            raise ValueError("Объем памяти фотоаппарата должен быть больше нуля")
        self.volume = volume

        if not isinstance(taken_pictures, int):
            raise TypeError("Количество сделанных фотографий должно быть int")
        if taken_pictures < 0:
            raise ValueError("Количество сделанных фотографий должно быть положительным числом")
        self.taken_pictures = taken_pictures

        if not isinstance(volume_of_image, int):
            raise TypeError("Вес одной фотографии должен быть int")
        if volume_of_image <= 0:
            raise ValueError("Вес одной фотографии должен быть больше нуля")
        self.volume_of_image = volume_of_image
    def is_volume_full(self) -> bool:
        """
        Функция, которая проверяет, существуют ли сохраненные снимки в памяти фотоаппарата
        :return: Существуют ли сохраненные снимки в памяти фотоаппарата

        Примеры:
        >>> photo_camera = PhotoCamera(128, 10, 5)
        >>> photo_camera.is_volume_full()
        """
        ...
    def make_photo(self) -> None:
        """
        Функция для создания снимка

        :raise ValueError: Если память фотоаппарата не способна вместить еще одну фотографию, возвращается ошибка

        Примеры:
        >>> photo_camera = PhotoCamera(512, 50, 4)
        >>> photo_camera.make_photo()
        """
        ...



if __name__ == "__main__":
    doctest.testmod() # Тестирование примеров, которые находятся в документации
    pass
