import json
import sys
import urllib.request

import matplotlib.pyplot as plt
from PyQt4 import QtGui


def write_plot(region, region_name):
    cases = []
    dead = []
    recovered = []
    currently_positive = []
    for index in region:
        day = region[index]
        cases.append(day['totale_casi'])
        dead.append(day['deceduti'])
        recovered.append(day['dimessi_guariti'])
        currently_positive.append(day['totale_attualmente_positivi'])

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.canvas.set_window_title('Grafici')

    fig.suptitle('Grafici andamento contagi in ' + region_name)

    ax1.plot(cases, 'o-r')
    ax1.plot(currently_positive, 'yo-')
    ax1.legend(['Casi totali', 'Attualmente positivi'], loc='upper left')

    ax2.plot(dead, 'bo-')
    ax2.plot(recovered, 'go-')
    ax2.legend(['Morti', 'Curati'], loc='upper left')

    plt.show()


def json_loader():
    with urllib.request.urlopen(
            "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json") as url:
        data = json.loads(url.read().decode())
        return data


class DataWindow(QtGui.QDialog):
    def __init__(self, region, name):
        super(DataWindow, self).__init__()

        self.setWindowTitle('Data')
        self.resize(200, 100)

        # Layout that will contains all the element of the window
        self.windowLayout = QtGui.QVBoxLayout()

        # It'll contain the data about the last region update
        lastData = region[len(region) - 1]

        for datum in lastData:
            # Filter useless data
            if datum != 'stato' and datum != 'codice_regione' and datum != 'lat' and datum != 'long':
                self.hLayout = QtGui.QHBoxLayout()
                self.label = QtGui.QLabel(str(datum).replace('_', ' ').capitalize())
                self.dateText = QtGui.QLineEdit()
                self.dateText.setText(str(lastData[datum]))
                self.dateText.setReadOnly(True)
                self.hLayout.addWidget(self.label)
                self.hLayout.addWidget(self.dateText)
                self.windowLayout.addLayout(self.hLayout)

        self.setLayout(self.windowLayout)
        self.setWindowIcon(QtGui.QIcon('..\\icons\\mainWindow.png'))
        self.show()
        write_plot(region, name)


class RegionList(QtGui.QListWidget):

    # It'll contain all data about regions
    regions = None

    def __init__(self):
        super().__init__()

    # When an item in the list been clicked
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
        self.regions = json_loader()


def main():
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()

    # Create a vertical layout
    layout = QtGui.QVBoxLayout(window)
    # Initialize listWidget
    listWidget = RegionList()
    # Load json from Github
    listWidget.init_json()

    # Set title
    listWidget.setToolTip('List of regions')
    listWidget.setAlternatingRowColors(True)

    # List of region name of each data
    regionNames = list()
    for region in listWidget.regions:
        # Fill the list
        regionNames.append(region['denominazione_regione'])

    # Delete duplicate
    regionNames = list(dict.fromkeys(regionNames))

    # Fill the list
    for i in range(len(regionNames)):
        region = listWidget.regions[i]
        listWidget.addItem(region['denominazione_regione'])

    listWidget.itemDoubleClicked.connect(listWidget.clicked)

    layout.addWidget(listWidget)

    window.setWindowTitle('Italian Regions COVID-19')

    window.setFixedSize(300, 200)
    window.setWindowIcon(QtGui.QIcon('..\\icons\\mainWindow.png'))
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()