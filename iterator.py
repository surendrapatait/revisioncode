


class LineItrator():



    def __init__(self,numof=5):
        with open ('sample') as file:
            self.allline = file.readlines()


    def __iter__(self):
        return self

    def __next__(self):




