import cv2

class Main:
		
	@staticmethod
	def check_device(source) -> bool:
		tet = cv2.VideoCapture(source)
		
		if tet is None or not tet.isOpened():
			return False
		return True

	@staticmethod
	def main() -> None:
		if Main.check_device(0):
			vid = cv2.VideoCapture(0)
			vid.set(3, 500)
			vid.set(4, 500)

			cicle = True
			while cicle:
				rect, frame = vid.read()
				cv2.imshow('cam', frame)
		
				if cv2.waitKey(1) & 0xFF == ord:
					cicle = False
			
			cv2.destroyWindowsAll()	

if __name__ == '__main__':
	Main.main()
