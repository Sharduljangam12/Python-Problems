#Write a Python class Counter with methods inc() and value() where inc() increases count by 1. (Paste code or explain.)
class Counter:
    def __init__(self):
        self.count = 0      # internal state

    def inc(self):
        self.count += 1     # update internal state

    def value(self):
        return self.count

