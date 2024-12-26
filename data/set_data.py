import csv
from datetime import datetime
from classes.processus import Processus


def set_data():
    processusList = []
    save_to_local = False

    print("Please allow us to take some of your time to fill in the data.")
    print("!!! For now, all the inputs should be integers.\n")
    while True:
        """
        The try/except here is to ensure our friend types an integer.
        """
        try:
            processusNum = int(
                input("How many processes are you willing to work with?: ")
            )
        except ValueError:  # Catch specific exceptions for clarity
            print("!!! Not to be rude, but you need to provide us with an integer.")
            continue  # ? Get back to the beginning

        try:
            isPriority = input("does your process have priority [yes/no]?: ").lower()
            if isPriority in ["yes", "y", "true", "1"]:
                isPriority = True
            if isPriority in ["no", "n", "false", "0"]:
                isPriority = False
        except ValueError:  # Catch specific exceptions for clarity
            print("!!! Not to be rude, but you need to provide us with an integer.")
            continue  # ? Get back to the beginning

        # * Now we're going to loop to create our process data.
        for i in range(processusNum):
            inputsValidation = True
            print("_" * 12)
            print(
                f"We're now setting up Process P{i}."
            )  # ? Used as a title for our process for good tracking
            print("_" * 12)

            while inputsValidation:
                try:
                    # ? Get the moment our process starts running.
                    processusEnterDate = int(
                        input(
                            f"What time does Process {i} start? `Please enter an integer`: "
                        )
                    )
                    # ? Get how many units our process keeps running.
                    processusCPUs = int(
                        input(f"How many CPU cycles does Process {i} take? ")
                    )
                    if isPriority:
                        # ? Get the priority of our process.
                        processusPriority = int(
                            input(f"What is the priority of this Process {i}? ")
                        )
                    else:
                        processusPriority = 0

                    inputsValidation = False
                except ValueError:  # Catch specific exceptions for clarity
                    print("!!! For now, all the inputs should be integers.")
                    continue  # ? Get back to the beginning

                processus = Processus(
                    f"P{i}",
                    processusEnterDate,
                    processusCPUs,
                    processusPriority,
                )

                # ? Add the processus to our processus list.
                processusList.append(processus)

        print("-" * 12)
        print("Data Entry Complete.")  # ? Just some decoration
        # + Just some decoration
        print("Process Table\n")
        print("-" * 40)
        print(f"| {'Name':^8}|{'Entry':^8}|{'CPUs':^8}|{'Priority':^8} |")
        print("-" * 40)
        for process in processusList:
            print(
                f"| {process.name:^8}|{process.entry:^8}|{process.cpu:^8}|{process.priority:^8} |"
            )
            print("-" * 40)
        # + Decoration end
        break

    while True:
        try:
            save_to_local = input(
                "Do you want to save this data to your local machine? y(yes)/n(no): "
            ).lower()
            if save_to_local in ["y", "yes", "true", "1"]:
                filename = f"{datetime.today().strftime('%Y_%m_%d_%H_%M_%S')}.csv"
                with open(filename, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    # Write header row
                    writer.writerow(["Name", "Entry", "CPUs", "Priority"])
                    # Write process data
                    for process in processusList:
                        writer.writerow(
                            [process.name, process.entry, process.cpu, process.priority]
                        )
                print(f"Data successfully saved to {filename}.")
            else:
                print("Data not saved locally.")
                break
        except Exception as e:  # Catch generic exceptions for feedback
            print(f"An error occurred while saving data: {e}")
            continue  # ? Get back to the beginning
        break

    # Sort the process list by priority and entry time.
    processusList.sort(key=lambda p: (p.priority, p.entry))
    return processusList
