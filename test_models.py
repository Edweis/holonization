"""Test models."""
import pandas as pd
# import numpy as np

from .models import Evolution, Situation, State, Deposit

class TestModels:

    def test_shallow(self):
        """Test shallow models."""
        Evolution('Hey you')
        df = pd.DataFrame()
        Situation(df, [])
        State('v', 1, 2)
        deposit_series = pd.Series([])
        Deposit(deposit_series, [])

    def test_simple(self):
        """Test simple case."""
        df = pd.DataFrame(data=[[0,1], [2,3]])
        stake_holders = ['a', 'b']
        situation = Situation(df, stake_holders)
        state_b = situation.get_state('b')
        assert state_b.module == 6.4031242374328485

def test_case():
    """Test what i want to have."""
    pass
