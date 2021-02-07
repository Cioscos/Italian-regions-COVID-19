import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import utilities


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setDocumentMode(False)
        self.setWindowIcon(QtGui.QIcon('.\\mainWindow.png'))
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.RegionList = RegionList(self.centralwidget)
        self.RegionList.setGeometry(QtCore.QRect(0, 40, 791, 471))
        self.RegionList.setMouseTracking(False)
        self.RegionList.setAlternatingRowColors(True)
        self.RegionList.setObjectName("RegionList")
        self.RegionList.init_json()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 41))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.label.setMargin(10)
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(690, 520, 101, 31))
        self.okButton.setFlat(False)
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(self.clicked)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setCheckable(False)
        self.actionSave.setChecked(False)
        self.actionSave.setObjectName("actionSave")
        self.actionEcit = QtWidgets.QAction(self)
        self.actionEcit.setObjectName("actionEcit")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEcit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Italian-regions-COVID-19"))
        self.RegionList.setStatusTip(_translate("MainWindow", "Seleziona una regione per visualizzarne i dati"))
        self.RegionList.setSortingEnabled(True)
        self.label.setText(_translate("MainWindow", "Lista delle regioni"))
        self.okButton.setToolTip(_translate("MainWindow", "Seleziona"))
        self.okButton.setText(_translate("MainWindow", "Ok"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save as File"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEcit.setText(_translate("MainWindow", "Exit"))

    def clicked(self):
        self.RegionList.clicked(self.RegionList.currentItem())


class DataWindow(QtWidgets.QDialog):
    def __init__(self, region, name):
        super(DataWindow, self).__init__()
        self.region = region
        self.name = name

        self.setWindowTitle('Data')
        self.resize(200, 100)

        # Layout that will contains all the element of the window
        self.windowLayout = QtWidgets.QVBoxLayout()

        # It'll contain the data about the last region update
        lastData = region[len(region) - 1]

        for datum in lastData:
            # Filter useless data
            if datum != 'stato' and datum != 'codice_regione' and datum != 'lat' and datum != 'long':
                self.hLayout = QtWidgets.QHBoxLayout()
                self.label = QtWidgets.QLabel(str(datum).replace('_', ' ').capitalize())
                self.dateText = QtWidgets.QLineEdit()
                self.dateText.setText(str(lastData[datum]))
                self.dateText.setReadOnly(True)
                self.dateText.textChanged.connect(self.resizeToContent)
                self.hLayout.addWidget(self.label)
                self.hLayout.addWidget(self.dateText)
                self.windowLayout.addLayout(self.hLayout)

        self.hLayout = QtWidgets.QHBoxLayout()
        self.showPlotButton = QtWidgets.QPushButton(self)
        self.showPlotButton.setText('Mostra grafico')
        self.showPlotButton.clicked.connect(self.clicked)
        self.hLayout.addWidget(self.showPlotButton)
        self.windowLayout.addLayout(self.hLayout)
        self.setLayout(self.windowLayout)
        self.setWindowIcon(QtGui.QIcon('.\\mainWindow.png'))

        self.show()

    def clicked(self):
        utilities.write_plot(self.region, self.name)

    def resizeToContent(self):
        text = self.dateText.text()
        font = QtGui.QFont()
        fm = QtGui.QFontMetrics(font)
        pixelsWide = fm.width(text)
        pixelsHigh = fm.height()

        self.dateText.setFixedSize(pixelsWide, pixelsHigh)



class RegionList(QtWidgets.QListWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super(RegionList, self).__init__(parent)
        self.regions = None

    def clicked(self, item):
        # Dictionary with all the data of selected region
        region_dic = dict()
        j = 0

        # If regions is initialized
        if self.regions is not None:
            for region in self.regions:
                # If the name of the region is the same of user's selected region
                if region['denominazione_regione'] == str(item.text()):
                    # Add the datum in the dictionary
                    region_dic[j] = region
                    j += 1

        dataWindow = DataWindow(region_dic, str(item.text()))
        dataWindow.exec_()

    def init_json(self):
        self.regions = utilities.json_loader()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()

    # List of region name of each data
    regionNames = list()
    for region in win.RegionList.regions:
        # Fill the list
        regionNames.append(region['denominazione_regione'])

    # Delete duplicate
    regionNames = list(dict.fromkeys(regionNames))

    # Fill the list
    for i in range(len(regionNames)):
        region = win.RegionList.regions[i]
        win.RegionList.addItem(region['denominazione_regione'])

    win.RegionList.itemDoubleClicked.connect(win.RegionList.clicked)

    sys.exit(app.exec_())
