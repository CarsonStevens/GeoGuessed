from PIL import Image
from os import listdir
from os.path import isfile
import numpy as np

class App:
	def __init__(self):
		self.images = {}

	def load_image(self, filename : str):
	    img = Image.open(filename)
	    img.load()
	    return np.asarray(img, dtype="int32")

	def load_images(self, directory : str):
		try:
			for state in listdir(directory):
				state_path = directory + '/' + state
				print(f'loading {state}')
				count = 0
				for file in listdir(state_path):
					if count == 100:
						break
					# ignore all but images
					if file[-4:] == '.jpg':
						image_path = state_path + '/' + file
						image = self.load_image(filename = image_path)
						if state in self.images:
							self.images[state].append(image)
						else:
							self.images[state] = [image]
					count += 1
			print('done')
		except Exception as e:
			print(f'error: {e}')

if __name__ == "__main__":
	img_dir = "../images/10k"
	app = App()
	app.load_images(directory = img_dir)