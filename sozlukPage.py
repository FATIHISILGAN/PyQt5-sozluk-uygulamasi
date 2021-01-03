
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import QCompleter
import os
from pathlib import Path
class Ui_Sozluk(object):
    def setupUi(self, Sozluk):
        Sozluk.setObjectName("Sozluk")
        Sozluk.resize(496, 311)
        Sozluk.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(Sozluk)
        self.centralwidget.setObjectName("centralwidget")
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 40, 339, 223))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.anlamLbl = QtWidgets.QLabel(self.layoutWidget)
        self.anlamLbl.setObjectName("anlamLbl")
        self.gridLayout.addWidget(self.anlamLbl, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.araBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.araBtn.setObjectName("araBtn")
        self.araBtn.clicked.connect(self.ara_Clicked)
        self.gridLayout.addWidget(self.araBtn, 0, 1, 1, 1)
        self.kelimeler = QtWidgets.QListWidget(self.layoutWidget)
        self.kelimeler.setObjectName("kelimeler")
        self.kelimeler.clicked.connect(self.kelimeler_Clicked)
        self.gridLayout.addWidget(self.kelimeler, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        Sozluk.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Sozluk)
        self.statusbar.setObjectName("statusbar")
        Sozluk.setStatusBar(self.statusbar)

        self.retranslateUi(Sozluk)
        QtCore.QMetaObject.connectSlotsByName(Sozluk)
        
        with open('kelimeler.txt', 'r') as movieDir:

            for movie in movieDir:
                self.kelimeler.addItem(movie)
               
        kelimelist=['apple','hello','my','suprise','why','shy','love','life','language']
         
        completer=QCompleter(kelimelist)

        self.editor=self.lineEdit
        self.editor.setCompleter(completer)
        
       
        

   
        
       


       
       
        

       

        
        
    def retranslateUi(self, Sozluk):
        _translate = QtCore.QCoreApplication.translate
        Sozluk.setWindowTitle(_translate("Sozluk", "MainWindow"))
        
        self.anlamLbl.setText(_translate("Sozluk", "anlam"))
        self.araBtn.setText(_translate("Sozluk", "ara"))
        self.label.setText(_translate("Sozluk", "anlam:"))

    def ara_Clicked(self, Sozluk):

        dizi = list()

        for i in range(self.kelimeler.count()):
            dizi.append(self.kelimeler.item(i).text())

        for i in range(len(dizi)):
            if(dizi[i] == self.lineEdit.text() or dizi[i] == self.lineEdit.text()+'\n'):
                self.kelimeler.setCurrentRow(i)
                break

        self.getMean(self)

    def kelimeler_Clicked(self, sozluk):
        self.getMean(self)

    def getMean(self, sozluk):

        seciliIndex = self.kelimeler.currentRow()
        sayac = 0
        with open('anlamlar.txt', 'r') as movieDir:
            for movie in movieDir:

                if(sayac == seciliIndex):

                    self.anlamLbl.setText(movie)

                sayac = sayac+1


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    Sozluk = QtWidgets.QMainWindow()
    ui = Ui_Sozluk()
    ui.setupUi(Sozluk)
    Sozluk.show()
    sys.exit(app.exec_())
   

    