import config
from PIL import Image
from ..helpers.image_processor import get_total_tif_height


def combine_images(image_paths):
    images = [
        Image.open(image_path).resize(
            (config.image_size['x'], config.image_size['y']), Image.LANCZOS)
        for image_path in image_paths]

    max_width = max(image.width for image in images) + config.image_margin['x']

    num_cols = min(4, len(images))

    total_width = max_width * num_cols + 120

    total_height = get_total_tif_height(images)

    combined_image = Image.new(
        'RGB', (total_width, total_height), color='white'
    )

    x_offset, y_offset = config.offset['x'], config.offset['y']

    for image in images:
        combined_image.paste(image, (x_offset, y_offset))

        x_offset += max_width

        if x_offset >= max_width * num_cols:
            x_offset, y_offset = config.offset['x'], y_offset + \
                image.height + config.image_margin['y']

    combined_image.save('Result.tif', format='JPEG')
