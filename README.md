# Hybrid Image Generator

## Author: Katelyn Van Dyke
## Date: 26 Jan 2024
## Course: Computer Vision
## Professor: Dr. Feliz Bunyak Ersoy

### Description

This repository contains Python code for generating hybrid images, a technique in computer vision that combines low-frequency information from one image with high-frequency information from another to create a visually intriguing composite image.

### Installation

Ensure you have the required dependencies installed:

```bash
pip install opencv-python numpy matplotlib
```

### Usage

1. Clone the repository:

```bash
git clone [repository_url]
cd [repository_directory]
```

2. Run the script:

```bash
python hybrid_image_generator.py
```

### Files

1. **hybrid_image_generator.py**: The main script containing functions for generating hybrid images, applying filters, and saving the results.
2. **/images**: Directory containing the input images (dog_crp.jpeg, cat_crp.jpeg).
3. **/data**: Directory where the output images and histograms are saved.

### Functionality

The script performs the following operations:

1. **Image Loading**: Load two input images (dog_crp.jpeg, cat_crp.jpeg) from the /images directory.
2. **Image Padding**: Pad the images with a border to avoid boundary effects during convolution.
3. **Filtering Parameters**: Set filtering parameters such as cutoff frequency and kernel size based on [OpenCV documentation](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html).
4. **Image Blurring and Sharpening**: Apply low-pass and high-pass filters to blur and sharpen the input images.
5. **Frequency Separation**: Extract low and high frequencies from the images using the defined filters.
6. **Save Convolutions**: Save the results of the filtering operations for both images.
7. **Generate Hybrid Image**: Combine low frequencies from one image with high frequencies from another to create a hybrid image.
8. **Save Hybrid Image**: Save the generated hybrid image.
9. **Generate and Save Histograms**: Generate and save histograms for original, smoothed, sharpened, low-frequency, and high-frequency images.

### Results

The script outputs various images and histograms in the /data directory, providing insights into the frequency components of the input images and the resulting hybrid image.

### Acknowledgments

The script is based on the principles of hybrid image generation and leverages the OpenCV library for image processing.

For any questions or issues, please contact Katelyn Van Dyke at [contact_email].

---

*Note: Replace [repository_url], [repository_directory], and [contact_email] with the appropriate values.*
