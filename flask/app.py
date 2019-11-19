import os
import requests
import numpy as np
from config import *
from PIL import Image
from os.path import isfile

class App:
	def __init__(self):
		self.images = {}

	def load_image(self, filename: str):
		'''
		'''
		img = Image.open(filename)
		img.load()
		return np.asarray(img, dtype="float32")

	def load_images(self, directory: str):
		'''
		'''
		try:
			for state in listdir(directory):
				state_path = directory + '/' + state
				print(f'loading {state}')
				count = 0
				for file in os.listdir(state_path):
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

	def save_streetview_image(self, sequence_id: str, image_url: str, lat: str, lng: str):
		try:
			filename = ','.join([lat, lng])
			path = '/'.join([SEQUENCE_DIR, sequence_id])
			fullname = path + '/' + filename + '.' + FILE_EXTENSION

			if os.path.isdir(path):
				print(f"directory {path} exists")
			else:
				os.mkdir(path)
				print(f'directory {path} created')

			r = requests.get(url = image_url)
			with open(fullname, "wb") as file:
				file.write(r.content)

			return True

		except Exception as e:
			print(e)

	# def save_image(self, sequence_id: str, image_url: str, lat: str, lng: str):
	# 	'''
	# 	'''
	# 	try:
	# 		self.save_streetview_image(image_url, lat, lng)
	# 		return True

	# 		# fullname = path + '/' + filename + '.' + FILE_EXTENSION
	# 		# with open(fullname, "wb") as outstream:
	# 		# # # 	outstream.write(image_bytes.encode())
	# 		# 	outstream.write(str.encode(image_bytes))
	# 		# print(type(str.encode(image_bytes)))
	# 		# print("encoded")
	# 		# print(image_bytes)
	# 		# print(str.encode(image_bytes)[:100])
	# 		# print(image_bytes[:100])

	# 	except Exception as e:
	# 		print(f"save_image error: {e}")
	# 		return False



# if __name__ == "__main__":
# 	img_dir = "../images/10k"
# 	app = App()
# 	app.load_images(directory = img_dir)