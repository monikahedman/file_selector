import sys, os, subprocess
import os.path


class FileBrowser:
    """
    Class to handle all file browsing, manipulation, and checking.
    """

    # CONSTRUCTOR ------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor for the file browser. Its initial state is the files in the user's system.
        """
        self.current_path = os.path.expanduser('~')
        self.get_files_in_dir()

    # GETTERS & SETTERS ------------------------------------------------------------------------------------------------

    def get_files(self):
        """
        Method to get the files stored in self.files
        :return: list of files in current directory
        """
        return self.files

    def get_current_path(self):
        """
        Method to get the current path being displayed
        :return: current full path
        """
        return self.current_path

    def set_current_path(self, path):
        """
        Takes path passed in as a parameter and sets it to the current path
        :param path: the new path
        """
        self.current_path = path

    # METHODS ----------------------------------------------------------------------------------------------------------

    def is_dir(self, file):
        """Indicates if the file passed in as the parameter is a folder or a
        regular file. This acts as a wrapper for the is_dir function and allows
        for only the file name to be passed in as a parameter.

        :param file: Name of the file to check
        :return: A boolean indicating if file is a regular file or folder
        """
        full_path = self.current_path + "/" + file
        return os.path.isdir(full_path)

    def get_files_in_dir(self):
        """
        This function gets the list of all files in the current directory, which
        is stored in self.current_path.
        :return: The list of file names in the current directory
        """
        all_files = os.listdir(self.current_path)
        self.files = []
        for file in all_files:
            if not FileBrowser.is_hidden_file(file):
                self.files.append(file)
        self.files.sort()
        return self.files

    def get_parent_path(self):
        """
        This function gets the parent path of the current path. It does not
        set the parent path to the current path.
        :return: The parent path
        """
        return os.path.abspath(os.path.join(self.current_path, os.pardir))

    @staticmethod
    def is_hidden_file(name):
        """
        Method indicates if the file is a hidden file, which is indicated by "." preceding the file name. This program
        does not show hidden files.
        :param name: name of file to check
        """
        if name[0] == ".":
            return True
        return False

    def open_file(self, filename):
        """
        Opens file with the name passed in as a parameter. Appends the name to the current directory and opens with the
        specific call needed for the operating system
        :param filename: name of file to open
        """
        filename = self.current_path + "/" + filename
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, filename])
