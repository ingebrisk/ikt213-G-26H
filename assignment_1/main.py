import cv2

def print_image_information(image):
    Height, Width, Channels = image.shape
    print(f"Height: {Height}")
    print(f"Width: {Width}")
    print(f"Channels: {Channels}")
    print(f"Size: {image.size}")
    print(f"Data type: {image.dtype}")


def main():
    image = cv2.imread("iris-1.jpg")
    print_image_information(image)
    
if __name__ == "__main__":
    main()