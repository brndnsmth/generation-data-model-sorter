import os
from PIL import Image
from tqdm import tqdm
import shutil


# Extracts model information from the given image metadata
def extract_model(metadata):
    # Check if metadata is a dictionary
    if isinstance(metadata, dict):
        # Extract 'parameters' from metadata dictionary
        parameters = metadata.get("parameters", "")
        # Split parameters string into lines
        lines = parameters.split("\\n")
        # Search for the line containing "Model:"
        for line in lines:
            if "Model:" in line:
                # Find the index of "Model:" in the line
                start_index = line.index("Model:") + len("Model:")
                # Extract the model substring until the end of the line
                model = line[start_index:].split(",")[0].strip()
                return model
    return "Unknown"


# Extracts parameter and additional metadata from the given image file and returns it
def extract_generation_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            metadata = img.info
            return metadata
    except Exception as e:
        print(f"Error extracting metadata from {image_path}: {e}")
        return None


# Process image files and export to txt files, copying them to appropriate folders
def export_generation_metadata_to_text(image_dir, output_dir):
    # Get list of image files in the directory
    image_files = [
        filename
        for filename in os.listdir(image_dir)
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))
    ]
    # Iterate over each image file and extract parameters metadata
    for filename in tqdm(image_files, desc="Extracting Metadata"):
        image_path = os.path.join(image_dir, filename)
        try:
            metadata = extract_generation_metadata(image_path)
            if metadata:
                # Extract model information from metadata
                model = extract_model(metadata)
                # Create directory for model if it doesn't exist
                model_dir = os.path.join(output_dir, model)
                if not os.path.exists(model_dir):
                    os.makedirs(model_dir)
                # Copy image to model directory
                shutil.copy(image_path, model_dir)
                # Write metadata to txt file
                txt_filename = os.path.splitext(filename)[0] + ".txt"
                with open(os.path.join(model_dir, txt_filename), "w") as f:
                    for key, value in metadata.items():
                        f.write(f"{key}: {value}\n")
            else:
                print(f"Skipping {filename} due to extraction error")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    image_directory = "images"
    output_directory = "output"
    export_generation_metadata_to_text(image_directory, output_directory)
