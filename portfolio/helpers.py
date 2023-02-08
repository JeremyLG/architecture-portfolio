import os
from typing import List


def get_images(path: str) -> List[str]:
    files = os.listdir("assets/" + path)
    images = []

    for file in files:
        # make sure file is an image
        if file.endswith((".jpg", ".png", "jpeg")):
            images += [ "/" + path + file]
    return images
