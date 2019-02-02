import pandas as pd
import numpy as np
from typing import List

class Evolution:
    """Evolution of a holon situation accross time."""

    def __init__(self, title):
        self.title = title
        self.situations = []
        self.stake_holders = []

    def append(self, situation: 'Situation', deposit: 'Deposit'):
        """Append a situation."""
        print(self.__dict__)
        if not self.stake_holders:
            print(situation.stake_holders)
            print(self.stake_holders)
            assert situation.stake_holders == self.stake_holders,\
                'Stake holders don\'t match the previous ones.'
            self.stake_holders = situation.stake_holders
        assert deposit.shape[0] == len(self.stake_holders)
        self.situations.append(situation)
        self.deposits.append(situation)

    def __repr__(self):
        return f'<Evolution "{self.title}" length: {len(self.situations)}>'


class Situation:
    """Situation of a holon with all sub-holons transactions."""

    def __init__(self, df, stake_holders: List[str]):
        assert df.shape[0] == df.shape[1]
        assert len(stake_holders) == df.shape[0]
        self.stake_holders = stake_holders
        self.df = df
        self.df.index = stake_holders
        self.df.columns = stake_holders

    def get_state(self, stake_holder: str) -> 'State':
        """Get the state of stake_holder."""
        outcome = self.df.loc[stake_holder, :].sum()
        income = self.df.loc[:, stake_holder].sum()
        return State(stake_holder, income, outcome)

    def __repr__(self):
        return f'<Situation {self.df.shape}>'


class State:
    """State of a holon as a point."""

    def __init__(self, stake_holder: List[str], income: int, outcome: int):
        self.stake_holder = stake_holder
        self.income = income
        self.outcome = outcome
        self.module = np.sqrt(income**2 + outcome**2)

    def __repr__(self):
        return f'<State ({self.outcome}, {self.income}), mod={self.module}>'


class Deposit:
    """Represent a deposit from the holons."""

    def __init__(self, deposit_serie, stake_holders):
        pass
