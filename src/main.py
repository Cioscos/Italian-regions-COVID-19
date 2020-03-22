import json
import sys
import urllib.request

import matplotlib.pyplot as plt
from PyQt4.QtGui import *


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


class RegionList(QListWidget):

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

        write_plot(region_dic, str(item.text()))

    def init_json(self):
        self.regions = json_loader()


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    listWidget = RegionList()
    listWidget.init_json()

    # Resize width and height
    listWidget.resize(300, 120)
    listWidget.setToolTip('List of regions')

    for i in range(21):
        region = listWidget.regions[i]
        listWidget.addItem(region['denominazione_regione'])

    listWidget.setWindowTitle('PyQT QListwidget Demo')
    listWidget.itemDoubleClicked.connect(listWidget.clicked)

    layout.addWidget(listWidget)

    window.setWindowTitle('Italian Regions COVID-19')
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()