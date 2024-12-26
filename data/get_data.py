import csv
import tkinter as tk
from tkinter import filedialog
from classes import Processus


def get_data():
    data = []
    while True:
        try:
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename(
                title="Select a CSV file", filetypes=[("CSV Files", "*.csv")]
            )
            # Check if a file was selected
            if file_path:
                # Open the selected CSV file
                with open(file_path, mode="r") as file:
                    reader = csv.reader(file)

                    # Skip the header row if necessary
                    next(reader)  # Uncomment if there's a header row

                    # Loop through the rows and print them
                    for row in reader:
                        data.append(
                            Processus(row[0], row[1], row[2], row[3])
                        )  # Each row is a list
            else:
                print("No file selected")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            break
