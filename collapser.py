from funcs import *

# Constant indicating if the dot separated names (i.e. hello.world.001.jpg) should be condensed or not
CONDENSE_DOT_SEPARATED = True

class Collapser:
    """
    This class handles all of the collapsing that needs to be done with files. It does all name manipulation and
    checking of file names. It also stores all result files and the indicators that they were collapsed.

    This program assumes that hello.world.001.jpg is a valid file name to condense. This can be easily modified by
    changing the boolean CONDENSE_DOT_SEPARATED to false.
    """

    # CONSTRUCTOR ------------------------------------------------------------------------------------------------------

    def __init__(self):
        """
        Constructor creates the necessary lists
        """
        self.res = []
        self.condensed = []

    # GETTERS & SETTERS ------------------------------------------------------------------------------------------------

    def get_result_files(self):
        """
        This method gets the list of result files stored in the file browser.
        :return: List of files
        """
        return self.res

    def get_collapsed_list(self):
        """
        This method gets the list of booleans associated with each file, which indicates if the file has been
        collapsed or not.
        :return: List of booleans
        """
        return self.condensed

    # METHODS ----------------------------------------------------------------------------------------------------------

    def make_final_list(self, entries):
        """
        This hefty method creates the final list of files, which includes the condensed versions of files. The bulk of
        the logic handles when something should be collapsed.
        :param entries: The list of files to potentially condense
        :return: The final list of files that include condensed file names
        """
        # Clears old lists to make sure that there are no duplicates
        clear_list(self.res)
        clear_list(self.condensed)

        # All initial variables
        name = ""
        frame_padding = 0
        start_range = 0
        end_range = 0
        should_update_vals = False                  # Variable indicates if the various values should be updated or not

        for i in range(0, len(entries)):
            # if the entry can be condensed, look forward in the list
            if Collapser.should_condense(entries[i]):

                # splits current filename into pieces
                file_parts = entries[i].split('.')

                # Set the initial values if there are none set already, or sets them if the variable indicates to
                if i == 0 or should_update_vals:
                    name = Collapser.get_name(file_parts)
                    frame_padding = Collapser.get_buffer(file_parts)
                    start_range = Collapser.get_iteration(file_parts)
                    end_range = Collapser.get_iteration(file_parts)
                    should_update_vals = False      # Updates this so no unecessary changes are made

                # if it's not the last entry in the list
                if Collapser.is_not_last(i, entries):
                    next_file = entries[i + 1].split('.')
                    end_range = Collapser.get_iteration(file_parts)
                    # if the next file should not be condensed up into the current one
                    if not Collapser.should_condense_up(file_parts, next_file):
                        should_update_vals = True
                        ext = file_parts[len(file_parts) - 1]
                        self.res.append(Collapser.get_condensed_filename(name, frame_padding, ext, start_range, end_range))
                        self.condensed.append(True)
                # if it is the last file on the list
                else:
                    ext = file_parts[len(file_parts) - 1]
                    self.res.append(Collapser.get_condensed_filename(name, frame_padding, ext, start_range, end_range))
                    self.condensed.append(True)

            # if the entry can't be condensed, then add it to the result list
            # and continue looking
            else:
                self.res.append(entries[i])
                self.condensed.append(False)

    @staticmethod
    def should_condense(filename):
        """
        This function returns a boolean indicating if the file name is in the correct format to be collapsed.
        :param filename: name of the file to check
        :return: if the file should be collapsed
        """
        # splits string at each '.' to make sure that each piece of the filename
        # is correct for condensing. file_parts[length-1] will always be the file
        # extension, and file_parts[length-2] should be the buffer
        file_parts = filename.split('.')

        # there always must be at least 3 elements in the array (name, buffer, ext)
        if len(file_parts) < 3:
            return False

        # if not condensing dot separated names (i.e. hello.world.001.jpg), then
        # there cannot be more than 3 elements in the array of file parts.
        if not CONDENSE_DOT_SEPARATED and len(file_parts) > 3:
            return False

        # since the check for condensing dot separated is already done, this
        # will always be the final indicator for if a file should be condensed
        if is_num(file_parts[len(file_parts)-2]):
            return True

    @staticmethod
    def get_names_from_condensed(condensed_name):
        """
        This method gets a list of file names from one condensed name. Because the structure of the condensed name is
        set, it can develop the original file names from the condensed name.
        Structure: [baseName].%[frame_padding].[extension] [startFrame]-[endFrame]
        :param condensed_name: name of the condensed file
        :return: the list of the original file names
        """

        # first, split on space then dash
        filename = condensed_name.split(" ")[0]
        basename = Collapser.get_basename_from_condensed(filename)
        ext = Collapser.get_ext(filename)
        frame_padding = Collapser.get_frame_padding(filename)
        iter_range = condensed_name.split(" ")[1]
        start = iter_range.split("-")[0]
        end = iter_range.split("-")[1]
        final_list = []

        for i in range(int(start), int(end) + 1):
            padding = Collapser.make_padding(i, frame_padding)
            uncondensed = basename + padding + "." + ext
            final_list.append(uncondensed)

        return final_list

    @staticmethod
    def get_frame_padding(name):
        """
        This method gets the length of the padding from the condensed file name specification. For example, in the file
        hello_world.004.jpg, the value returned from the condensed name would be 3 because there are 3 digits in the
        frame padding.
        :param name: name of the condensed file
        :return: the frame padding
        """
        file_parts = name.split(".")
        # Get the string associated with the padding and modify it as necessary
        padding_string = file_parts[len(file_parts) - 2]
        padding_string = padding_string.replace("%0", "")
        padding_num = padding_string.replace("d", "")
        return int(padding_num)

    @staticmethod
    def make_padding(iteration, padding):
        """
        Makes the frame padding string. It takes the current iteration (i.e. 4) and the padding (i.e. 3) and turns
        it into 004.
        :param iteration: the current iteration
        :param padding: the number of digits that should be in the frame padding
        :return: the frame padding number
        """
        final_str = str(iteration)
        while len(final_str) < padding:
            final_str = "0" + final_str
        return final_str

    @staticmethod
    def get_ext(name):
        """
        Gets the extension of a file. Assumed that the extension is always following the last "." in the file name
        :param name: name of the file
        :return: the extension of the file
        """
        file_parts = name.split(".")
        return file_parts[len(file_parts) - 1]

    @staticmethod
    def get_basename_from_condensed(name):
        """
        This method takes in a condensed file name and returns the basename.
        Note: this adds a "." to the end of each name
        :param name: Condensed name of the file
        :return: the basename of the file
        """
        file_parts = name.split(".")
        # removing the last two elements removes the extension and the frame_padding
        file_parts = file_parts[:len(file_parts) - 2]
        to_return = ""
        for part in file_parts:
            to_return += part + "."
        return to_return

    @staticmethod
    def should_condense_up(current_entry, next_entry):
        """
        This method decides if the next entry can be condensed up into the existing one. The name needs to be the same
        and the number needs to be one higher than the previous
        :param current_entry: current file name
        :param next_entry: next file name
        :return: if the next file can be collapsed up into the current one
        """
        # if names aren't the same, return false
        if Collapser.get_name(current_entry) != Collapser.get_name(next_entry):
            return False
        # If the next file is one "higher", it can be condensed up
        file_count_1 = Collapser.get_iteration(current_entry)
        file_count_2 = Collapser.get_iteration(next_entry)
        return file_count_2 == file_count_1 + 1

    @staticmethod
    def get_condensed_filename(basename, frame_padding, extension, start, end):
        """
        This method takes all the individual pieces of a file name and puts them together to make the condensed name.
        :param basename: base name of the file. helloworld.001.jpg would be helloworld.
        :param frame_padding: Number of digits in the frame padding. In above example, fp would be 3
        :param extension: file extension, i.e. jpg
        :param start: Start range of iterations
        :param end: End range of iterations
        :return: the final string
        """
        return str(basename + ".%0" + str(frame_padding) + "d." + extension + " " + str(start) + "-" + str(end))

    @staticmethod
    def is_not_last(i, entries):
        """
        This method checks if the current index is the last index in the list. Made into helper for easier understanding
        of the condense method.
        :param i: current index
        :param entries: List being looped through
        :return: if this index is the last
        """
        return i < len(entries) - 1

    @staticmethod
    def get_name(file_parts):
        """
        Gets the name of the file excluding the buffer and the extension. For example, helloworld.001.png would return
        helloworld, and hello.world.001.jpg would return hello.world
        :param file_parts: the file pre-split along the "."
        :return: the base name of the file
        """
        # if not condensing dot separated, then the name is simply the first
        # element in the list of parts
        if not CONDENSE_DOT_SEPARATED:
            return file_parts[0]
        # if it is condensing dot separated, then the entire set of parts before
        # the buffer needs to be part of the name
        else:
            string = ""
            for i in range(0, (len(file_parts) - 2)):
                string += file_parts[i]
                # add the '.' back in (because it's removed at the split)
                if i < len(file_parts) - 3:
                    string += "."
            return string

    @staticmethod
    def get_buffer(file_parts):
        """
        This method gets the length of the buffer. For example, in hello_world.001.jpg, this method would return 3. In
        this file name specification, the iteration is always the second to last item in the list.
        :param file_parts: the file pre-split along the "."
        :return: Length of the buffer
        """
        return len(file_parts[len(file_parts) - 2])

    @staticmethod
    def get_iteration(file_parts):
        """
        This method gets the integer associated with the specific iteration of this file.
        For example, in hello_world.002.jpg, 2 would be the returned value.
        :param file_parts: the file pre-split along the "."
        :return: the integer associated with this specific iteration
        """
        return int(file_parts[len(file_parts) - 2])