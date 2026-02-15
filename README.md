<<<<<<< HEAD
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
=======
Learning Probability Density Functions Using GAN
Project Overview

This project focuses on learning an unknown probability density function (PDF) of a transformed random variable using a Generative Adversarial Network (GAN).

The goal is to model the distribution purely from data samples without assuming any parametric form such as Gaussian or exponential distributions.

Dataset

Dataset: India Air Quality Data
Source: Kaggle
Feature Used: NO₂ concentration (column: no2)

The NO₂ concentration values are used as the input feature 
𝑥
x.

Step 1: Non-Linear Transformation

Each value of 
𝑥
x is transformed using the roll-number-parameterized function:
>>>>>>> de0cd92013a9ca997242059461bf28314b3ebdc2

z = x + a_r * sin(b_r * x)

Where:

<<<<<<< HEAD
a_r = 0.5 * (r mod 7)  
b_r = 0.3 * ((r mod 5) + 1)

For roll number:

r = 102483080  

r mod 7 = 0  
r mod 5 = 0  

Therefore:

a_r = 0  
b_r = 0.3  
=======
a_r = 0.5 * (r mod 7)
b_r = 0.3 * ((r mod 5) + 1)

For roll number: 102483080

r mod 7 = 0
r mod 5 = 0

Therefore:

a_r = 0
b_r = 0.3
>>>>>>> de0cd92013a9ca997242059461bf28314b3ebdc2

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
=======
Thus, the transformed variable is identical to the original NO₂ concentration.

Step 2: PDF Learning Using GAN

The probability density function of the transformed variable 
𝑧
z is assumed unknown.

A Generative Adversarial Network (GAN) is trained to learn this distribution directly from data samples.

Generator Architecture

Input: 1-dimensional Gaussian noise N(0,1)

Hidden Layer 1: Fully connected, 32 neurons, ReLU activation

Hidden Layer 2: Fully connected, 32 neurons, ReLU activation

Output: 1-dimensional generated sample

Discriminator Architecture

Input: 1-dimensional real or generated sample

Hidden Layer 1: Fully connected, 32 neurons, ReLU activation

Hidden Layer 2: Fully connected, 32 neurons, ReLU activation

Output: 1 neuron with Sigmoid activation (probability of real sample)

Training Configuration

Loss Function: Binary Cross Entropy (BCE)

Optimizer: Adam

Learning Rate: 0.001

Batch Size: 64

Epochs: 2000

The discriminator learns to distinguish real samples from generated samples, while the generator learns to produce realistic synthetic samples.

Step 3: PDF Approximation

After training:

5000 synthetic samples are generated from the trained generator.

Kernel Density Estimation (KDE) is applied to generated samples.

The estimated density is plotted along with the histogram of real data.

This KDE curve represents the learned probability density function.

Observations

Mode Coverage:
The GAN successfully captured the dominant mode of the NO₂ distribution. The main peak of the generated distribution closely matches that of the real data.

Training Stability:
The generator and discriminator losses exhibited typical oscillatory behavior without divergence or mode collapse, indicating stable adversarial training.

Quality of Generated Distribution:
The generated samples reproduced the overall shape and spread of the real distribution. Slight smoothing in tail regions occurred due to KDE bandwidth selection.

Technologies Used

Python

PyTorch

NumPy

Pandas

Matplotlib

Scikit-learn

How to Run

Install dependencies:

pip install torch numpy pandas matplotlib scikit-learn


Run the script:

python sol.py

Author
>>>>>>> de0cd92013a9ca997242059461bf28314b3ebdc2

Saanvi Wadhwa
