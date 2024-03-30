import os


def get_all_files_from_folder(path):
    return [f for f in os.listdir(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), path)
        )
    )]
