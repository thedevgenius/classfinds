import string
import random
import pygeohash as pgh


def generate_biz_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

#Get geohash neighbors
# Width (lon), Height (lat) in degrees
_GEOHASH_CELL = {
    1: (23, 23),
    2: (5.6, 2.8),
    3: (0.7, 0.7),
    4: (0.18, 0.087),
    5: (0.022, 0.022),
    6: (0.0055, 0.0027),
    7: (0.00068, 0.00068),
    8: (0.00017, 0.000085),
    9: (0.000021, 0.000021),
    10: (0.0000053, 0.0000026),
}

# 8 directions (lon, lat)
_OFFSETS = [
    ( 0,  1),  # north
    ( 0, -1),  # south
    ( 1,  0),  # east
    (-1,  0),  # west
    ( 1,  1),  # northeast
    ( 1, -1),  # southeast
    (-1,  1),  # northwest
    (-1, -1),  # southwest
]
def get_geohash_neighbors(gh):
    precision = len(gh)
    lat, lon = pgh.decode(gh)

    lon_size, lat_size = _GEOHASH_CELL[precision]

    neighbors = []
    for dx, dy in _OFFSETS:
        nlat = lat + dy * lat_size
        nlon = lon + dx * lon_size
        neighbors.append(pgh.encode(nlat, nlon, precision))
    
    return neighbors