import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_histogram(image):
    histogram = [0] * 256
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            histogram[int(image[i][j])] += 1
    return histogram


img = cv2.imread("Inputs/spider.png", cv2.IMREAD_GRAYSCALE)
histogram = calculate_histogram(img)


plt.plot(histogram)
plt.ylabel('pixels')
plt.xlabel('range of color')
plt.title('Histogram')
plt.savefig('Output/histogram_plot.png')

plt.hist(img.ravel(), 256)
plt.ylabel('pixels')
plt.xlabel('range of color')
plt.title('Histogram')
plt.savefig('Output/histogram_hist.png')

plt.bar(np.arange(256), histogram)
plt.ylabel('pixels')
plt.xlabel('range of color')
plt.title('Histogram')
plt.savefig('Output/histogram_bar.png')