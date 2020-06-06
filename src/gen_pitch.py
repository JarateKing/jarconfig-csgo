for i in range(0, 101):
	n = i / 10
	print('alias jar_mouse_vert_mult=', n, ' "m_pitch ', "{:.4f}".format(0.022 * n), '"', sep='')