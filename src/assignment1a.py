"""
Author: Katelyn Van Dyke
Date: 26 Jan 2024
Course: Computer Vision
Professor: Dr. Feliz Bunyak Ersoy
Description: Hybrid image generator
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# Create a data folder
output_folder = '../data'
os.makedirs(output_folder, exist_ok=True)


# Save image to data folder
def save_image(image, name):
    cv2.imwrite(os.path.join(output_folder, name), image)


# Plot color levels and save to data folder
def rgb_histograms(image, title, figure_number):
    colors = ('r', 'g', 'b')
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.title(title)
    plt.savefig(os.path.join(output_folder, f'figure_{figure_number}.png'))
    plt.close()


# Isolate low frequencies
def low_pass_filter(image, kernel_size, cutoff_frequency):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), cutoff_frequency)


# Isolate high frequencies
def high_pass_filter(image, kernel_size, cutoff_frequency):
    filtered_image = cv2.subtract(image, low_pass_filter(image, kernel_size, cutoff_frequency))
    return np.clip(filtered_image, 0, 255)


# Blur image with low pass filter
def blur(image, kernel_size, cutoff_frequency):
    return low_pass_filter(image, kernel_size, cutoff_frequency)


# Sharpen image with high pass filter
def sharpen(image, kernel_size, cutoff_frequency):
    sharpened_image = cv2.addWeighted(high_pass_filter(image, kernel_size, cutoff_frequency), 1, image, 1, 0)
    return np.clip(sharpened_image, 0, 255)


# Create hybrid image using high & low pass filters
def hybrid_image(image1, image2, kernel_size, cutoff_frequency):
    low_freq = low_pass_filter(image1, kernel_size, cutoff_frequency)
    high_freq = high_pass_filter(image2, kernel_size, cutoff_frequency)
    return cv2.addWeighted(low_freq, 0.5, high_freq, 0.5, 0)


# Load test images
image1 = cv2.imread('../images/dog_crp.jpeg')
image2 = cv2.imread('../images/cat_crp.jpeg')


# Pad images
image1 = cv2.copyMakeBorder(image1, 3, 3, 3, 3, cv2.BORDER_DEFAULT)
image2 = cv2.copyMakeBorder(image2, 3, 3, 3, 3, cv2.BORDER_DEFAULT)


# Filtering parameters (https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html)
cutoff_frequency = 9
kernel_size = 3 * cutoff_frequency

# Blur images
blurred_image1 = blur(image1, kernel_size, cutoff_frequency)
blurred_image2 = blur(image2, kernel_size, cutoff_frequency)

# Sharpen images
sharpened_image1 = sharpen(image1, kernel_size, cutoff_frequency)
sharpened_image2 = sharpen(image2, kernel_size, cutoff_frequency)

# Extract low frequencies with low pass filter
low_freq_image1 = low_pass_filter(image1, kernel_size, cutoff_frequency)
low_freq_image2 = low_pass_filter(image2, kernel_size, cutoff_frequency)

# Extract high frequencies with high pass filter
high_freq_image1 = high_pass_filter(image1, kernel_size, cutoff_frequency)
high_freq_image2 = high_pass_filter(image2, kernel_size, cutoff_frequency)

# Save image 1 convolutions
save_image(blurred_image1, 'smoothed_image_1.jpg')
save_image(sharpened_image1, 'sharpened_image_1.jpg')
save_image(low_freq_image1, 'low_freq_image_1.jpg')
save_image(high_freq_image1, 'high_freq_image_1.jpg')

# Save image 2 convolutions
save_image(blurred_image2, 'smoothed_image_2.jpg')
save_image(sharpened_image2, 'sharpened_image_2.jpg')
save_image(low_freq_image2, 'low_freq_image_2.jpg')
save_image(high_freq_image2, 'high_freq_image_2.jpg')

# Save image 1 histograms
rgb_histograms(image1, 'Original Image 1 Histograms', 1)
rgb_histograms(blurred_image1, 'Smoothed Image 1 Histograms', 2)
rgb_histograms(sharpened_image1, 'Sharpened Image 1 Histograms', 3)
rgb_histograms(low_freq_image1, 'Low Frequencies Image 1 Histograms', 4)
rgb_histograms(high_freq_image1, 'High Frequencies Image 1 Histograms', 5)

# Save image 2 histograms
rgb_histograms(image2, 'Original Image 2 Histograms', 6)
rgb_histograms(blurred_image2, 'Smoothed Image 2 Histograms', 7)
rgb_histograms(sharpened_image2, 'Sharpened Image 2 Histograms', 8)
rgb_histograms(low_freq_image2, 'Low Frequencies Image 2 Histograms', 9)
rgb_histograms(high_freq_image2, 'High Frequencies Image 2 Histograms', 10)

# Generate hybrid image
hybrid_image = hybrid_image(image1, image2, kernel_size, cutoff_frequency)

# Save hybrid image
save_image(hybrid_image, 'hybrid_image.jpg')

# Save hybrid image histograms
rgb_histograms(hybrid_image, 'Hybrid Image Histograms', 11)
