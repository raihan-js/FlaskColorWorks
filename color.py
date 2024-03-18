# color.py

import torch
import numpy as np
import cv2
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights
from torchvision.transforms import functional as F
from PIL import Image
import sys

def get_model():
    model = maskrcnn_resnet50_fpn(weights=MaskRCNN_ResNet50_FPN_Weights.DEFAULT)
    model.eval()
    return model

def apply_color_preserving_texture(image, mask, rgb_color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask_bool = mask > 127
    target_hue = cv2.cvtColor(np.uint8([[rgb_color]]), cv2.COLOR_BGR2HSV)[0][0][0]
    hsv_image[..., 0] = np.where(mask_bool, target_hue, hsv_image[..., 0])
    image_colored = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    return image_colored

def detect_and_color_objects(image_path, target_label, rgb_color, model, output_filepath):
    image = Image.open(image_path).convert("RGB")
    image_tensor = F.to_tensor(image).unsqueeze(0)
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    with torch.no_grad():
        prediction = model(image_tensor)

    for element in range(len(prediction[0]['labels'])):
        if prediction[0]['labels'][element].item() == target_label:
            mask = prediction[0]['masks'][element, 0].mul(255).byte().cpu().numpy()
            image_cv = apply_color_preserving_texture(image_cv, mask, rgb_color)

    cv2.imwrite(output_filepath, image_cv)
    print(f"Processed image saved as: {output_filepath}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python object_detection.py <image_path> <target_label_id> <R,G,B>")
    else:
        model = get_model()  # Load the model only once
        image_path = sys.argv[1]
        target_label = int(sys.argv[2])
        rgb_color = tuple(map(int, sys.argv[3].split(',')))
        output_filepath = "colored_" + image_path.split('/')[-1]
        detect_and_color_objects(image_path, target_label, rgb_color, model, output_filepath)
