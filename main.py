import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import requests


class MapApp(QMainWindow):
    def __init__(self, coords, size):
        super().__init__()
        uic.loadUi('map.ui', self)
        self.setWindowTitle('Карта')
        self.setGeometry(400, 400, 600, 600)
        self.init_map(coords, size)

    def init_map(self, coords, size):
        response = requests.get(f'https://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={size[0]},{size[1]}&l=map')
        with open('img/map.jpg', "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap('img/map.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 600)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    coords = input('Введите координаты места (через пробел): ').split(' ')
    size = input('Введите маштаб карты (два числа через пробел): ').split(' ')
    app = QApplication(sys.argv)
    main_app = MapApp(coords, size)
    main_app.show()
    sys.excepthook = except_hook

    sys.exit(app.exec_())