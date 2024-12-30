from classes import Processus, GanttGraph
from data import generateTestData as gtd
from ordannacement.cooperatif import Fifo_Coop, Round_Robin_Coop, SRTF_Coop
from ordannacement.premtif import Fifo_Prem, Round_Robin_Prem, SRTF_Prem

import pandas as pd
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QSpinBox,
    QMessageBox,
    QGroupBox,
    QFileDialog,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

dataTest = gtd()


class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=8, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        fig.tight_layout()


class AppGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Scheduler")
        self.setGeometry(100, 100, 1000, 600)  # Increased window size for plot

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create horizontal layout for controls and plot
        h_layout = QHBoxLayout()

        # Left panel for controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # Data input selection
        input_group = QGroupBox("Data Input Selection")
        input_layout = QHBoxLayout()

        self.data_source = QComboBox()
        self.data_source.setToolTip("Select the method for data input.")
        self.data_source.addItems(["Direct Input", "Ready Data", "Test Data"])
        input_layout.addWidget(QLabel("Data Source:"))
        input_layout.addWidget(self.data_source)
        input_group.setLayout(input_layout)
        left_layout.addWidget(input_group)

        # Process table
        table_group = QGroupBox("Process Table")
        table_layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Entry", "CPUs", "Priority"])

        # Table controls
        table_controls = QHBoxLayout()
        self.add_process_btn = QPushButton("Add Process")
        self.remove_process_btn = QPushButton("Remove Selected")
        table_controls.addWidget(self.add_process_btn)
        table_controls.addWidget(self.remove_process_btn)

        # Regenerate Test Data Button
        self.regenerate_test_btn = QPushButton("Regenerate Test Data")
        left_layout.addWidget(self.regenerate_test_btn)
        self.regenerate_test_btn.clicked.connect(self.regenerate_test_data)

        table_layout.addLayout(table_controls)
        table_layout.addWidget(self.table)
        table_group.setLayout(table_layout)
        left_layout.addWidget(table_group)

        # Algorithm selection
        algo_group = QGroupBox("Algorithm Selection")
        algo_layout = QVBoxLayout()

        self.algo_combo = QComboBox()
        self.algo_combo.addItems(
            [
                "FIFO Cooperative",
                "FIFO Preemptive",
                "Round-Robin Cooperative",
                "Round-Robin Preemptive",
                "Shortest Remaining Time First Cooperative",
                "Shortest Remaining Time First Preemptive",
            ]
        )
        algo_layout.addWidget(QLabel("Select Algorithm:"))
        algo_layout.addWidget(self.algo_combo)

        # Quantum input
        quantum_layout = QHBoxLayout()
        self.quantum_spin = QSpinBox()
        self.quantum_spin.setRange(1, 100)
        self.quantum_spin.setValue(2)
        self.quantum_spin.setEnabled(False)
        quantum_layout.addWidget(QLabel("Quantum:"))
        quantum_layout.addWidget(self.quantum_spin)
        algo_layout.addLayout(quantum_layout)

        algo_group.setLayout(algo_layout)
        left_layout.addWidget(algo_group)

        # Generate button
        self.generate_btn = QPushButton("Generate Gantt Chart")
        left_layout.addWidget(self.generate_btn)

        # Add left panel to horizontal layout
        h_layout.addWidget(left_panel, stretch=40)

        # Right panel for plot
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # Create matplotlib canvas
        self.canvas = MatplotlibCanvas()
        right_layout.addWidget(self.canvas)

        # Add right panel to horizontal layout
        h_layout.addWidget(right_panel, stretch=60)

        # Add horizontal layout to main layout
        layout.addLayout(h_layout)

        # Create Gantt graph instance
        self.gantt = GanttGraph(self.canvas, isGui=True)

        # Connect signals
        self.data_source.currentIndexChanged.connect(self.update_data_source)
        self.algo_combo.currentIndexChanged.connect(self.update_quantum_visibility)
        self.generate_btn.clicked.connect(self.generate_chart)
        self.add_process_btn.clicked.connect(self.add_process)
        self.remove_process_btn.clicked.connect(self.remove_selected_process)

        # Initialize UI state
        self.update_data_source(0)
        self.update_controls_visibility()

    def update_controls_visibility(self):
        is_console = (
            self.data_source.currentText() == "Direct Input"
            or self.data_source.currentText() == "Test Data"
        )
        self.add_process_btn.setVisible(is_console)
        self.remove_process_btn.setVisible(is_console)
        self.table.setEnabled(is_console)
        # Show the regenerate button only if "Test Data" is selected
        is_test_data = self.data_source.currentText() == "Test Data"
        self.regenerate_test_btn.setVisible(is_test_data)

    def add_process(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

        # Add default values
        self.table.setItem(row_count, 0, QTableWidgetItem(f"P{row_count}"))
        for col in range(1, 4):
            self.table.setItem(row_count, col, QTableWidgetItem("0"))

    def regenerate_test_data(self):
        """Regenerate test data and update the process table."""
        self.table.clearContents()
        self.table.setRowCount(0)

        # Generate new test data
        dataTest = gtd()

        # Populate the table with new test data
        for process in dataTest:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(process.name))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(process.entry)))
            self.table.setItem(row_position, 2, QTableWidgetItem(str(process.cpu)))
            self.table.setItem(row_position, 3, QTableWidgetItem(str(process.priority)))

    def remove_selected_process(self):
        selected_rows = set(item.row() for item in self.table.selectedItems())
        for row in sorted(selected_rows, reverse=True):
            self.table.removeRow(row)

    def update_quantum_visibility(self, index):
        algorithm = self.algo_combo.currentText()
        self.quantum_spin.setEnabled("Round-Robin" in algorithm)

    def update_data_source(self, index):
        self.table.clearContents()
        self.table.setRowCount(0)

        if self.data_source.currentText() == "Ready Data":
            self.load_from_csv()
        elif self.data_source.currentText() == "Test Data":
            self.load_test_data()

        self.update_controls_visibility()

    def load_from_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Process Data File", "", "CSV Files (*.csv)"
        )

        if file_path:
            try:
                df = pd.read_csv(file_path)
                required_columns = ["Name", "Entry", "CPUs", "Priority"]

                if not all(col in df.columns for col in required_columns):
                    raise ValueError(
                        "CSV must contain columns: Name, Entry, CPUs, Priority"
                    )

                for _, row in df.iterrows():
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    for col, value in enumerate(row[required_columns]):
                        self.table.setItem(
                            row_position, col, QTableWidgetItem(str(value))
                        )

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load CSV: {str(e)}")
                self.data_source.setCurrentIndex(0)  # Reset to Direct Input

    def load_test_data(self):
        for process in dataTest:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(process.name))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(process.entry)))
            self.table.setItem(row_position, 2, QTableWidgetItem(str(process.cpu)))
            self.table.setItem(row_position, 3, QTableWidgetItem(str(process.priority)))

    def get_table_data(self):
        data = []
        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text()
            entry = int(self.table.item(row, 1).text())
            cpu = int(self.table.item(row, 2).text())
            priority = int(self.table.item(row, 3).text())
            data.append(Processus(name, entry, cpu, priority))
        return data

    def generate_chart(self):
        try:
            if self.table.rowCount() == 0:
                QMessageBox.warning(self, "Warning", "No processes to schedule.")
                return
            data = self.get_table_data()
            algorithm = self.algo_combo.currentText()
            if (
                algorithm in ["Round-Robin Cooperative", "Round-Robin Preemptive"]
                and self.quantum_spin.value() <= 0
            ):
                QMessageBox.warning(
                    self, "Warning", "Quantum value must be greater than 0."
                )
                return

            # Clear previous plot
            self.canvas.axes.clear()

            # Update Gantt title
            self.gantt.setTitle(algorithm)

            # Get Gantt data based on selected algorithm
            if algorithm == "FIFO Cooperative":
                gantt_data = Fifo_Coop(data)
            elif algorithm == "FIFO Preemptive":
                gantt_data = Fifo_Prem(data)
            elif algorithm == "Round-Robin Cooperative":
                gantt_data = Round_Robin_Coop(data, self.quantum_spin.value())
            elif algorithm == "Round-Robin Preemptive":
                gantt_data = Round_Robin_Prem(data, self.quantum_spin.value())
            elif algorithm == "Shortest Remaining Time First Cooperative":
                gantt_data = SRTF_Coop(data)
            elif algorithm == "Shortest Remaining Time First Preemptive":
                gantt_data = SRTF_Prem(data)

            # Draw the Gantt chart
            self.gantt.drawGraph(gantt_data)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
