class OfacElement():
    def __init__(self, name, address, type, program, list, score) -> None:
        self.name = name
        self.address = address
        self.type = type
        self.program = program
        self.list = list
        self.score = score
    
    def __repr__(self):
        return (f"OfacElement(name={self.name}, address={self.address}, "
                f"type={self.type}, program={self.program}, "
                f"list={self.list}, score={self.score})")