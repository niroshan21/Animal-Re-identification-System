# Animal Re-Identification System

## Overview
The **Animal Re-Identification System** is designed to re-identify cows based on their unique patterns and features. By utilizing the **SIFT (Scale-Invariant Feature Transform)** descriptor and matching methods, this system aims to provide efficient and accurate identification of individual animals. The project employs the **MegaDescriptor** model instead of traditional models like CLIP and DINOv2, ensuring better performance. The Wildlife Toolkit is used for matching descriptors, enhancing the accuracy of the identification process.

![Project Overview](https://github.com/niroshan21/Animal-Re-identification-System/blob/main/Images/Google%20Form.jpg?raw=true)

## Features
- **Cow Registration**: Owners can register their cows using a Google Form.
- **Descriptor Database**: Cow features are stored in a database for re-identification.
- **Automated Email Notifications**: Automatic emails are sent to owners with a reference number upon registration.(We use [google app scripts](https://github.com/niroshan21/Animal-Re-identification-System/tree/main/Google%20Apps%20Script) for this)
- **Efficient Matching**: Utilizes the MegaDescriptor model for accurate re-identification.

## Algorithm
1. **Registration**: Cow owners fill out a Google Form to register their cows. Upon submission, an auto-generated reference code is sent to the owner.
2. **Descriptor Database**: We can add cow's feature description data into the descriptor database using the reference code.
3. **Re-Identification**: The numpy array uses stored data to re-identify cows based on their unique features.

## Libraries and Dependencies

To set up and run this project, install the following libraries:
- **timm**: For loading and utilizing the deep learning model.
- **numpy**: For numerical operations, such as averaging feature vectors and saving data.
- **Pillow**: Python Imaging Library for loading and handling images.
- **scikit-learn**: Contains the `cosine_similarity` function to compare feature vectors.
- **gdown**: Allows downloading files from Google Drive for accessing registered cow images.
- **gspread**: A client for the Google Sheets API to enable reading and writing data to Google Sheets.
- **oauth2client**: Manages authorization to access Google Sheets via a service account.
  ```bash
  pip install timm
  pip install numpy
  pip install pillow
  pip install scikit-learn
  pip install gdown
  pip install gspread
  pip install oauth2client
  ```

To download the dataset click [here](https://github.com/niroshan21/Animal-Re-identification-System/blob/main/Codes/downloadDatasets.ipynb)
