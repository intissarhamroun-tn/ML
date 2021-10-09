# ML
This python script apply Otsu's thresholding method which involves iterating through all the possible threshold values and calculating a measure of spread for the pixel levels each side of the threshold, i.e. the pixels that either fall in foreground or background.
The goal is to find the threshold value where the sum of foreground and background spreads is at its minimum.
After applying Otsu method, we will apply GLCM (gray level co-occurrence matrices) to extract some features from the image.


Requirements: 
*Python 3.
*opencv:
	pip install opencv-python
*skimage:
	pip install scikit-image
	
To run the script:
	$ python3 otsu.py path_to_image
	exp:
	$ python3 otsu.py /home/Desktop/test.png 
 

	
