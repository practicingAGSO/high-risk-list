class Response():
    def __init__(self, total, data) -> None:
        self.total = total
        self.data = data
    def __repr__(self):
        return f"Response(total={self.total}, data={self.data})"
    
    def to_dict(self):
        return {
            "total": self.total,
            "data": [element.__dict__ for element in self.data]  
        }