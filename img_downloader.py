import os
import requests

# Declarations of global variables
url = ""
html = b'\xff'


def link_check():
    """
    Checks if the link provided is correct and contents can be retrieved from it.
    If the link is invalid, the user is asked to enter a different link.
    """
    global url
    global html
    valid_link = False

    while not valid_link:
        url = input("\nPlease paste the image url:\n")

        if "http://" in url:
            valid_link = True

        elif "https://" in url:
            valid_link = True

    html = requests.get(url).content


def directory_check():
    """
    Selects a directory where the image will be saved.
    If a Pictures directory exists in Users or home user space directory,
    Image_Downloader directory is created there, otherwise the user is asked
    to specify a path where they want to save the image.
    """
    full_dir = os.path.dirname(__file__)
    parent = os.path.abspath(os.path.join(full_dir, os.pardir))
    dirs = parent.split("\\", -1)

    i = 1
    dir_name = dirs[-i]
    parent_dir = dirs[-i - 1]

    while True:

        if parent_dir == "Users":
            break

        elif parent_dir == "home":
            break

        else:
            i += 1
            dir_name = dirs[-i]
            parent_dir = dirs[-i - 1]

    dirs = full_dir.split(dir_name)
    target = dirs[0] + dir_name

    pictures = target + "/Pictures"

    if os.path.isdir(pictures):
        path = target + "/Pictures/Image_Downloader"

        if not os.path.isdir(path):
            os.mkdir(path)

        os.chdir(path)

    else:
        valid = False

        print("\nDefault path does not exist.")

        while not valid:

            input_path = input("\nPlease enter a path where you would like to save the picture:\n")

            if os.path.isdir(input_path):
                valid = True

                while True:
                    input_choice = input("\nWould you like to save the image in this directory or would you "
                                         "like to create another subdirectory for it?\n"
                                         "[1] - Save the image here\n"
                                         "[2] - Save the image to a subdirectory\n")

                    if input_choice == '1':
                        os.chdir(input_path)
                        break

                    elif input_choice == '2':
                        path = input_path + "/Image_Downloader"

                        if not os.path.isdir(path):
                            os.mkdir(path)

                        os.chdir(path)
                        break

                    else:
                        print("\nPlease enter an option 1 or 2.\n")

            else:
                print("\nThe input path is not valid.")


def extension_check():
    """
    Asks the user to name the image, and checks for the extension.

    :return: Name with extension of the image
    """
    name = input("\nWhat would you like to name the picture?\n")

    if ".png" in url:
        extension = ".png"

    elif ".jpeg" in url:
        extension = ".jpeg"

    elif ".jpg" in url:
        extension = ".jpg"

    elif ".gif" in url:
        extension = ".gif"

    else:
        url_parts = url.split(".")
        extension = "." + url_parts[-1]
        print("\nThe extension is unusual, saved file may be corrupted.")

    return name + extension


def download(filename):
    """
    Downloads the image.

    :param filename: The name of the image.
    """
    with open(filename, "wb") as f:
        f.write(html)


def run():
    """
    Runs the general UI and relevant functions.
    """
    link_check()
    directory_check()

    try:
        download(extension_check())
        print("\nDownload was successful. The image is stored in " + os.getcwd())
        post_save()

    except OSError:
        print("\nThe image link extension was invalid.\n")
        run()


def post_save():
    """
    After an image was saved, the user is asked whether they would like to save
    another image or quit the program.
    """
    while True:
        choice = input("\nWould you like to save another image?\n"
                       "[1] - Yes\n"
                       "[2] - No\n")

        if choice == '1':
            run()
            break

        elif choice == '2':
            print("\nHave a good day.")
            exit(0)

        else:
            print("\nPlease enter an option 1 or 2.\n")


run()
