class OffshoreElement():
    def __init__(self, entity, jurisdiction, linkedTo, dataFrom) -> None:
        self.entity = entity
        self.jurisdiction = jurisdiction
        self.linkedTo = linkedTo
        self.dataFrom = dataFrom
    
    def __repr__(self):
        return (f"OffshoreElement(entity={self.entity}, "
                f"jurisdiction={self.jurisdiction}, "
                f"linkedTo={self.linkedTo}, "
                f"dataFrom={self.dataFrom})")
    