import dataclasses

from nl_economist.classes.accounts import Accounts
from nl_economist.constants import (
    ACTIVATION_LO,
    BASE_COEFFICIENT,
    INCREASED_COEFFICIENT,
    INCREASED_LO,
    RECOMMENDED_LO,
    UE_CURRENCY,
)

ACTIVATION_LO_BONUS = 35.0
RECOMMENDED_LO_BONUS = 87.0
INCREASED_LO_BONUS = 217.0


@dataclasses.dataclass
class LO:
    """Личный объём"""

    pv: float

    def calculate(self) -> Accounts:
        if self.pv < ACTIVATION_LO:
            return Accounts(0, 0)
        bonus = self.__get_count_bonus_ue() * UE_CURRENCY
        reward_accounts = self.__get_reward()
        return Accounts(
            unit=bonus + reward_accounts.unit,
            reward=reward_accounts.reward,
        )

    def __get_count_bonus_ue(self) -> float:
        bonus_ue = ACTIVATION_LO_BONUS
        recommended_lo_bonus_ue = self.__get_recommended_lo_bonus(self.pv)
        increased_lo_bonus_ue = self.__get_increased_lo_bonus(self.pv)
        if recommended_lo_bonus_ue > increased_lo_bonus_ue:
            bonus_ue += recommended_lo_bonus_ue
        else:
            bonus_ue += increased_lo_bonus_ue
        return bonus_ue

    @staticmethod
    def __get_recommended_lo_bonus(pv: float) -> float:
        return pv // RECOMMENDED_LO * RECOMMENDED_LO_BONUS

    def __get_increased_lo_bonus(self, pv: float) -> float:
        increased_lo_counts = pv // INCREASED_LO
        increased_lo_bonus = increased_lo_counts * INCREASED_LO_BONUS
        increased_lo_bonus += self.__get_recommended_lo_bonus(
            pv - increased_lo_counts * INCREASED_LO,
        )
        return increased_lo_bonus

    def __get_reward(self) -> Accounts:
        if self.pv < ACTIVATION_LO:
            return Accounts(0, 0)

        if ACTIVATION_LO <= self.pv < RECOMMENDED_LO:
            unit_reward = (self.pv - ACTIVATION_LO) * BASE_COEFFICIENT * UE_CURRENCY
            return Accounts(unit_reward, 0)

        reward = (self.pv - ACTIVATION_LO) * INCREASED_COEFFICIENT * UE_CURRENCY
        return Accounts(0, reward)
