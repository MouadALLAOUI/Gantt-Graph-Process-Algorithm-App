import sys
from classes import GanttGraph, AppGui
from ordannacement.cooperatif import Fifo_Coop, Round_Robin_Coop, SRTF_Coop
from ordannacement.premtif import Fifo_Prem, Round_Robin_Prem, SRTF_Prem
from data import setData, getData, generateTestData
from PyQt5.QtWidgets import QApplication

dataTest = generateTestData()


def main():
    graph = GanttGraph()
    data = []
    ganttData = []

    while True:
        try:
            print("=" * 20)
            print("Hello user,")
            print("\n\n")
            # Choose data entry method
            isEntryData = input(
                "Do you want to enter data via console (c) or use ready data (r) or test data (t)? [c/r/t]: "
            ).lower()
            if isEntryData in ["c", "console"]:
                data = setData()
            elif isEntryData in ["r", "ready"]:
                data = getData()
            elif isEntryData in ["t", "test"]:
                # + Just some decoration
                print("Process Table\n")
                print("-" * 40)
                print(f"| {'Name':^8}|{'Entry':^8}|{'CPUs':^8}|{'Priority':^8} |")
                print("-" * 40)
                for process in dataTest:
                    print(
                        f"| {process.name:^8}|{process.entry:^8}|{process.cpu:^8}|{process.priority:^8} |"
                    )
                    print("-" * 40)
                # + Decoration end
                data = dataTest
            else:
                print("Invalid choice. Please choose 'c' or 'r'.")
                continue

            # Choose algorithm
            alg = input(
                """Which algorithm would you like to use?
For 'FIFO Cooperative', type (fc)
For 'FIFO Preemptive', type (fp)
For 'Round-Robin Cooperative', type (rc)
For 'Round-Robin Preemptive', type (rp)
For 'Shortest Remaining Time First Cooperative', type (sc)
For 'Shortest Remaining Time First Preemptive', type (sp)
: """
            ).lower()
            if alg in ["fc", "fifo cooperative"]:
                graph.setTitle("FIFO Cooperative")
                ganttData = Fifo_Coop(data)
            elif alg in ["fp", "fifo preemptive"]:
                graph.setTitle("FIFO Preemptive")
                ganttData = Fifo_Prem(data)
            elif alg in ["rc", "round-robin cooperative"]:
                graph.setTitle("Round-Robin Cooperative")
                Quantum = int(input("Enter the quantum value: "))
                ganttData = Round_Robin_Coop(data, Quantum)
            elif alg in ["rp", "round-robin preemptive"]:
                graph.setTitle("Round-Robin Preemptive")
                Quantum = int(input("Enter the quantum value: "))
                ganttData = Round_Robin_Prem(data, Quantum)
            elif alg in ["sc", "shortest cooperative", "srtfc"]:
                graph.setTitle("Shortest Remaining Time First Cooperative")
                ganttData = SRTF_Coop(data)
            elif alg in ["sp", "shortest preemptive", "srtfp"]:
                graph.setTitle("Shortest Remaining Time First Preemptive")
                ganttData = SRTF_Prem(data)
            else:
                print("Invalid algorithm choice.")
                continue

            # Print and draw the Gantt chart
            print("Generating Gantt Graph: ")
            # print(ganttData)
            graph.drawGraph(ganttData)
            print("\n\n")
            print("thank you for using our app")
            print("=" * 20)
            break  # Exit the loop

        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    methode = input("Do you want to use the GUI version? [y/n]: ").lower()
    if methode in ["n", "no"]:
        main()
    else:
        app = QApplication(sys.argv)
        window = AppGui()
        window.show()
        sys.exit(app.exec_())
