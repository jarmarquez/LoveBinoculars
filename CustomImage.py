import cv2


class Images:

    def __init__(self, source):
        self.source = source
        self.read = cv2.imread(self.source)

    def show_original(self):

        """
        This function shows the original image
        :return: Original image
        """

        cv2.imshow("Window", self.read)
        cv2.waitKey(0)  # Window doesn't close until a key is pressed

    def face_detector(self):

        """
        This function takes an image and saves a copy of the image but with the face detected
        :return: 0 - The identified face, 1 - The copy of the image with the detected face
        """

        # Create a copy of image so we don't affect the original
        img_copy = self.read.copy()

        # Convert image to grayscale
        gray_img = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        gray_img_crp = gray_img

        # Load local binary patterns classifier
        lbp_face_cascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")

        # Display identified face
        identified_face = lbp_face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=6)

        # Obtain coordinates for face and superimpose rectangle onto copied image
        for (x, y, w, h) in identified_face:
            cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 0), thickness=2)

        # Cropped face data
        (x, y, w, h) = identified_face[0]
        identified_face = gray_img_crp[y:y+w, x:x+h]

        # Return the function
        return [identified_face, img_copy]


def save_detected_image(source, destination, destination2):

    """
    This function saves the detected facial image from the Images class
    :param source: file path source
    :param destination: file path detected image destination
    :param destination2: file path cropped face destination
    :return: void
    """

    facial_detection = Images(source).face_detector()
    cropped_face = facial_detection[0]
    complete_picture_with_detection = facial_detection[1]

    cv2.imwrite(destination, complete_picture_with_detection)

    cv2.imwrite(destination2, cropped_face)

    return
