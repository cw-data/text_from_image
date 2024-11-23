"""
Extract text from one or more folders of images containing text

Uses `easyocr`
https://github.com/jaidedai/easyocr

1. Screenshots of pages into project dir
    - manual process TODO: automate this? Right now it takes about 12 files per chapter.
    - The quality of text-output changes depending on the font-size of the text. Specs for k app settings are in data/text_spec.png.
2. Loop over screenshots and extract text-pieces
3. Append each text-piece to a list of pieces
4. Write each piece to a text file and save
5. Import text file to screen-reader
"""

import easyocr
from glob import glob
import time

reader = easyocr.Reader(['ch_sim','en']) # only have to run once to download the text dictionary

def process_images(data_folder:str, output_filename:str='') -> list[list[str]]:
    """Extract the text from each .png file in a folder of .png images.

    Args:
        data_folder (str): relative or absolute filepath to a folder of .png images from which text should be parsed
        output_filename (str, optional): relative or absolute filepath for output file of text parsed from images.
            Defaults to ''. If blank, will not write file. If not blank, must end in '.txt'.

    Returns:
        list: A list of lists.
            The outer list contains one element per .png file located in `data_folder`.
            Each inner list contains one element per chunk of text present in a .png file from `data_folder`.

    Example usage:
        import src.img as img
        input_folder=r'data/ch3'
        output_file=r'output/test.txt'
        result = img.process_images(data_folder=input_folder, output_filename=output_file)
    """
    
    # business logic
    # input folder must be instance of folder and cannot end in '/' or '\'
    assert data_folder.endswith('/')==False, print(f"You proivded {data_folder=}, which ends in a forward-slash. Folders should not end in a slash.")
    assert data_folder.endswith('\\')==False, print(f"You proivded {data_folder=}, which ends in a backslash. Folders should not end in a slash.")

    # output must be a txt file
    if output_filename != '':
        assert output_filename.endswith('.txt'), print(f"You provided {output_filename=} which does not end with '.txt'. The output filename must end in '.txt'.")
    
    start_time = time.time()

    files = _find_image_files(data_folder=data_folder)
    extracted_text, counter = _extract_text_from_files(files=files)
    
    print(f"Parsed {counter} pieces of text from {len(files)} files in {round((time.time() - start_time) ,2)} seconds")

    if output_filename != '':
        _write_text_to_file(output_filename=output_filename, input_list=extracted_text)

    return extracted_text


def _find_image_files(data_folder:str) -> list:

    files = glob(f'{data_folder}\\*.png')
    assert len(files) >0, print(f"You provided {data_folder=}, which contains zero .png files.")
    print(f"Found {len(files)} images to parse...")

    return files

def _extract_text_from_files(files:list):

    extracted_text = []
    for i in range(len(files)):
        result = reader.readtext(image=files[i], detail=0)
        extracted_text.append(result)
        print(f"Processed {i+1} of {len(files)} files...")
        counter=0
    
    for t in extracted_text:
        counter+=len(t)

    return extracted_text, counter

def _write_text_to_file(output_filename:str, input_list:list) -> None:

    with open(output_filename, "w", encoding="utf-8") as file:
        for line in input_list:
            if isinstance(line, list):
                for x in line:
                    if x.endswith("\n"):
                        file.write(x)
                    else:
                        file.write(x + "\n")
            elif isinstance(line, str):
                file.write(line + "\n")
            else:
                print(f"FAIL: did not write line to file {output_filename=}")
                print(line)

    print(f"Wrote text to {output_filename=}")

    return None
