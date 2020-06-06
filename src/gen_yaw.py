def invert(n):
	if n == 0:
		return 1
	else:
		return 1 / n

for i in range(0, 101):
	n = i / 10
	print('alias jar_mouse_horiz_mult=', n, ' "m_yaw ', "{:.4f}".format(0.022 * n), '; alias jar_multsens multvar sensitivity 0 1000000 ', "{:.8f}".format(invert(n)), '; jar_sens; jar_multsens"', sep='')