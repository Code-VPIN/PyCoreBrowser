import sys
from PyQt5.QtCore import * #dependencies
from PyQt5.QtWidgets import * #dependencies
from PyQt5.QtWebEngineWidgets import * #dependencies


# Main window code
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar =QToolBar()
        self.addToolBar(navbar)


        #back_btn code
        back_btn = QAction('Back', self)
        back_btn. triggered.connect(self.browser.back)
        navbar.addAction(back_btn)



        #forward_btn code
        forward_btn = QAction('Forward',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        #Reload_btn code
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        #Home_btn code
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)


        #Url_Bar code
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        #Url Update Code in URL_BAR
        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('PyCore Browser')
window = MainWindow()
app.exec_()