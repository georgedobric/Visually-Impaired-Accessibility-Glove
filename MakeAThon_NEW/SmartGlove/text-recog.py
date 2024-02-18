import cv2
import easyocr
import matplotlib.pyplot as plt

def img2text(image_path):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the image inline
    plt.imshow(frame_rgb)
    plt.axis('off')
    plt.show()

    reader = easyocr.Reader(['en'])  # Specify language(s) you want to recognize
    result = reader.readtext(image_path)
    for detection in result:
        _, text, _ = detection
        print(text)
    return result

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    cv2.imshow('frame', frame)
    img2text(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
