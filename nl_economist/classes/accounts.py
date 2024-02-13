import dataclasses


@dataclasses.dataclass
class Accounts:
    unit: float
    reward: float

    def __repr__(self) -> str:
        return f"Accounts(unit: {self.unit}, reward: {self.reward})"
