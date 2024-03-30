import os
import sys
from scripts.helpers.directory_processor import get_all_files_from_folder
from scripts.actions.combine_images import combine_images


if __name__ == "__main__":
    images_sum = []

    folders = [
        '1369_12_Наклейки 3-D_3', '1388_2_Наклейки 3-D_1', '1388_6_Наклейки 3-D_2', '1388_12_Наклейки 3-D_3'
    ]

    if len(folders) == 0:
        sys.exit('Не указаны имена папок.')

    for folder in folders:
        images_per_folder = get_all_files_from_folder(
            f'{os.getcwd()}/images/{folder}')

        for image in images_per_folder:
            images_sum.append(f'{os.getcwd()}/images/{folder}/{image}')

    if len(images_sum) == 0:
        sys.exit('Не было найдено ни одной картинки.')

    combine_images(images_sum)

    print('Работа скрипта завершена.')
