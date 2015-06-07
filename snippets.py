__author__ = 'Zivia'

    gems_url = "https://api.guildwars2.com/v2/commerce/exchange/gems?quantity=100"
    gem_time = []
    gem_data = []

    for x in xrange(300):

        response = urllib.urlopen(gems_url)
        data = json.loads(response.read())

        for key, value in data.items():
            print key, value
            if key == 'quantity':
                gem_time.append(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                gem_data.append(value)

        print '---------------------'

        time.sleep(60)

    data = Data([
        Scatter(name='Gem --> Coin', x=gem_time, y=gem_data)
    ])

    layout = Layout(
        title='Gem --> Coin',
        xaxis=XAxis(title='Time Stamp'),
        yaxis=YAxis(title='100 Gems --> Coin')
    )

    figure = Figure(data=data, layout=layout)

    py.plot(figure, filename='100 Gems --> Coin')