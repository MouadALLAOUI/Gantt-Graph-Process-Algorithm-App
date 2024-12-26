class Processus:
    def __init__(self, name, entry, cpu, priority):
        self.name = name
        self.entry = entry
        self.cpu = cpu
        self.priority = priority
        self.rcpu = cpu

    @property
    def getProcess(self):
        return {
            "name": self.name,
            "EnterDate": self.entry,
            "CPUs": self.cpu,
            "priority": self.priority,
            "remainCPUs": self.rcpu,
        }

    def setEntry(self, entry=1):
        self.entry += entry

    def setRCPUs(self, rcpu):
        self.rcpu = rcpu

    def decreaseCPUs(self, step=1):
        self.rcpu -= step
