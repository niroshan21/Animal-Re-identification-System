import timm
import torchvision.transforms as T
import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import gdown
import pickle

# Load the pre-trained animal re-identification model
model = timm.create_model("hf-hub:BVRA/MegaDescriptor-S-224", pretrained=True)
model = model.eval()  # Set the model to evaluation mode

# Define the transformation for input images
train_transforms = T.Compose([
    T.Resize((224, 224)), 
    T.ToTensor(), 
    T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

# Function to extract features from an image file path
def extract_features(image_path):
    img = Image.open(image_path)                        # Load image
    img_transformed = train_transforms(img)             # Apply transformations
    img_features = model(img_transformed.unsqueeze(0))  # Extract features
    return img_features.detach().numpy()                # Convert to numpy array

# Load the known animal feature list from the file
known_animal_features = np.load('Feature CSV/known_animal_features.npy')  

# Load the known animal information list from the file
with open('Feature CSV/animal_info_list.pkl', 'rb') as f:
    animal_info_list = pickle.load(f)

# Function to download image from Google Drive (using the gdown library)
def download_image_from_drive(drive_url):
    # Example : https://drive.google.com/open?id=1KJ6kpya6UzhxteN-kIhg6mITvk_ekBnj
    file_id = drive_url.split('=')[1]
    direct_link = f'https://drive.google.com/uc?id={file_id}'
    output_path = f'Test Images/Registered Cows/{file_id}.jpg' # Save the registered cow images to my local directory
    gdown.download(direct_link, output_path, quiet=False)
    return output_path

# Function to add a new animal to the known list
def add_animal(drive_links, name, owner, refnum):
    # Download images and extract features
    features_list = []
    for link in drive_links:
        image_path = download_image_from_drive(link)        # Download image
        features_list.append(extract_features(image_path))  # Extract features
        
    avg_features = np.mean(features_list, axis=0)           # Average the features
    
    # Update the known features list
    global known_animal_features
    if known_animal_features.size == 0:
        known_animal_features = avg_features
    else:
        known_animal_features = np.vstack((known_animal_features, avg_features))
    
    # Update the animal information list
    animal_info_list.append({
        'name': name,
        'owner': owner,
        'refnum' : refnum
    })
    print(f"Added animal: {name}, Owner: {owner}, Reference Number: {refnum}")



#Get the Google Sheets access
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Set Up the Google Sheets API Client:
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']      # Define the scope
creds = ServiceAccountCredentials.from_json_keyfile_name('Google Cloud Console/animal-re-identification-ae729ae62110.json', scope)  # Load the service account credentials
client = gspread.authorize(creds)  # Authorize the client

#Open the Google Sheet:
sheet = client.open("Cow Re-Identification").sheet1  # # Open the sheet by name or by URL

column_index = 2  # Reference Number column
search_value = input("Enter your reference number: ") 

# Get all values in the specified column
column_values = sheet.col_values(column_index)

# Search for the value and get the row index
try:
    row_index = column_values.index(search_value) + 1  # I used 1 because list indices start at 0
    print(f"Found '{search_value}' at row: {row_index}")
except ValueError:
    print(f"'{search_value}' not found in column {column_index}.")

cell_value = sheet.cell(row_index, 6).value

new_animal_links = cell_value.split(", ")     # Split the links into a list  (comma as a separator)

name = sheet.cell(row_index, 5).value
owner = sheet.cell(row_index, 3).value
ref = sheet.cell(row_index, 2).value



# Add the new animal to the known list
add_animal(new_animal_links, name, owner, ref)



# Save the array to a file
np.save('Feature CSV/known_animal_features.npy', known_animal_features)

# Save the list to a file
with open('Feature CSV/animal_info_list.pkl', 'wb') as f:
    pickle.dump(animal_info_list, f)

print('Your Cow Regisrtation is Sucessfull...')