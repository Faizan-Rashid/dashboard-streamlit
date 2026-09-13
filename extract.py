import zipfile

with zipfile.ZipFile("archive.zip") as zip_ref:
    zip_ref.extractall("food-ordering-dataset")