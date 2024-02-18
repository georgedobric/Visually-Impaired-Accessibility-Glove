import pytesseract
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches



"""
def img2text(image_path):
    reader = easyocr.Reader(['en'])  # Specify language(s) you want to recognize
    result = reader.readtext(image_path)

    closest = None

    for detection in result:
        _, text, _ = detection
        '''print ("New Capture:")
        print(text, _)
        '''
        if closest is None:
            closest = detection
            continue

        pos, test, pos = closest

        if abs(_ - 0.5) < abs(pos - 0.5):
            #print(_, text, pos, test)
            closest = detection
    if closest is not None:
        _, text, _ = closest
        print(text, _)
        
    return result

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    #cv2.imshow('frame', frame)
    img2text(frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

"""

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\shaka\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# we get some video input from controller or phone
# it can be either just a single image or multiple determining on time
# this will be a list of paths to images or just a single path if only one image
'''
------------------------
START OF TESSERACT STUFF
------------------------
'''

image_path_list = []


# function to preprocess image to easy to decipher text vs background
def image_preprocesser(path: str):
    # Read image from which text needs to be extracted
    img = cv2.imread(path)
    img = cv2.resize(img, (800, 800))
    # Preprocessing the image starts

    # Convert the image to gray scale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #file = open("images/hopefullythisworks.png", "w+")
    cv2.imwrite("images/hopefullythisworks.png", grey)
    return grey

# Separate image into blocks of text (I think we only want the central one as that is the one that matters)
def image_text_blocks(image):
    # Performing OTSU threshold
    #ret, thresh1 = cv2.threshold(image, 100, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    #image = cv2.resize(image, (800, 800))
    ret, thresh1 = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY_INV)
    #print(thresh1)
    #print(ret)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    #rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))

    # Applying dilation on the threshold image
    #dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    #contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
     #                                      cv2.CHAIN_APPROX_NONE)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print(len(contours))
    # Display the image using matplotlib
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("contour_image")

    contours1 = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 5 and h > 5:
            contours1.append(cnt)
            pass
    for cnt in contours1:
        x, y, w, h = cv2.boundingRect(cnt)
        print(x, y, w, h)
        plt.gca().add_patch(patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none'))
    # returning blocks of text for image (may need to re-add sending back a copy of image
    plt.show()
    return contours1, hierarchy

def test_it(img, contours):
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        # print(x, y, w, h)
        # mid_box_x = (x + w) / 2
        # mid_box_y = (y + h) / 2

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = img[y:y + h, x:x + w]

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        print(text)

# find middle box
def get_middle_box(img, contours, hierarchy):
    #print(img.shape)

    height, width = img.shape

    mid_img_y = height / 2
    mid_img_x = width / 2
    print(width, mid_img_x, height, mid_img_y)
    print("--- going into contours --")
    real_middle_box = None


    print(len(contours))
    # finding middle box
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        #print(x, y, w, h)
        #mid_box_x = (x + w) / 2
        #mid_box_y = (y + h) / 2

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = img[y:y + h, x:x + w]

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)


        if text.strip().replace(" ", "").replace("\t", "").replace("\n", "") == '':
            continue
        print(text + "hi", end='')
        #print("New Box:")
        #print("TEXT!!!:\n")
        #print(text)
        #print(mid_box_x, mid_box_y)
        if real_middle_box is None:
            #rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #real_middle_box = img[y:y + h, x:x + w]
            real_middle_box = cnt
            continue
        '''
        # check if middle point is within a box first
        if ( mid_img_x >= x and mid_img_x  <= x + w and mid_img_y >= y and mid_img_y <= y + h):
            # we are within a box let's break
            #real_middle_box = img[y:y + h, x:x + w]
            #print
            real_middle_box = cnt
            continue
        '''

        # if we reach here we must have not found a box yet that we're within so compare distances

        dist_new_box_x = min(abs(mid_img_x - x), abs(mid_img_x - (x + w)))
        dist_new_box_y = min(abs(mid_img_y - y), abs(mid_img_y - (y + h)))

        old_x, old_y, old_w, old_h = cv2.boundingRect(real_middle_box)
        dist_old_box_x = min(abs(mid_img_x - old_x), abs(mid_img_x - (old_x + old_w)))
        dist_old_box_y = min(abs(mid_img_y - old_y), abs(mid_img_y - (old_y + old_h)))

        if ((dist_new_box_x + dist_new_box_y) < (dist_old_box_x + dist_old_box_y)):
            real_middle_box = cnt

        #if ( min(()))
    if real_middle_box is not None:
        print("This is the middle box:\n")
        print(cv2.boundingRect(real_middle_box))
        #local_dist = abs(mid_box_x)

    x, y, w, h = cv2.boundingRect(real_middle_box)
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return real_middle_box

# Get the characters and find the middle of the screen character (Not character in middle of text block)

def process_image(img, cnt, hierarchy):
    # A text file is created and flushed
    file = open("test_recognized.txt", "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file

    '''
    # finding middle box
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)


        # otherwise we already have one we think its middle box, lets compare



        # Drawing a rectangle on copied image
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = img[y:y + h, x:x + w]

        # Open the file in append mode
        file = open("test_recognized.txt", "a")

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        # Appending the text into file
        file.write(text)
        file.write("\n")

        # Close the file
        file.close
    '''
    x, y, w, h = cv2.boundingRect(cnt)

    # otherwise we already have one we think its middle box, lets compare

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = img[y:y + h, x:x + w]

    # Open the file in append mode
    file = open("test_recognized.txt", "a")

    #cv2.imwrite("images/again.jpg", cropped)

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped, lang='eng', config='--psm 7')
    #print("TEXT!!!:\n")
    #print(text)
    # Appending the text into file
    file.write(text)
    file.write("\n")

    # Close the file
    file.close()


#x = image_preprocesser("images/sample.jpg")
x = image_preprocesser("images/reorient.jpg")
y,z = image_text_blocks(x)
test_it(x, y)
#q = get_middle_box(x.copy(), y, z)
#process_image(x.copy(), q, z)

#process_image(x.copy(), y, z)



# Convert the character to braille

# send braille to qualcomm


# qualcomm will fire off sensors (not from program)

'''
def read_pdf(path: str):

    # open and create pdf object
    pdf_obj = open(path, 'rb')

    pdf_reader = PyPDF2.PdfReader(pdf_obj)

    #pdf_pages = len(pdfReader.pages)
    pdf_pages = pdf_reader.pages

    pages_text_list = []

    for pdf_page in pdf_pages:
        pages_text_list.append(pdf_page.extract_text())

    #print(pdf_reader.pages[0].extract_text())
    pdf_obj.close()

    return pages_text_list
'''





# reading the pdf test
'''x = read_pdf("pdfs/larger_test.pdf")
print(len(x))
print("\n")
for y in x:
    print("New Page:\n")
    print(y)
#print(x[0])
'''


'''def extract_pdf_page_text(pdf_page) -> str:
    # get text
    return pdf_page.extract_text()



# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print(len(pdfReader.pages))

# creating a page object
pageObj = pdfReader.pages[0]

# extracting text from page
print(pageObj.extract_text())

# closing the pdf file object
pdfFileObj.close()
'''


'''
# Read image from which text needs to be extracted
img = cv2.imread("images/sample.jpg")

# Preprocessing the image starts

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

print(type(im2))

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]

    # Open the file in append mode
    file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)

    # Appending the text into file
    file.write(text)
    file.write("\n")

    # Close the file
    file.close


'''

