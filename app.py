from flask import Flask, render_template, request
import torch
import torchvision.transforms as transforms
from PIL import Image
import base64
from io import BytesIO

app = Flask(__name__)

# Load the pre-trained model
class FakeRealModel:
    def __init__(self):
        self.model = torch.load('C:/Users/Veesignature/Desktop/deepfake analyzer/model_training/model.pth', map_location=torch.device('cpu'))
        self.model.eval()

    def predict(self, image):
        with torch.no_grad():
            outputs = self.model(image.unsqueeze(0))
            _, predicted = torch.max(outputs, 1)
            return 'real' if predicted.item() == 1 else 'fake'

fake_real_model = FakeRealModel()

def process_uploaded_image(image):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = preprocess(image)
    return image

def image_to_data_url(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_data = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{img_data}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image1' not in request.files or 'image2' not in request.files:
            return "Please upload two images."
        
        image1 = request.files['image1']
        image2 = request.files['image2']
        
        if image1.filename == '' or image2.filename == '':
            return "Please select two images to upload."
        
        image1 = Image.open(image1)
        image2 = Image.open(image2)
        
        processed_image1 = process_uploaded_image(image1)
        processed_image2 = process_uploaded_image(image2)
        
        image1_data = image_to_data_url(image1)
        image2_data = image_to_data_url(image2)
        
        result1 = fake_real_model.predict(processed_image1)
        result2 = fake_real_model.predict(processed_image2)
        
        return render_template('result.html', result1=result1, result2=result2, image1_data=image1_data, image2_data=image2_data)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
