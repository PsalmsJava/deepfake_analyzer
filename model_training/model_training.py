import torch
import torchvision.models as models

resnet18 = models.resnet18(pretrained=True)
torch.save(resnet18, 'C:/Users/Veesignature/Desktop/deepfake analyzer/model_training/model.pth')
