import cv2 


def web_cam_capture(cam):
    fps = int(cam.get(cv2.CAP_PROP_FPS))
    Width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    Height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    with open("assignment_1/solutions/camera_outputs.txt", "w") as f:
        f.write(f"fps: {fps}\nHeight: {Height}\nWidth: {Width} ")

    with open("assignment_1/solutions/camera_outputs.txt") as f:
        print(f.read())

def main():
    cam = cv2.VideoCapture(0)
    web_cam_capture(cam)
    
    
    
if __name__ == "__main__":
    main()