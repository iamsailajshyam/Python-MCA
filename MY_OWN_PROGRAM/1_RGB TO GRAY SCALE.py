import cv2
import numpy as np
import requests
from io import BytesIO
from google.colab.patches import cv2_imshow

def url_to_grayscale(url):
    """
    Converts an image from a URL to grayscale.

    :param url: URL of the image.
    :return: Grayscale image as a NumPy array.
    """
    # Step 1: Download the image
    response = requests.get(url)
    image_data = BytesIO(response.content)

    # Step 2: Read the image from the downloaded data
    # Convert the byte data to a NumPy array
    image_array = np.frombuffer(image_data.read(), np.uint8)

    # Decode the image from the NumPy array
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError("Could not read the image from the URL.")

    # Step 3: Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return image, grayscale_image

# Example usage
image_url = 'https://imagecdnsa.zigwheels.ae/medium/gallery/color/2/8/audi-a3-color-234803.jpg'
original_image, grayscale_image = url_to_grayscale(image_url)

# Display the original image
cv2_imshow(original_image)

# Display the grayscale image
cv2_imshow(grayscale_image)

# Optionally, save the grayscale image
cv2.imwrite('grayscale_image.jpg', grayscale_image)
