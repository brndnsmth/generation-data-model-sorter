# Generation Data - Model Sorter

Export metadata from images to .txt files, sorted into directories by models.

Useful for bulk sorting of generated images into directories named after checkpoint model.

Example output:

## Usage

1. Place the images you want to process in the `images` folder.
2. Run the script `main.py`.
3. Images and text files (w/ generation data) will be added to model directories within `output`.

The script supports the following file types:

- .jpg
- .jpeg
- .png
- .bmp
- .gif

## Requirements

- Python 3.x

## Setup Steps


1. Clone git repo.

```
git clone https://github.com/brndnsmth/generation-data-model-sorter.git
cd generation-data-model-sorter
```

2. **Create a Virtual Environment:** Utilize Python 3 to create a virtual environment for this project. This step ensures a clean and isolated environment for installing dependencies.

```
python3 -m venv .venv
```

3. **Activate the Virtual Environment:** Activate the virtual environment to isolate the project dependencies from other Python installations on your system.

```
source .venv/bin/activate
```

4. **Install Dependencies:** While inside the virtual environment, install the required dependencies specified in the requirements.txt file using pip.

```
pip install -r requirements.txt
```

5. **Add Images:** Create `images` folder and add images to directory.

```
mkdir images
```

6. **Run the Script:** Execute the following command to run the script:

```
python main.py
```

7. **Check Output:** Check `output` directory.
