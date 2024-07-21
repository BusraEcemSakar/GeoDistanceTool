# geo_distance_tool.py

import math

class GeoDistanceTool:
    def __init__(self, unit='km'):
        self.unit = unit
        self.R = 6371 if unit == 'km' else 3958.8  # Radius of Earth in km or miles

    def haversine(self, lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points on the Earth's surface
        :param lat1: Latitude of the first point
        :param lon1: Longitude of the first point
        :param lat2: Latitude of the second point
        :param lon2: Longitude of the second point
        :return: Distance between the two points in the specified unit
        """
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return self.R * c

    def vincenty(self, lat1, lon1, lat2, lon2):
        """
        Calculate the distance using the Vincenty formula
        :param lat1: Latitude of the first point
        :param lon1: Longitude of the first point
        :param lat2: Latitude of the second point
        :param lon2: Longitude of the second point
        :return: Distance between the two points in the specified unit
        """
        # Vincenty formula implementation here
        pass

# Example usage
if __name__ == "__main__":
    tool = GeoDistanceTool(unit='mi')
    print(f"Distance: {tool.haversine(52.2296756, 21.0122287, 41.8919300, 12.5113300)} miles")
