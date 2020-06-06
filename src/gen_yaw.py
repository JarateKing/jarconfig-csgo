for i in range(0, 101):
	n = i / 10
	print('alias jar_mouse_horiz_mult=', n, ' "m_yaw ', "{:.4f}".format(0.022 * n), '"', sep='')