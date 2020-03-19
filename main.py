import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore
from ui_mainwindow import Ui_MainWindow
from collapser import Collapser
from filebrowser import FileBrowser
from funcs import *


class MainWindow(QMainWindow):
    """
    This class handles all of the UI elements and how they operate and connect to the logical pieces.
    """

    # CONSTRUCTOR ------------------------------------------------------------------------------------------------------

    def __init__(self, app):
        super(MainWindow, self).__init__()

        # Instance Variables
        self.ui = Ui_MainWindow()
        self.app = app
        self.fb = FileBrowser()
        self.collapser = Collapser()
        self.widgets = []

        # Sets up UI based on the auto-generated python file
        self.ui.setupUi(self)

        # Sets up all initial functionality for the program
        self.setup_functionality()

    # METHODS ----------------------------------------------------------------------------------------------------------

    def move_forward(self):
        """
        Navigates forwards visually in the file tree if only one folder is selected. If more than one folder is
        selected OR a regular file is selected, then nothing happens.
        """
        widgets = self.ui.systemTreeWidget.selectedItems()
        # if there is one item selected
        if len(widgets) == 1:
            widget = widgets[0]
            # If it is a folder, not a regular file
            if widget.text(2) == "Folder":
                # Updates current path in the filebrowser for the logical side of the file system
                current_path = self.fb.get_current_path()
                new_path = current_path + "/" + widget.text(0)
                self.update_path(new_path)

    def move_back(self):
        """
        Navigates backwards in the file tree to the parent directory visually.
        """
        new_path = self.fb.get_parent_path()
        self.update_path(new_path)

    def update_path(self, new_path):
        """
        This method handles everything that goes with changing the file path regardless of which direction the
        movement is happening in. It clears the trees containing the current files so the new ones can be displayed,
        clears the list of widgets, sets the text in the line edit, logically upadtes the path in the file browser,
        and lastly updates the visual file browser in the left tree.
        :param new_path: the new path to display
        """
        self.ui.systemTreeWidget.clear()
        self.ui.selectedTreeWidget.clear()
        clear_list(self.widgets)
        self.ui.pathLineEdit.setText(new_path)
        self.fb.set_current_path(new_path)
        self.populate_system_tree()

    def update_multi_select_option(self):
        """
        Method updates the type of selection when the user clicks the multi select checkbox. Either enables multi or
        single selection using helper methods.
        """
        if self.ui.multiCheckBox.isChecked():
            self.setup_multi_select()
        else:
            self.setup_single_select()

    def setup_functionality(self):
        """
        This method sets up all of the miscellaneous functionality that is not part of setupUI.
        """
        # Populates the left tree with the user's base folder
        self.populate_system_tree()
        # Sets the contents of the line edit to the the current path
        self.ui.pathLineEdit.setText(self.fb.get_current_path())
        # Connects all buttons and functionalities
        self.connect_buttons()
        # Sets up multi-select (multi-select is on by default)
        self.setup_multi_select()
        # Establishes connection between right tree and double click event
        self.ui.selectedTreeWidget.itemDoubleClicked.connect(self.on_double_click)
        # Sets the initial state of the multi-select checkbox to checked
        self.ui.multiCheckBox.setChecked(True)
        # Sets up connection between returnPressed and submitting the path change
        self.ui.pathLineEdit.returnPressed.connect(self.submit_path_change)

    def on_double_click(self):
        """
        This method handles a double click on a file in the righthand file browser. This opens a file or a folder
        in the operating system's default application.
        """
        # this should only be one since this widget only accepts one select
        items = self.ui.selectedTreeWidget.selectedItems()
        item_name = items[0].text(0)
        self.fb.open_file(item_name)

    def submit_path_change(self):
        """
        Submits the path change if it is made in the QLineEdit. Gets the value in the text edit and passes it into
        update_path to make all the necessary changes.
        """
        path = self.ui.pathLineEdit.text()
        self.update_path(path)

    def setup_multi_select(self):
        """
        This method enables multi selection on the lefthand file browser.
        """
        self.ui.systemTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

    def setup_single_select(self):
        """
        This method enables single selection on the lefthand file browser.
        """
        self.ui.systemTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    def select_all(self):
        """
        Selects all files in the lefthand browser and updates the right widget
        """
        self.ui.systemTreeWidget.selectAll()
        self.update_right_widget()

    def deselect_all(self):
        """
        Deselects all files in the lefthand browser and updates the right widget
        """
        self.ui.systemTreeWidget.clearSelection()
        self.update_right_widget()

    def update_right_widget(self):
        """
        This function is called whenever there is a click event registered in the app. To ensure the list isn't being
        updated unnecessarily, the current widgets are stored and the selected ones are compared to that list. If those
        lists are different, then the right widget is updated.
        :return:
        """
        self.widgets.sort()
        new_widgets = self.ui.systemTreeWidget.selectedItems()
        new_widgets.sort()
        if not self.ui.multiCheckBox.isChecked() or not self.widgets == new_widgets:
            equalize_lists(self.widgets, new_widgets)
            self.populate_selected_tree()
            self.set_expansion()

    def connect_buttons(self):
        """
        Connects all buttons and other click events to their corresponding functions
        """
        self.ui.expandCollapseButton.clicked.connect(self.expand_collapsed_clicked)
        self.ui.selectAllButton.clicked.connect(self.select_all)
        self.ui.deselectButton.clicked.connect(self.deselect_all)
        self.ui.backButton.clicked.connect(self.move_back)
        self.ui.forwardButton.clicked.connect(self.move_forward)
        self.ui.multiCheckBox.clicked.connect(self.update_multi_select_option)
        self.ui.goButton.clicked.connect(self.submit_path_change)

    def expand_collapsed_clicked(self):
        """
        Function for when the expand collapsed/collapse files button is pressed. Handles everything that needs to
        happen when the user presses that button.
        """
        # Sets the button to using the correct text and other ui elements
        exp_coll = "Expand Collapsed"
        coll = "Collapse Files"
        cur = self.ui.expandCollapseButton.text()
        should_expand = True if cur == exp_coll else False
        new = coll if should_expand else exp_coll
        self.ui.expandCollapseButton.setText(new)

        # Handles what happens to the actual files
        if should_expand:
            self.expand_collapsed_items()
        else:
            self.collapse_items()

    def set_expansion(self):
        exp_coll = "Expand Collapsed"
        coll = "Collapse Files"
        cur = self.ui.expandCollapseButton.text()
        should_expand = True if cur == coll else False
        # Handles what happens to the actual files
        if should_expand:
            self.expand_collapsed_items()
        else:
            self.collapse_items()

    def expand_collapsed_items(self):
        """
        Function to take the collapsed items and uncollapse them.
        """
        num_items = self.ui.selectedTreeWidget.topLevelItemCount()
        results = []
        for i in range(0, num_items):
            widget = self.ui.selectedTreeWidget.topLevelItem(i)
            # If the current widget item indicates it is collapsed or collapsible
            if str_to_bool(widget.text(1)):
                # Get list of all file names gotten from the collapsed name
                names = Collapser.get_names_from_condensed(widget.text(0))
                for name in names:
                    new_widg = QtWidgets.QTreeWidgetItem()
                    new_widg.setText(0, name)
                    new_widg.setText(1, widget.text(1))
                    results.append(new_widg)
            else:
                new_widg = QtWidgets.QTreeWidgetItem()
                new_widg.setText(0, widget.text(0))
                new_widg.setText(1, widget.text(1))
                results.append(new_widg)
        results.sort()
        self.ui.selectedTreeWidget.clear()
        # Add all widgets to the tree
        self.ui.selectedTreeWidget.addTopLevelItems(results)

    def collapse_items(self):
        """
        Function to collapse the uncollapsed items.
        """
        self.populate_selected_tree()

    def populate_system_tree(self):
        """
        This method populates the visual file browser on the lefthand side of the ui based on the path stored in the
        file browser. Creates all of the widgets and adds them to the tree.
        """
        # gets all filenames from the current path
        files = self.fb.get_files_in_dir()
        self.collapser.make_final_list(files)
        collapsedFiles = self.collapser.get_result_files()
        collapsedTF = self.collapser.get_collapsed_list()
        widgets = []
        # Create widgets to add to the tree list
        for i in range(0, len(collapsedFiles)):
            widget = QtWidgets.QTreeWidgetItem()
            widget.setText(0, collapsedFiles[i])
            type = "Folder" if self.fb.is_dir(collapsedFiles[i]) else "File"
            widget.setText(2, type)
            collapsed = "Yes" if collapsedTF[i] else "No"
            widget.setText(1, collapsed)
            widgets.append(widget)
        # Add all widgets to the tree
        self.ui.systemTreeWidget.addTopLevelItems(widgets)

    def populate_selected_tree(self):
        """
        This method populates the righthand tree of files. This is called whenever a new file is selected or deselected.
        It creates new widgets based on the old and adds them to the other tree.
        """
        # Clears any old widgets so duplicates are not added
        self.ui.selectedTreeWidget.clear()
        new_widgets = []
        for widget in self.widgets:
            new_widg = QtWidgets.QTreeWidgetItem()
            name = widget.text(0)
            new_widg.setText(0, name)
            new_widg.setText(1, widget.text(1))
            new_widgets.append(new_widg)
        new_widgets.sort()
        # Add all widgets to the tree
        self.ui.selectedTreeWidget.addTopLevelItems(new_widgets)


class MouseDetector(QtCore.QObject):
    """
    This class deals with general mouse events for the purpose of updating the right widget.
    """

    # CONSTRUCTOR ------------------------------------------------------------------------------------------------------

    def __init__(self, main_window):
        """
        Constructor for the mouse handler. Acts on the main window, which is passed in as a parameter. The main window
        contains the right widget, which is the widget affected by clicks.
        :param main_window: window containing the right widget
        """
        super(MouseDetector, self).__init__()
        self.window = main_window

    def eventFilter(self, obj, event):
        """
        General event handler. Used to add functionality to the click event to update the right pane.
        :param obj: Object being clicked
        :param event: Event Type
        :return: the event handler from the parent class
        """
        if event.type() == QtCore.QEvent.MouseButtonRelease:
            self.window.update_right_widget()
        return super(MouseDetector, self).eventFilter(obj, event)


if __name__ == "__main__":
    # Creates the app and the window containing the app
    app = QApplication(sys.argv)
    window = MainWindow(app)

    # Sets up the mouse handler
    mouseFilter = MouseDetector(window)
    app.installEventFilter(mouseFilter)

    window.show()
    sys.exit(app.exec_())
