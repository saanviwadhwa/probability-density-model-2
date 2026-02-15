# Learning Probability Density Functions Using GAN

## Project Overview

This project aims to learn an unknown probability density function (PDF) of a transformed random variable using a **Generative Adversarial Network (GAN)**.

The distribution is learned purely from data samples without assuming any parametric form.

---

## Dataset

- Dataset: India Air Quality Data  
- Source: Kaggle  
- Feature Used: NO₂ concentration (`no2` column)

---

## Step 1: Non-Linear Transformation

The transformation applied is:

z = x + a_r * sin(b_r * x)

Where:

a_r = 0.5 * (r mod 7)  
b_r = 0.3 * ((r mod 5) + 1)

For roll number:

r = 102483080  

r mod 7 = 0  
r mod 5 = 0  

Therefore:

a_r = 0  
b_r = 0.3  

Since a_r = 0, the transformation reduces to:

z = x

---

## Step 2: GAN Architecture

### Generator

- Input: 1D Gaussian noise N(0,1)
- Dense(32) + ReLU
- Dense(32) + ReLU
- Dense(1)

### Discriminator

- Input: 1D sample
- Dense(32) + ReLU
- Dense(32) + ReLU
- Dense(1) + Sigmoid

### Training Configuration

- Loss: Binary Cross Entropy
- Optimizer: Adam
- Learning Rate: 0.001
- Batch Size: 64
- Epochs: 2000

The generator learns to produce realistic samples while the discriminator learns to distinguish real from fake samples.

---

## PDF Estimation

After training:

1. 5000 samples are generated from the generator.
2. Kernel Density Estimation (KDE) is applied.
3. The estimated density is plotted with real data histogram.

---

## Observations

### Mode Coverage

The GAN captures the dominant peak of the NO₂ distribution effectively.

### Training Stability

The adversarial training remained stable without divergence or mode collapse.

### Quality of Generated Distribution

The generated samples match the overall shape and spread of the real data distribution.

---

## Author

Saanvi Wadhwa
