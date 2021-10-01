from glob import glob
from PIL import Image
from tqdm import tqdm

# Przeskalowanie obrazów do formatu 500x500
thumbnail_size = (500, 500)
# tqdm i ładny paseczek "ulala" :))
for file in tqdm(glob('photo/*.jpg')):
    img = Image.open(file)
    print(img.size)
    img.thumbnail(thumbnail_size)


    img.save(file)