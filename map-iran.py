import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


cities = [
    ("Tehran", 35.6892, 51.3890, 9.0),
    ("Mashhad", 36.2605, 59.6168, 3.0),
    ("Isfahan", 32.6539, 51.6660, 2.2),
    ("Tabriz", 38.0837, 46.2919, 1.6),
    ("Shiraz", 29.5918, 52.5837, 1.5),
    ("Qom", 34.6416, 50.8757, 1.2),
    ("Ahvaz", 31.3183, 48.6706, 1.1),
    ("Kermanshah", 34.3142, 47.0650, 1.0),
    ("Urmia", 37.5527, 45.0760, 0.7),
    ("Rasht", 37.2808, 49.5832, 0.7)
]


m = Basemap(projection='lcc', resolution='l', lat_0=32.0, lon_0=54.0, width=3E6, height=3E6)


m.drawcoastlines()
m.drawcountries()
m.drawparallels(range(25, 40, 5), labels=[1, 0, 0, 0])
m.drawmeridians(range(45, 65, 5), labels=[0, 0, 0, 1])
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='lightgray', lake_color='aqua')


for city, lat, lon, pop in cities:
    x, y = m(lon, lat)
    m.plot(x, y, 'ro', markersize=pop*2)
    plt.text(x, y, city, fontsize=12, ha='left', va='bottom')


plt.title("Major Cities of Iran with Population") 
plt.show()
