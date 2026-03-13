# Handwritten Chinese Character Recognition (HCCR)

This repository contains a deep learning implementation for recognizing handwritten Chinese characters using the CASIA HWDB1.1 dataset. The project evaluates and compares ResNet101 and DenseNet121 architectures, specifically investigating the impact of the Convolutional Block Attention Module (CBAM) on model performance.

## Overview

The primary objective of this project is to achieve high-accuracy character recognition for a subset of the CASIA HWDB1.1 dataset (200 classes). The implementation leverages transfer learning from ImageNet-pretrained weights and incorporates attention mechanisms to enhance feature extraction.

### Key Features

*   **Architectures:** Implementation of ResNet101 and DenseNet121.
*   **Attention Mechanisms:** Integration of Squeeze-and-Excitation (SE) and Convolutional Block Attention Module (CBAM) blocks.
*   **Preprocessing Pipeline:** A multi-stage pipeline for data extraction, resizing, contrast enhancement, and dataset organization.
*   **Performance Evaluation:** Comparative analysis of base models versus attention-enhanced variants.

## Technical Architecture

### Model Enhancements
The standard ResNet and DenseNet implementations were modified to include attention modules:
*   **CBAM (Convolutional Block Attention Module):** Applies both channel and spatial attention to the feature maps, allowing the model to focus on the most relevant parts of the character strokes.
*   **SE (Squeeze-and-Excitation):** Focuses on modeling the interdependencies between channels.

### Preprocessing Pipeline
The `preprocessing/` directory contains scripts for preparing the CASIA HWDB1.1 dataset:
1.  **Extraction:** Extracting character images from the raw `.gnt` format.
2.  **Resizing:** Normalizing character dimensions to 64x64 pixels.
3.  **Contrast Enhancement:** Improving stroke visibility through image processing.
4.  **Data Organization:** Structuring the dataset into training, validation, and testing sets.

## Project Structure

*   `main.py`: Entry point for training, validation, and testing.
*   `resnet.py`: Modified ResNet101 implementation with CBAM support.
*   `densenet.py`: Modified DenseNet121 implementation with CBAM support.
*   `attention_module.py`: Definitions for SE and CBAM blocks.
*   `preprocessing/`: Data preparation scripts.
*   `graphs/`: Performance visualization (loss and accuracy curves).

## Installation and Usage

### Prerequisites
*   Python 3.x
*   TensorFlow / Keras
*   NumPy, Matplotlib, OpenCV (for preprocessing)

### Dataset Preparation
1.  Download the CASIA HWDB1.1 dataset.
2.  Execute the scripts in the `preprocessing/` directory in sequence (1-5) to prepare the data.

### Training and Evaluation
To train and evaluate the model, run:
```bash
python main.py
```
By default, `main.py` is configured to use ResNet101 with CBAM. You can switch between models and configurations by modifying the imports and model initialization in `main.py`.

## Results

| Model | Configuration | Test Accuracy |
|------|---------------|--------------|
| DenseNet121 | Base | **96.2%** |
| DenseNet121 | With CBAM | 96.1% |
| ResNet101 | Base | 94.4% |
| ResNet101 | With CBAM | 91.5% |

### Observations

- **DenseNet121 + CBAM converged faster** (optimal epoch 23 vs 33) while maintaining nearly identical accuracy.
- **ResNet101 + CBAM did not improve performance**, achieving lower accuracy and slightly slower convergence.
- This suggests the effectiveness of CBAM may depend on the underlying architecture.

## References

*   Woo, S., Park, J., Lee, J. Y., & Kweon, I. S. (2018). CBAM: Convolutional Block Attention Module. ECCV.
*   He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep Residual Learning for Image Recognition. CVPR.
*   Huang, G., Liu, Z., Van Der Maaten, L., & Weinberger, K. Q. (2017). Densely Connected Convolutional Networks. CVPR.
