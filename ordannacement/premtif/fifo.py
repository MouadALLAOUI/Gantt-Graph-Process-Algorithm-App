def Fifo_Prem(data):
    waitingList = []  # ? list were we put ready to run process
    inRun = None  # ? express the process in exucution
    ganttData = []
    # ? here we add the remaining (rest) CPUs for each process
    for proc in data:
        proc.setRCPUs(proc.cpu)

    # todo: get the the sum of cpus for all processus we have
    iterNum = sum(proc.cpu for proc in data)  # inline for loop

    #! loop to run the sorting
    for i in range(iterNum + 1):
        # todo: we will create a loop to manage the wainting list and add process according to thier entry
        for proc in data:
            if proc.entry == i and proc not in waitingList:
                waitingList.append(proc)
        # todo: sort the waitingList by priority then by entry time
        waitingList.sort(key=lambda p: (p.priority, p.entry))

        # !  update the running if higher-priority process exists
        if waitingList and (inRun is None or waitingList[0].priority < inRun.priority):
            inRun = waitingList[0]
            """_summary_
                we use 0 as index just because every iteration our waitingList will resort it self 
                # ! ==> waitingList.sort(key=lambda p: (p["Priority"], p["entry"]))
                so every eteration we will have the processus with higher-priority in the first index which is 0
            """

        # ? execute inRun for one unite
        if inRun:
            ganttData.append(
                {
                    "name": inRun.name,
                    "startTime": i,
                    "CPUs": 1,  # Each iteration runs for 1 unit
                }
            )
            inRun.decreaseCPUs(1)  # Decrement remaining CPUs
            if inRun.rcpu == 0:
                waitingList.remove(inRun)
                inRun = None  # Reset to pick the next process

    # ? re-sort ganttData
    dataToDraw = []
    for entry in ganttData:
        # ! dataTotreat[-1] last element in the list
        if dataToDraw and dataToDraw[-1]["name"] == entry["name"]:
            # Extend the current block
            dataToDraw[-1]["CPUs"] += entry["CPUs"]
        else:
            # Start a new block
            dataToDraw.append(
                {
                    "name": entry["name"],
                    "startTime": entry["startTime"],
                    "CPUs": entry["CPUs"],
                }
            )

    return dataToDraw
