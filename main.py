from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8 model
model = YOLO('best.pt') # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model('signin.png',conf =0.15)  # results list

# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg') 