import config


def get_total_tif_height(images):
    total_height = config.image_size['y']

    counter = 0

    for image in images:
        counter += 1

        if counter == 4:
            total_height += image.height
            total_height += config.image_margin['y']

            counter = 0

    if counter != 0:
        return total_height + config.offset['y'] * 2
    else:
        return total_height - 24
