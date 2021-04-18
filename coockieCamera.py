import picamera

# setup the camera such that it closes
# when we are done with it.
print ("Capturing Picture")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("cam.jpg")
print ("Picture Captured...")

