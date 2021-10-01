from glob import glob
from PIL import Image
from tqdm import tqdm
import typer

def make_thumbnails(thumbnail_size:tuple[int, int], source_dir: str,
                    extension: str):
    # tqdm i ładny paseczek "ulala" :))
    for file in tqdm(glob(f'{source_dir}/*.{extension}')):
        img = Image.open(file)
        print(img.size)
        img.thumbnail(thumbnail_size)


        img.save(file)