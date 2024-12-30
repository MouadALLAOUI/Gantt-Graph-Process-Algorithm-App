from random import randint
from classes import Processus


def generateTestData():
    testData = []
    for i in range(randint(2, 11)):
        testData.append(Processus(f"P{i}", randint(0, 5), randint(1, 5), randint(0, 5)))

    return testData
