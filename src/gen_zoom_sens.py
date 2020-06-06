from math import tan, atan, radians

def zoomsens(zoom, hip, target):
	return atan(target * tan(atan(tan(radians(zoom) / 2) * (3/4)))) / atan(target * tan(atan(tan(radians(hip) / 2) * (3/4)))) / (zoom / hip)

print(zoomsens(40, 90, 0.00000000000001))