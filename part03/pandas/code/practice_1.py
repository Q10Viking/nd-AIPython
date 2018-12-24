import pandas as pd

# Create a Pandas Series that contains the distance of some planets from the Sun.
# Use the name of the planets as the index to your Pandas Series, and the distance
# from the Sun as your data. The distance from the Sun is in units of 10^6 km

distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth','Saturn', 'Mars','Venus', 'Jupiter']

# Create a Pandas Series using the above data, with the name of the planets as
# the index and the distance from the Sun as your data.
dist_planets = pd.Series(data=distance_from_sun,index=planets)
print(dist_planets)
# Calculate the number of minutes it takes sunlight to reach each planet. You can
# do this by dividing the distance from the Sun for each planet by the speed of light.
# Since in the data above the distance from the Sun is in units of 10^6 km, you can
# use a value for the speed of light of c = 18, since light travels 18 x 10^6 km/minute.
time_light = dist_planets / 18
print(time_light)

# Use Boolean indexing to select only those planets for which sunlight takes less
# than 40 minutes to reach them.
close_planets = time_light[ time_light < 40]
print(close_planets)
'''
Earth       149.6
Saturn     1433.5
Mars        227.9
Venus       108.2
Jupiter     778.6
dtype: float64
Earth       8.311111
Saturn     79.638889
Mars       12.661111
Venus       6.011111
Jupiter    43.255556
dtype: float64
Earth     8.311111
Mars     12.661111
Venus     6.011111
dtype: float64
'''