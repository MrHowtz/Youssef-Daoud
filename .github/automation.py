import os
from PIL import Image, ImageEnhance
import time

def enhance_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"enhanced_{filename}")

            try:
                if os.path.exists(input_path):
                    img = Image.open(input_path)

                    enhancer = ImageEnhance.Color(img)
                    enhanced_img = enhancer.enhance(2.0)

                    enhanced_img.save(output_path)
                    print(f"Image enhanced and saved: {output_path}")
                else:
                    print(f"Error: {input_path} does not exist.")
            except Exception as e:
                print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
  input_directories = ['Images/BMW_images/', 'Images/Mercedes_images/', 'Images/Porsche_images/']
output_directory = 'enhanced_images/'
#whwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhw
for input_directory in input_directories:
    enhance_images(input_directory, output_directory)

    
    enhance_images(input_directory, output_directory)