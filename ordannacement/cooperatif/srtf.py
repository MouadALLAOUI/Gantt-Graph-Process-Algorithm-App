def SRTF_Coop(data):
    waitingList = []  # ? List of ready-to-run processes
    inRun = None  # ? express the process in exucution
    ganttData = []
    current_time = 0  # Track the current time unit

    # ? here we add the remaining (rest) CPUs for each process
    for proc in data:
        proc.setRCPUs(proc.cpu)

    # todo: get the the sum of cpus for all processus we have
    iterNum = sum(proc.cpu for proc in data)

    # ? sort the data by entry priority and cpu
    data.sort(key=lambda p: (p.rcpu, -p.priority))

    #! loop until all processes are completed
    while current_time < iterNum:
        # todo: loop to manage the wainting list and processus according to thier entry time
        for proc in data:
            if proc.entry == current_time and proc not in [p for p in waitingList]:
                # ? Use a list [process, quantum iteration] to track the quantum time
                waitingList.append(proc)

        waitingList.sort(key=lambda p: (p.priority, p.rcpu))
        if not inRun and waitingList:
            inRun = waitingList.pop(0)

        # ! If there's a process running, continue its execution
        if inRun:
            inRun.decreaseCPUs(1)  # ? Decrease remaining CPUs by 1
            ganttData.append(
                {
                    "name": inRun.name,
                    "startTime": current_time,
                    "CPUs": 1,  # Each iteration runs for 1 unit
                }
            )

            #! If the process finishes or its quantum expires, move it back to the list
            if inRun.rcpu == 0:
                inRun = None  # Process finished

        # Increment time
        current_time += 1

    # ? re-sort ganttData
    dataToDraw = []
    for data in ganttData:
        # ! dataTotreat[-1] last element in the list
        if dataToDraw and dataToDraw[-1]["name"] == data["name"]:
            # Extend the current block
            dataToDraw[-1]["CPUs"] += data["CPUs"]
        else:
            # Start a new block
            dataToDraw.append(data)

    return dataToDraw
