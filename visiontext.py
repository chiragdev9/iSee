import io
import picamera
from google.cloud import vision

print ("Capturing Picture")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("cam.jpg")
print ("Picture Captured...")

vision_client = vision.Client()
file_name = "cam.jpg"

with io.open(file_name,'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(content=content)

labels = image.detect_text()

for label in labels:
    print(label.description)
