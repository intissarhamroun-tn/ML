import cv2
import sys
import os
import time

# convert image to grayscale
def tograyscale(image_path):
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    result_path = os.path.dirname(image_path)+'/'+str(time.time())+'_grayscale.png'
    width = 600
    height = 450
    dim = (width, height)
    resized = cv2.resize(gray_img, dim, interpolation=cv2.INTER_AREA)
    cv2.imwrite(result_path, resized)
    
if __name__ == "__main__":
    tograyscale(sys.argv[1])


