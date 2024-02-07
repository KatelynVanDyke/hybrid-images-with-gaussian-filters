# Hybrid Image Generator

### Description

This repository contains Python code for generating hybrid images, a technique in computer vision that combines low-frequency information from one image with high-frequency information from another to create a visually intriguing composite image.

### Installation and Usage

1. Ensure you have the required dependencies installed:

```bash
pip install opencv-python numpy matplotlib
```

2. Clone the repository:

```bash
git clone https://github.com/KatelynVanDyke/hybrid-images-with-gaussian-filters.git
cd hybrid-images-with-gaussian-filters
```

3. Run the script:

```bash
python assignment1a.py
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
