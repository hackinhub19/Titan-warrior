def mse(picA, picB):
	
	err = np.sum((picA.astype("float") - picB.astype("float")) ** 2)
	err /= float(picA.shape[0] * picA.shape[1])
	
	return err
 
def compare_images(picA, picB, title):
	
	m = mse(picA, picB)
	s = ssim(picA, picB)
 
	
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
 
	
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(picA, cmap = plt.cm.gray)
	plt.axis("off")
 
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(picB, cmap = plt.cm.gray)
	plt.axis("off")
 
	plt.show()
