import sys
from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8 model
model = YOLO('best.pt') # pretrained YOLOv8n model

# Check if an image path is provided through the command line
if len(sys.argv) > 1:
    image_path = sys.argv[1]
else:
    print("Please provide the path to the image as a command-line argument.")
    sys.exit(1)

# Run inference on the provided image
results = model(image_path, conf=0.15)  # results list

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')
