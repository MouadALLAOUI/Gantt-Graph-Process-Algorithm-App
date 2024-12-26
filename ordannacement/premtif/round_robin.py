def Round_Robin_Prem(data, Quantum=2):
    waitingList = []  # ? List of ready-to-run processes
    inRun = None  # ? express the process in exucution
    gantt_data = []
    current_time = 0  # Track the current time unit

    # ? here we add the remaining (rest) CPUs for each process
    for proc in data:
        proc.setRCPUs(proc.cpu)

    # ? sort the data by entry time and priority
    data.sort(key=lambda p: (p.entry, -p.priority))

    #! loop until all processes are completed
    while True:
        # todo: loop to manage the wainting list and processus according to thier entry time
        for proc in data:
            if proc.entry == current_time and proc not in [p[0] for p in waitingList]:
                # ? Use a list [process, quantum iteration] to track the quantum time
                waitingList.append([proc, 0])

        # !  update the running if higher-priority process exists
        for act in waitingList:
            if inRun is None or act[0].priority < inRun[0].priority:
                # print(act)
                if inRun:
                    waitingList.append(inRun)
                inRun = [act[0], 0]
                waitingList.remove(act)
        waitingList.sort(key=lambda p: (-p[0].priority, p[0].entry))
        if inRun:
            inRun[1] += 1
            inRun[0].decreaseCPUs(1)

            gantt_data.append(
                {"name": inRun[0].name, "startTime": current_time, "CPUs": 1}
            )

            # Handle completion or quantum expiration
            if inRun[0].rcpu == 0:
                inRun = None
            elif inRun[1] == Quantum:
                waitingList.append([inRun[0], 0])
                inRun = None

        if not waitingList and inRun is None:
            break
        current_time += 1

    # ? re-sort ganttData
    dataToDraw = []
    for data in gantt_data:
        if dataToDraw and dataToDraw[-1]["name"] == data["name"]:
            dataToDraw[-1]["CPUs"] += data["CPUs"]
        else:
            dataToDraw.append(data)

    return dataToDraw
