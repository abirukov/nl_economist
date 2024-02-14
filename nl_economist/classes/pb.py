import dataclasses

from nl_economist.constants import ACTIVATION_LO, UE_CURRENCY

PB_COEFFICIENT = 0.4  # Коэффициент партнерского бонуса


@dataclasses.dataclass
class PB:
    """
    Партнерский бонус

    Attributes
    ----------
    count_partners_activated: int
        количество 70ков
    count_partners_recommended_lo: int
        количество 200ков(отдельно от 70ков)
    not_active_partners_pv_sum: float = 0.0
        Сумма PV от партнеров у которых менее 70 pv
    ----------
    """

    count_partners_activated: int
    count_partners_recommended_lo: int
    not_active_partners_pv_sum: float = 0.0

    def calculate(self) -> float:
        base_pb = self.__get_base_pb()
        premium_pb = self.__get_premium_pb(
            self.count_partners_activated + self.count_partners_recommended_lo,
        )
        increased_premium_pb = self.__get_premium_pb(self.count_partners_recommended_lo)
        return (base_pb + premium_pb + increased_premium_pb) * UE_CURRENCY

    def __get_base_pb(self) -> float:
        return (
            (self.count_partners_activated + self.count_partners_recommended_lo)
            * ACTIVATION_LO
            + self.not_active_partners_pv_sum
        ) * PB_COEFFICIENT

    @staticmethod
    def __get_premium_pb(count_partners: int) -> int:
        if count_partners < 5:
            return 0
        if 5 <= count_partners < 7:
            return 100
        if 7 <= count_partners < 9:
            return 200
        if 9 <= count_partners < 12:
            return 300
        if 12 <= count_partners < 15:
            return 400
        return 500
