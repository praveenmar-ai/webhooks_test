"""inp = int(input("enter the num"))
for ite in range(0,inp):
    for j in range(0,ite+1):
        print("*" ,end = '')
    print()
"""

"""def function(*kids):
    k = kids[:]
    print("The younger childern are : " ,k  )
    l = type(k)
    print(l)


function(1,2,3,4,5,6,7,8,9)"""


# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 


class Window(QMainWindow): 
	def __init__(self): 
		super().__init__() 

		# setting title 
		self.setWindowTitle("Python ") 

		# setting geometry 
		self.setGeometry(100, 100, 600, 400)
		self.show()

		# calling method 
		self.UiComponents() 

		# showing all the widgets 
		 

	# method for widgets 
	def UiComponents(self): 

		# creating a push button 
		button = QPushButton("CLICK", self) 

		# setting geometry of button 
		button.setGeometry(200, 150, 100, 40) 


		# adding action to a button 
		button.clicked.connect(self.clickme) 


	# action method 
	def clickme(self): 

		# printing pressed 
		print("pressed") 

# create pyqt5 app 
App = QApplication(sys.argv) 

# create the instance of our Window 
window = Window() 

# start the app 
sys.exit(App.exec()) 


