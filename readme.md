# Text from image

A python program that extracts text from one or more images and concatenate the text into one file.

## Use-case

Language-learning. I use this tool to extract Chinese characters from images, like pictures of menus or street signs. Then, I upload the extracted text into a flashcard program so that I can study colloquial Mandarin Chinese.

## Getting started

1. Clone the repository. In terminal:

```
git clone https://github.com/cw-data/text_from_image
```

2. Install `requirements.txt` into your project python environment. In (Windows) terminal:

```
python -m venv /path/to/new/virtual/environment
<venv_name>\Scripts\activate
pip install -r /path/to/requirements.txt
```
3. Update variables `input_folder` and `output_file` in `main.py`. Run `main.py.` In terminal:

```
<venv_name>\Scripts\activate # if environment is not activated
python main.py
```
## Usage notes

1. Output text accuracy increases as the resolution and text size of input images increases. Feeding blurry images with small text into the model will not yield good results.
2. I run this model on CPU-only, and it processes one image every ~20 seconds. This program is built on top of [easyocr](https://github.com/JaidedAI/EasyOCR), which recommends a GPU to improve performance.
