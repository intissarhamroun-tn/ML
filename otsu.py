import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops
import sys
import csv
import time
import os



# Extract GLCM Texture Features from thresholded image

def glcm(image_path,csv_file):
    '''
    	image_path: path of image to apply GLCM
	csv_file: path of csv file that we will save glcm result in
    '''
    img = cv2.imread(image_path,0)
    image_array = np.array(img, dtype=np.uint8)
    g = greycomatrix(image_array, [1], [0, np.pi / 4, np.pi / 2, (3 * np.pi) / 4], levels=256, normed=True,
                     symmetric=True)
    # Compute some GLCM properties 
    contrast = greycoprops(g, 'contrast')
    dissimilarity = greycoprops(g, 'dissimilarity')
    homogeneity = greycoprops(g, 'homogeneity')
    energy = greycoprops(g, 'energy')
    correlation = greycoprops(g, 'correlation')
    ASM = greycoprops(g, 'ASM')
    global_contrast = (contrast[0, 0] + contrast[0, 1] + contrast[0, 2] + contrast[0, 3]) / 4
    global_diss = (dissimilarity[0, 0] + dissimilarity[0, 1] + dissimilarity[0, 2] + dissimilarity[0, 3]) / 4
    global_homog = (homogeneity[0, 0] + homogeneity[0, 1] + homogeneity[0, 2] + homogeneity[0, 3]) / 4
    global_energy = (energy[0, 0] + energy[0, 1] + energy[0, 2] + energy[0, 3]) / 4
    global_corr = (correlation[0, 0] + correlation[0, 1] + correlation[0, 2] + correlation[0, 3]) / 4
    global_asm = (ASM[0, 0] + ASM[0, 1] + ASM[0, 2] + ASM[0, 3]) / 4
    nms = [[global_contrast, global_diss, global_homog, global_energy, global_corr, global_asm,3]]
    # write GLCM Features in csv file
    f = open(csv_file, 'w')
    with f:
        writer = csv.writer(f)
        for row in nms:
            writer.writerow(row)


def otsu(image_path):
    # read img
    im=cv2.imread(image_path)
    # prepare paths
    result_path = os.path.dirname(image_path)+'/'+str(time.time())+'_result.png'
    contour_path = os.path.dirname(image_path)+'/'+str(time.time())+'_contour.png'
    csv_file = os.path.dirname(image_path)+'/'+str(time.time())+'_glcm.csv'
    # binary thresholding
    img = cv2.imread(image_path, 0)
    ret3, th3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # extract contour
    contours, hierarchy = cv2.findContours(th3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im, contours, -1, (255, 0, 0), 1)
    cv2.imwrite(contour_path, im)
    # apply filters
    mask = cv2.dilate(th3, None, iterations=1)
    mask = cv2.erode(mask, None, iterations=1)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)
    lesion = cv2.bitwise_or(img, mask)
    cv2.imwrite(result_path, lesion)
    glcm(result_path, csv_file)


if __name__ == "__main__":
    otsu(sys.argv[1])

