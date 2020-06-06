from math import tan, atan, radians

targets = {
	'center': 0.0000000000000000000000000000000000000000000000000001,
	'1:1':    1,
	'5:4':    5/4,
	'4:3':    4/3,
	'16:10':  16/10,
	'16:9':   16/9,
}

weapons = {
	'awp': 40,
	'awp2': 10,
	'ssg': 40,
	'ssg2': 15,
	'scar': 40,
	'scar2': 15,
	'g3sg': 40,
	'g3sg2': 15,
	'aug': 45,
	'sg553': 45,
}

def zoomsens(zoom, hip, target):
	return atan(target * tan(atan(tan(radians(zoom) / 2) * (3/4)))) / atan(target * tan(atan(tan(radians(hip) / 2) * (3/4)))) / (zoom / hip)

for wep, zoom in weapons.items():
	for aspect, target in targets.items():
		print('alias jar_zoomsens=', wep, ',', aspect, ' "zoom_sensitivity_ratio_mouse ', "{:.15f}".format(zoomsens(zoom, 90, target)), '"', sep='')
