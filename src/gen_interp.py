for i in range(10, 101):
	n = i / 10
	print('alias jar_interp=', n, ' "cl_interp ', "{:.6f}".format(0.015625 * n), '; cl_interp_ratio ', n, '"', sep='')