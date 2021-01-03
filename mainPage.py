
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os 
from sozlukPage import Ui_Sozluk
from ekle import Ui_EklePage





class Ui_MainWindow(object):
    
  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 278)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(170, 80, 111, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addWord = QtWidgets.QPushButton(self.widget)
        self.addWord.setObjectName("addWord")
        self.addWord.clicked.connect(self.kelime_Clicked)
        self.verticalLayout.addWidget(self.addWord)
        self.sozluk = QtWidgets.QPushButton(self.widget)
        self.sozluk.setObjectName("sozluk")
        self.sozluk.clicked.connect(self.sozluk_Clicked)
        self.verticalLayout.addWidget(self.sozluk)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addWord.setText(_translate("MainWindow", "kelime ekle"))
        self.sozluk.setText(_translate("MainWindow", "Sözlük"))



    
    def sozluk_Clicked(self,MainWindow):   
        self.sozlukac = SozlukEkrani()
        self.sozlukac.show()   
    

    def kelime_Clicked(self,MainWindow):
        
        self.kelimeac = KelimeEkrani()
        self.kelimeac.show() 
      
     
    

       
       

   



class SozlukEkrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(SozlukEkrani, self).__init__()
        self.sozluktikla = Ui_Sozluk()
        self.sozluktikla.setupUi(self) 

class KelimeEkrani(QtWidgets.QMainWindow):
    def __init__(self):
        super(KelimeEkrani, self).__init__()
        self.kelimetikla = Ui_EklePage()
        self.kelimetikla.setupUi(self)        
        
       

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())    