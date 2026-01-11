import cv2

def pencil_sketch_image(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError("Could not read the image. Check the file path.")

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # Invert the blurred image
    inverted_blurred = cv2.bitwise_not(blurred_image)

    # Create the sketch by blending the grayscale image with the inverted blurred image
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # Save the sketch image
    cv2.imwrite(output_path, pencil_sketch)