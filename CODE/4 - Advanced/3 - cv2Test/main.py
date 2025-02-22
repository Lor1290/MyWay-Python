import cv2
import os

class Main:
	
	@staticmethod
	def main() -> None:
		image = cv2.imread('img.jpg', 1)
		gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)		
		
		h, w  = image.shape[:2]
		print(f'height: {h} and width: {w}')
		data = image.shape[2:]
		print(f'other data: {data}')
			

		B, R, G = image[100, 100]
		print(f'value of the pixel in 100x100 position: {R} {G} {B}')
		R = image[110, 110, 2]
		print(f'value of the R pixel in the 110x110 position: {R}')
		
		
		from_to = image[100: 500, 200: 500]
		cv2.imshow('ROI image', from_to)

		resize_image = cv2.resize(image, (500, 500))
		cv2.imshow('Resized Image', resize_image)
		
		ratio = 500 / w
		dim = (500, int(h * ratio))
		
		correct_resize = cv2.resize(image, dim)
		cv2.imshow('Correct Resized Image', correct_resize)


		out = image.copy()
		rect = cv2.rectangle(out, (100, 100), (200, 200), (190, 190, 190), 2)
		text = cv2.putText(out, 'TEST', (150, 150), cv2.FONT_HERSHEY_SIMPLEX, 4, (10, 10, 10), 3)

		cv2.imshow('Rectangle image', out)		
		

		cv2.imshow('gray image', gray_img)
		if 'gray_img.jpg' not in os.listdir('./'):	
			cv2.imwrite('./gray_img.jpg', gray_img)
			print('Image saved succesfully!')

		key = cv2.waitKey(0)
		print(f'{key} was pressed')
		
		cv2.destroyWindow('gray image')	
#		cv2.destroyAllWindows()

if __name__ == '__main__':
	Main.main()
