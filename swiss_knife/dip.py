import cv2
import numpy as np


def remove_background(i_file_path: str, o_file_path: str):
    image = cv2.imread(i_file_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    alpha = np.ones_like(thresh) * 255

    alpha[thresh == 0] = 0

    image_bgra = cv2.merge((image, alpha))

    cv2.imwrite(o_file_path, image_bgra)


if __name__ == "__main__":
    remove_background("assets/bird.jpeg", "assets/bird_bg_removed.png")
