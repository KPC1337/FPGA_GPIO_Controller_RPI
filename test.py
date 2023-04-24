from PySide6.QtWidgets import QApplication, QFileDialog
import csv

# create a QApplication instance
app = QApplication()

# open a file dialog to select a CSV file
file_dialog = QFileDialog()
file_dialog.setNameFilter("CSV files (*.csv)")
if file_dialog.exec_() == QFileDialog.Accepted:
    selected_file = file_dialog.selectedFiles()[0]
else:
    # user cancelled the file dialog
    selected_file = None

# parse the CSV file and create the dictionaries
if selected_file is not None:
    dictionaries = []
    current_dict = None

    with open(selected_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')

        for row in reader:
            if row[0] == '-':  # found end of dictionary
                current_dict = None
            elif row[0] == '/':  # found separator line
                current_dict = {}
                dictionaries.append(current_dict)
            elif current_dict is not None:  # data for current dictionary
                key = row[0]
                values = [[(row[i]), (row[i+1])] for i in range(1, len(row), 2)]
                current_dict[key] = values
            else:
                # first dictionary not preceded by separator line
                current_dict = {}
                dictionaries.append(current_dict)
                key = row[0]
                values = [[(row[i]), (row[i+1])] for i in range(1, len(row), 2)]
                current_dict[key] = values

    # do something with the dictionaries
    print(dictionaries)

# exit the application
app.exit()
