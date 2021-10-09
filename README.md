====================
Computer vision
====================

This repository provides some methods used in image processing and computer vision.

=============
About
=============

# ML/otsu.py
* This python script apply Otsu's thresholding method which involves iterating through all the possible threshold values and calculating a measure of spread for the pixel levels each side of the threshold, i.e. the pixels that either fall in foreground or background.

* The goal is to find the threshold value where the sum of foreground and background spreads is at its minimum.
* After applying Otsu method, we will apply GLCM (gray level co-occurrence matrices) to extract some features from the image.

# ML/grayscale.py
* This python script convert an image from RGB to GRAYSCALE


=============
Requirements
=============

* Python 3.
* Opencv:
	pip install opencv-python
* Skimage:
	pip install scikit-image

=====
Usage
=====

* To run the script otsu.py:
	$ python3 otsu.py path_to_image
	exp:
	$ python3 otsu.py /home/Desktop/test.png 
	
* To run the script grayscale.py:
	$ python3 grayscale.py path_to_image
	exp:
	$ python3 grayscale.py /home/Desktop/test.png 

======
Author
======

* Intissar HAMROUN
* intissar.hamroun@gmail.com
* Software engineer	
