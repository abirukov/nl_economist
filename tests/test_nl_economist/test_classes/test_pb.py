import pytest

from nl_economist.classes.pb import PB


@pytest.mark.parametrize(
    "count_partners_activated, count_partners_recommended_lo, not_active_partners_pv_sum, expected",
    [
        (0, 0, 0, 0),
        (3, 0, 78, 4032),
        (5, 0, 0, 8400),
        (7, 0, 0, 13860),
        (9, 0, 0, 19320),
        (12, 0, 0, 25760),
        (15, 0, 0, 32200),
        (7, 2, 0, 19320),
        (15, 5, 0, 40600),
    ],
)
def test__pb__calculate(
    count_partners_activated: int,
    count_partners_recommended_lo: int,
    not_active_partners_pv_sum: float,
    expected: float,
) -> None:
    assert (
        PB(
            count_partners_activated,
            count_partners_recommended_lo,
            not_active_partners_pv_sum,
        ).calculate()
        == expected
    )


@pytest.mark.parametrize(
    "count_partners_activated, count_partners_recommended_lo, expected",
    [
        (0, 0, 0),
        (5, 0, 140),
        (15, 0, 420),
        (15, 5, 560),
    ],
)
def test__pb__get_base_pb(
    count_partners_activated: int,
    count_partners_recommended_lo: int,
    expected: float,
) -> None:
    assert (
        PB(  # type: ignore[attr-defined]
            count_partners_activated,
            count_partners_recommended_lo,
        )._PB__get_base_pb()
        == expected
    )


@pytest.mark.parametrize(
    "count_partners, expected",
    [
        (3, 0),
        (5, 100),
        (7, 200),
        (9, 300),
        (12, 400),
        (17, 500),
    ],
)
def test__pb__get_premium_pb(
    count_partners: int,
    expected: int,
) -> None:
    assert PB._PB__get_premium_pb(count_partners) == expected  # type: ignore[attr-defined]
