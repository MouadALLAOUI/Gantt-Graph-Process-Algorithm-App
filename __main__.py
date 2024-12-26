from ordannacement.cooperatif.fifo import Fifo_Coop
from ordannacement.cooperatif.round_robin import Round_Robin_Coop
from ordannacement.premtif.fifo import Fifo_Prem
from ordannacement.premtif.round_robin import Round_Robin_Prem
from data.set_data import set_data
from classes.processus import Processus
from classes.graph import GanttGraph


dataTest = [
    Processus("P0", 0, 4, 0),
    Processus("P1", 1, 3, 0),
    Processus("P2", 2, 2, 0),
    Processus("P3", 3, 3, 0),
    Processus("P4", 4, 4, 0),
]


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
                data = set_data()
            elif isEntryData in ["r", "ready"]:
                print("Sorry, ready data is not available yet.")
                continue
            elif isEntryData in ["t", "test"]:
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
            else:
                print("Invalid algorithm choice. Please type 'fc' or 'fp'.")
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
    main()
    # ganttData = Round_Robin_Prem(dataTest)
    # GanttGraph().drawGraph(ganttData)
    # cpu_count = {proc.name: proc.cpu for proc in dataTest}
    # for entry in ganttData:
    #     cpu_count[entry["name"]] -= entry["CPUs"]

    # print("Remaining CPU times:", cpu_count)
