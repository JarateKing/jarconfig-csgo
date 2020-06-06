def sens(dpi, inches, yaw):
	return 360 / (dpi * inches * yaw)

for inches in range(1, 41):
	for dpi in range(400, 16001, 400):
		print('alias jar_sens=', inches, 'in/360,', dpi, 'dpi "sensitivity ', sens(dpi, inches, 0.022), '; alias jar_sens jar_sens=', inches, 'in/360,', dpi, 'dpi; jar_multsens"', sep='')