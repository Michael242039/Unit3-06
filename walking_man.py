import ui
import time

SPEED = 10

@ui.in_background
def animate():
	globals()
	
	frame = 1
	
	while frame <= 10:
		#makes a variable to store mans x (easier than typing view['blablabla']) everytime
		x = view['man_imageview'].x
		
		#sets the path to the image to the current frame by mashing the frame variable into the file paths string 
		path = 'Resources/walk' + str(frame) + '.bmp'
		
		#sets the image/frame to the path
		view['man_imageview'].image = ui.Image(path)
		
		#moves the man to his left
		x = x - SPEED
		
		#delays it so its not instant
		time.sleep(0.05)
		
		#updates frame and keeps it looping
		frame = frame + 1
		if frame >= 10:
			frame = 1
			
		#wraps man around when he hits the edge
		if x < 0:
			x = 540
			
		#sets the mans x to the stored and now modified x
		view['man_imageview'].x = x
		
	
view = ui.load_view()
#calls animate
animate()
view.present('sheet')
