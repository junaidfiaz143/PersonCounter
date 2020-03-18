import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from win32api import GetSystemMetrics

# print("Width =", GetSystemMetrics(0))
# print("Height =", GetSystemMetrics(1))

class MyApp(QWidget):

	def __init__(self):
		super().__init__()


		self.initUI()

	def closeEvent(self, event):

		QMessageBox.move(self, GetSystemMetrics(1)//2, 0)

		quit_msg = "Are you sure you want to exit the program?"
		reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def initUI(self):

		self.web = QWebEngineView()
		self.web.setWindowTitle("Person Counter")
		# self.web.setWindowIcon(QIcon("resources/icons/xray.ico"))
		self.web.load(QUrl.fromLocalFile("/index.html"))
		self.web.showMaximized()
		# self.web.setFixedSize(1366, 768)
		self.web.show()

		self.web.closeEvent = self.closeEvent

if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	my_app = MyApp()
	sys.exit(app.exec_())