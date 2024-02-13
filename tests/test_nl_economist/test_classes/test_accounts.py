from nl_economist.classes.accounts import Accounts


def test__accounts__repr() -> None:
    assert Accounts(200, 4000).__repr__() == "Accounts(unit: 200, reward: 4000)"
