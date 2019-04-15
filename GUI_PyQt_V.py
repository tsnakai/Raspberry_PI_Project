# Task 1
#import serial
#import matplotlib.pyplot as plt
#
#ser = serial.Serial('COM3', 9600)
#n = 0
#dataLst = []
#while n < 200:
#    print(ser.readline())
#    dataPoint = ser.readline()
#    dataPoint = int(dataPoint)
#    dataLst.append(dataPoint)
#    n += 1
#ser.close()
#plt.plot(dataLst)
##plt.show()
#f = open("serialData.dat", "w")
#f.write(str(dataLst))
#f.close()
#f = open("serialData.dat", 'r')
#print(f.read())

# Task 2
#import pyqtgraph as pg
#from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph import PlotWidget
#import numpy as np
#
#x = np.array([1, 2, 3])
#y = np.array([1, 2, 3])
#pg.setConfigOption('background', 'w')
#penn = pg.mkPen('k', width = 2, style = QtCore.Qt.SolidLine)
#p1 = pg.plot(x, y, pen = penn, title = "The first pyqtgraph plot", sysmbol = 't', symbolSize = 20)
#p1.setXRange(0, 4)
#p1.setYRange(0, 4)
#p1.setLabel('left', 'Voltage', 'V')
#p1.setLabel('bottom', 'Time', 's')
#
#QtGui.QApplication.exec_()


#from PyQt5 import QtGui, QtCore
#import pyqtgraph as pg
#
#app = QtGui.QApplication([])
#w = QtGui.QWidget()
#btn = QtGui.QPushButton('Press Me')
#text = QtGui.QLineEdit('Enter Text')
#listw = QtGui.QListWidget()
#pg.setConfigOption('background', 'w')
#plt = pg.PlotWidget()
#penn = pg.mkPen('k', width = 2, style = QtCore.Qt.SolidLine)
#plt.plot([1, 2, 3], [1, 2, 3], pen = penn, title = "The first pyqtgraph plot", symbol = 't', symbolSize = 20)
#
#labelStyle = {'color':'#000','font-size':'30px'}
#plt.setLabel('bottom','Time','s',**labelStyle)
#plt.setLabel('left','Voltage','V',**labelStyle)
#plt.setYRange(0,5)
#plt.setXRange(0,5)
#layout = QtGui.QGridLayout()
#w.setLayout(layout)
#layout.addWidget(btn, 0, 0) # button goes in upper-left
#layout.addWidget(text, 1, 0) # text edit goes in middle-left
#layout.addWidget(listw, 2, 0) # list widget goes in bottom-left
#layout.addWidget(plt, 0, 1, 3, 1) # plot goes on right side, spanning 3 rows and 1 column
#w.show()
#app.exec_()


# Task 3
#from PyQt5 import QtCore, QtGui, QtWidgets
#from pyqtgraph import PlotWidget
#import serial
#import sys
#import numpy as np
#import pyqtgraph
#
#ser = serial.Serial('COM3', 9600)
#
#class ExampleApp(QtGui.QMainWindow):
#    def __init__(self):
#        super().__init__()
#        pyqtgraph.setConfigOption('background', 'w')
#        self.setupUi(self)
#        
#    def setupUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(900, 900)
#        self.centralwidget = QtWidgets.QWidget(MainWindow)
#        self.centralwidget.setObjectName("centralwidget")
#        
#        self.graphicsView = PlotWidget(self.centralwidget)
#        self.graphicsView.setGeometry(QtCore.QRect(200, 200, 500, 500))
#        self.graphicsView.setObjectName("graphicsView")
#        
#        MainWindow.setCentralWidget(self.centralwidget)
#        
#    def update(self):
#        points = 100
#        X = np.arange(points)
#        n = 0
#        dataLst = []
#        while n < 100:
#            dataPoint = ser.readline()
#            dataPoint = int(dataPoint)
#            dataLst.append(dataPoint)
#            n += 1
#        Y = dataLst
#        penn = pyqtgraph.mkPen('k', width = 3, style = QtCore.Qt.SolidLine)
#        self.graphicsView.setYRange(0, 1200, padding = 0)
#        labelStyle = {'color':'#000', 'font-size':'20px'}
#        self.graphicsView.setLabel('bottom', 'Number of Points', '', **labelStyle)
#        self.graphicsView.setLabel('left', 'Voltage', '', **labelStyle)
#        self.graphicsView.plot(X, Y, pen = penn, clear = True)
#        QtCore.QTimer.singleShot(1, self.update)
#        
#app = QtGui.QApplication(sys.argv)
#form = ExampleApp()
#form.show()
#form.update()
#app.exec_()


# Task 4
#import spidev
#from numpy import interp
#from time import sleep
#
#spi = spidev.SpiDev()
#spi.open(0, 0)
#
#def analogInput(channel):
#    spi.max_speed_hz = 1350000
#    adc = spi.xfer2([1, (8 + channel) << 4, 0])
#    data = ((adc[1] & 3) << 8) + adc[2]
#    return data
#while True:
#    output = analogInput(0)
#    print(output)
#    sleep(0.1)


# Task 5
#import spidev
#from numpy import interp
#from time import sleep
#from PyQt5 import QtCore, QtGui, QtWidgets
#from pyqtgraph import PlotWidget
#import sys
#import numpy as np
#import pyqtgraph
#
#spi = spidev.SpiDev()
#spi.open(0, 0)
#
#class ExampleApp(QtGui.QMainWindow):
#    def __init__(self):
#        super().__init__()
#        pyqtgraph.setConfigOption('background', 'w')
#        self.setupUi(self)
#        
#    def setupUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(350, 300)
#        self.centralwidget = QtWidgets.QWidget(MainWindow)
#        self.centralwidget.setObjectName("centralwidget")
#        
#        self.graphicsView = PlotWidget(self.centralwidget)
#        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 300, 300))
#        self.graphicsView.setObjectName("graphicsView")
#        
#        MainWindow.setCentralWidget(self.centralwidget)
#        
#    def analogInput(self, channel):
#        spi.max_speed_hz = 1350000
#        adc = spi.xfer2([1, (8 + channel) << 4, 0])
#        data = ((adc[1] & 3) << 8) + adc[2]
#        return data
#    
#    def update(self):
#        points = 100
#        X = np.arange(points)
#        n = 0
#        dataLst = []
#        while n < 100:
#            dataPoint = self.analogInput(0)
#            dataLst.append(dataPoint)
#            n += 1
#        Y = dataLst
#        penn = pyqtgraph.mkPen('k', width = 3, style = QtCore.Qt.SolidLine)
#        self.graphicsView.setYRange(0, 1200, padding = 0)
#        labelStyle = {'color':'#000', 'font-size':'20px'}
#        self.graphicsView.setLabel('bottom', 'Number of Points', '', **labelStyle)
#        self.graphicsView.setLabel('left', 'Voltage', '', **labelStyle)
#        self.graphicsView.plot(X, Y, pen = penn, clear = True)
#        QtCore.QTimer.singleShot(1, self.update)
#        
#app = QtGui.QApplication(sys.argv)
#form = ExampleApp()
#form.show()
#form.update()
#app.exec_()