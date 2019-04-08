# 1. Statusbar
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('Statusbar')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


# 2. Simple Menu
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        self.setGeometry(300, 300, 450, 150)
        self.setWindowTitle('Simple menu')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


# 3. Submenu
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        
        newAct = QAction('New', self)
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


# 4. Check Menu
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')
        
        viewStatAct = QAction('View statusbar', self, checkable = True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        
        viewMenu.addAction(viewStatAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


# 5. Context Menu
import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Context menu')
        self.show()
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


# 6. Toolbar
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Toolbar')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())


# 7. Put It Together
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        
        exitAct = QAction(QIcon('exit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
       
        self.statusBar()
       
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
       
        self.setGeometry(300, 300, 400, 250)
        self.setWindowTitle('Main Window')
        self.show()
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())