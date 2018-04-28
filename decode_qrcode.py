import qrtools

file = open('text.txt', 'w')


qr = qrtools.QR()
for i in range(0,68):
	# print i
	img="frame"+str(i)+".jpg"
	print img
	qr.decode(img)
	# print qr.data
	file.write(qr.data)
file.close()