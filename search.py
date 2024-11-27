import re

class Search:
    def __init__(self, filename="note.txt"):
        self.filename = filename

        try:
            with open(self.filename, 'r') as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            raise Exception(f"File '{self.filename}' is not found.")

    def clean(self):
        pattern = r'[^\w\s]'
        self.lines = [re.sub(pattern, '', line) for line in self.lines]



    def get_lines(self, word):
        res=[word]
        for line_number, line in enumerate(self.lines, start=1):
            if word in line:
                res.append((line_number,line.strip()))
        if len(res)==1:
            raise ValueError(f"The Word '{word}' is not is not in file")
        return res





