from bs4 import BeautifulSoup
import requests
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BBC News Headlines')
        self.setGeometry(100,100,750, 900)

        self.label = QLabel('Click the button to get the latest BBC News headlines', self)
        self.label.move(220, 50)
        self.label.resize(700, 700)



        self.button = QPushButton('Get Headlines', self)
        self.button.move(280, 850)
        self.button.clicked.connect(self.bbc_news_scraper)

    def bbc_news_scraper(self):
        headers={'User-Agent':'Chrome/111.0.5563.65'}
        request = requests.get('https://www.bbc.com/news', headers=headers)
        html = request.content
        soup = BeautifulSoup(html, 'html.parser')

        news_list = []

        for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
            news_title = h.contents[:]
            if news_title not in news_list:
                    news_list.append(news_title)

        headlines = '\n'.join([f'{i+1}. {j}' for i,j in enumerate(news_list)])
        self.label.setText(headlines)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())