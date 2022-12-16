from time import perf_counter, perf_counter_ns


class Timer:


    def __init__(self, mass="The Time", typeTime='s'):

        self.start = perf_counter() if typeTime == 's' else perf_counter_ns()
        self.end = 0
        self.typeTime = typeTime
        self.mass = mass

    def __del__(self):
        self.end = perf_counter() if self.typeTime == 's' else perf_counter_ns()

        print(f"{self.mass} {round(self.end - self.start, 5)}")