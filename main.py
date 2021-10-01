from glob import glob
from PIL import Image
from tqdm import tqdm
import typer

def make_thumbnails(
        thumbnail_width: int = typer.Option(500, help="Szerokość obrazka."),
        thumbnail_heigh: int = typer.Option(500, help="Wysokość obrazka."),
        source_dir: str = typer.Option('AfterFormat', help="Ścieżka końcowa."),
        extension: str = typer.Option('jpg', help='rozszerzenie.')
):
    # tqdm i ładny paseczek "ulala" :))
    for file in tqdm(glob(f'{source_dir}/*.{extension}')):
        img = Image.open(file)
        img.thumbnail((thumbnail_width, thumbnail_heigh))
        img.save(file)

if __name__ == '__main__':
    typer.run(make_thumbnails)