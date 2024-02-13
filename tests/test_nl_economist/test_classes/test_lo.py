import pytest

from nl_economist.classes.accounts import Accounts
from nl_economist.classes.lo import LO


@pytest.mark.parametrize(
    "pv, expected",
    [
        (10, Accounts(0, 0)),
        (70, Accounts(1225, 0)),
        (140, Accounts(2450, 0)),
        (200, Accounts(4270, 3640)),
        (300, Accounts(4270, 6440)),
        (400, Accounts(7315, 9240)),
        (500, Accounts(8820, 12040)),
        (600, Accounts(10360, 14840)),
        (700, Accounts(11865, 17640)),
        (800, Accounts(13405, 20440)),
        (900, Accounts(14910, 23240)),
        (1000, Accounts(16450, 26040)),
    ],
)
def test__lo__calculate(pv: float, expected: Accounts) -> None:
    assert LO(pv).calculate() == expected


@pytest.mark.parametrize(
    "pv, expected",
    [
        (70, 35),
        (200, 122),
        (300, 122),
        (400, 209),
        (500, 252),
        (600, 296),
        (700, 339),
        (800, 383),
        (900, 426),
        (1000, 470),
    ],
)
def test__lo__get_count_bonus_ue(pv: float, expected: float) -> None:
    assert LO(pv)._LO__get_count_bonus_ue() == expected  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "pv, expected",
    [
        (70, 0),
        (200, 87),
        (300, 87),
        (400, 174),
        (500, 174),
        (600, 261),
        (700, 261),
        (800, 348),
        (900, 348),
        (1000, 435),
    ],
)
def test__lo__get_recommended_lo_bonus(pv: float, expected: float) -> None:
    assert LO(pv)._LO__get_recommended_lo_bonus(pv) == expected  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "pv, expected",
    [
        (70, 0),
        (200, 87),
        (300, 87),
        (400, 174),
        (500, 217),
        (600, 217),
        (700, 304),
        (800, 304),
        (900, 391),
        (1000, 434),
    ],
)
def test__lo__get_increased_lo_bonus(pv: float, expected: float) -> None:
    assert LO(pv)._LO__get_increased_lo_bonus(pv) == expected  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    "pv, expected",
    [
        (10, Accounts(0, 0)),
        (70, Accounts(0, 0)),
        (140, Accounts(1225, 0)),
        (200, Accounts(0, 3640)),
        (300, Accounts(0, 6440)),
        (400, Accounts(0, 9240)),
        (500, Accounts(0, 12040)),
        (600, Accounts(0, 14840)),
        (700, Accounts(0, 17640)),
        (800, Accounts(0, 20440)),
        (900, Accounts(0, 23240)),
        (1000, Accounts(0, 26040)),
    ],
)
def test__lo__get_reward(pv: float, expected: Accounts) -> None:
    assert LO(pv)._LO__get_reward() == expected  # type: ignore[attr-defined]
