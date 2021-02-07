import urllib.request as req
import json
import matplotlib.pyplot as plt
import numpy as np


def json_loader():
    with req.urlopen(
            "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json") as url:
        data = json.loads(url.read().decode())
        return data


def write_plot(region, region_name):
    cases = []
    dead = []
    recovered = []
    currently_positive = []

    # types of virus positive
    virusPositive = [[], [], []]

    # Load the lists with data for each days
    for index in region:
        day = region[index]
        cases.append(day['totale_casi'])
        dead.append(day['deceduti'])
        recovered.append(day['dimessi_guariti'])
        currently_positive.append(day['totale_positivi'])
        virusPositive[0].append(day['ricoverati_con_sintomi'])
        virusPositive[1].append(day['terapia_intensiva'])
        virusPositive[2].append(day['isolamento_domiciliare'])

    # Create matplotlib figure
    fig = plt.figure(figsize=(8, 6))
    fig.suptitle('Grafici andamento contagi in ' + region_name)
    gs = fig.add_gridspec(2, 2, hspace=0.40, wspace=0.40)

    # Creates plot for total cases and currently positives
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.plot(cases, 'o-r')
    ax1.plot(currently_positive, 'yo-')
    ax1.set_ylabel('Infetti')
    ax1.set_xlabel('Giorni')
    ax1.legend(['Casi totali', 'Attualmente positivi'], loc='upper left')

    # Creates plot for dead and recovered
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(dead, 'bo-')
    ax2.plot(recovered, 'go-')
    ax2.set_ylabel('Infetti')
    ax2.set_xlabel('Giorni')
    ax2.legend(['Morti', 'Curati'], loc='upper left')

    # create a plot for the 3 types of infected people
    ax3 = fig.add_subplot(gs[1, :])
    x = np.arange(len(virusPositive[0]))

    ax3.bar(x, virusPositive[2], 0.50, color='g')
    ax3.bar(x, virusPositive[1], 0.50, color='r')
    ax3.bar(x, virusPositive[0], 0.50, bottom=virusPositive[2], color='b')
    ax3.set_ylabel('Infetti')
    ax3.set_xlabel('Giorni')
    ax3.legend(['Isolamento domiciliare', 'Terapia intensiva', 'Ricoverati con sintomi'], loc='upper left')
    ax3.set_xticks(np.arange(0, len(virusPositive[0]), 50))

    plt.show()
