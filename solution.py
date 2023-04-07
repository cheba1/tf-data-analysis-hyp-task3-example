import pandas as pd
import numpy as np
from scipy import stats


chat_id = 725861714 # Ваш chat ID, не меняйте название переменной

def solution(control: List[float], experiment: List[float]) -> bool:
    alpha = 0.05
    _, p_value = stats.ttest_ind(control, experiment, equal_var=False)
    return p_value < alpha
