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
import spidev
from numpy import interp
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import sys
import numpy as np
import pyqtgraph

spi = spidev.SpiDev()
spi.open(0, 0)

class ExampleApp(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        pyqtgraph.setConfigOption('background', 'w')
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 300, 300))
        self.graphicsView.setObjectName("graphicsView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
    def analogInput(self, channel):
        spi.max_speed_hz = 1350000
        adc = spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data
    
    def update(self):
        points = 100
        X = np.arange(points)
        n = 0
        dataLst = []
        while n < 100:
            dataPoint = self.analogInput(0)
            dataLst.append(dataPoint)
            n += 1
        Y = dataLst
        penn = pyqtgraph.mkPen('k', width = 3, style = QtCore.Qt.SolidLine)
        self.graphicsView.setYRange(0, 1200, padding = 0)
        labelStyle = {'color':'#000', 'font-size':'20px'}
        self.graphicsView.setLabel('bottom', 'Number of Points', '', **labelStyle)
        self.graphicsView.setLabel('left', 'Voltage', '', **labelStyle)
        self.graphicsView.plot(X, Y, pen = penn, clear = True)
        QtCore.QTimer.singleShot(1, self.update)
        
app = QtGui.QApplication(sys.argv)
form = ExampleApp()
form.show()
form.update()
app.exec_()
