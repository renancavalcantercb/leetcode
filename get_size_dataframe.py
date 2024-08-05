import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    column, row = players.shape
    return [column, row]
