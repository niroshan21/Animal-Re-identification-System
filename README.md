# Animal Re-Identification System

## Overview
The **Animal Re-Identification System** is designed to re-identify cows based on their unique patterns and features. By utilizing the **SIFT (Scale-Invariant Feature Transform)** descriptor and matching methods, this system aims to provide efficient and accurate identification of individual animals. The project employs the **MegaDescriptor** model instead of traditional models like CLIP and DINOv2, ensuring better performance. The Wildlife Toolkit is used for matching descriptors, enhancing the accuracy of the identification process.

## Features
- **Cow Registration**: Owners can register their cows using a Google Form.
- **Descriptor Database**: Cow features are stored in a database for re-identification.
- **Automated Email Notifications**: Automatic emails are sent to owners with a reference number upon registration.(We use [google app scripts]() for this)
- **Efficient Matching**: Utilizes the MegaDescriptor model for accurate re-identification.

## Algorithm
1. **Registration**: Cow owners fill out a Google Form to register their cows. Upon submission, an auto-generated reference code is sent to the owner.
2. **Descriptor Database**: We can add cow's feature description data into the descriptor database using the reference code.
3. **Re-Identification**: The numpy array uses stored data to re-identify cows based on their unique features.

## Libraries and Dependencies
To access Google Sheets and send emails, install the following libraries:
```bash
pip install gspread oauth2client
