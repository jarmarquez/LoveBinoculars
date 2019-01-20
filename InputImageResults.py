from CustomImage import *


def determine_user_data():

    """
    This function returns the data for the user
    """

    # Path name for test images
    source1 = "Images/User/Test Images/Image1.JPEG"
    source2 = "Images/User/Test Images/Image2.JPEG"
    source3 = "Images/User/Test Images/Image3.JPEG"
    source4 = "Images/User/Test Images/Image4.JPEG"
    source5 = "Images/User/Test Images/Image5.JPEG"

    # Path name for detected images
    dest1 = "Images/User/Detected Images/Image1.JPEG"
    dest2 = "Images/User/Detected Images/Image2.JPEG"
    dest3 = "Images/User/Detected Images/Image3.JPEG"
    dest4 = "Images/User/Detected Images/Image4.JPEG"
    dest5 = "Images/User/Detected Images/Image5.JPEG"

    # Path name for isolated faces
    dest11 = "Images/User/Training Data/Image1.JPEG"
    dest12 = "Images/User/Training Data/Image2.JPEG"
    dest13 = "Images/User/Training Data/Image3.JPEG"
    dest14 = "Images/User/Training Data/Image4.JPEG"
    dest15 = "Images/User/Training Data/Image5.JPEG"

    # Create
    Images(source1).face_detector()
    Images(source2).face_detector()
    Images(source3).face_detector()
    Images(source4).face_detector()
    Images(source5).face_detector()

    # Save data
    save_detected_image(source1, dest1, dest11)
    save_detected_image(source2, dest2, dest12)
    save_detected_image(source3, dest3, dest13)
    save_detected_image(source4, dest4, dest14)
    save_detected_image(source5, dest5, dest15)


def determine_so_data():

    """
    This function returns the data for the user
    """

    # Path name for test images
    source1 = "Images/SO/Test Images/Image1.jpg"
    source2 = "Images/SO/Test Images/Image2.jpg"
    source3 = "Images/SO/Test Images/Image3.jpg"

    # Path name for detected images
    dest1 = "Images/SO/Detected Images/Image1.jpg"
    dest2 = "Images/SO/Detected Images/Image2.jpg"
    dest3 = "Images/SO/Detected Images/Image3.jpg"

    # Path name for isolated faces
    dest11 = "Images/SO/Training Data/Image1.jpg"
    dest12 = "Images/SO/Training Data/Image2.jpg"
    dest13 = "Images/SO/Training Data/Image3.jpg"

    # Create
    Images(source1).face_detector()
    Images(source2).face_detector()
    Images(source3).face_detector()

    # Save data
    save_detected_image(source1, dest1, dest11)
    save_detected_image(source2, dest2, dest12)
    save_detected_image(source3, dest3, dest13)
