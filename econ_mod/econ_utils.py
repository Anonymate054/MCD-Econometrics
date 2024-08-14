import pandas as pd
import numpy as np

def create_cop_df(df: pd.DataFrame, x: str, y: str) -> pd.DataFrame:
    """ """
    df_cop = df.copy()
    df_cop['x_bar'] = df_cop[x].mean()
    df_cop['y_bar'] = df_cop[y].mean()

    df_cop['x-x_bar'] = df_cop[x] - df_cop['x_bar']
    df_cop['y-y_bar'] = df_cop[y] - df_cop['y_bar']

    df_cop['num_b1'] = df_cop['x-x_bar'] * df_cop['y-y_bar']
    df_cop['den_b1'] = df_cop['x-x_bar'] ** 2
    return df_cop

def get_lr_metrics(df_cop: pd.DataFrame, x: str, y: str) -> float:
    """  """
    b1 = df_cop['num_b1'].sum() / df_cop['den_b1'].sum()
    b0 = df_cop[y].mean() - b1 * df_cop[x].mean()
    return b1, b0

def y_hat(x: int | float, slope : float, intercept: float): 
    """ """
    return slope * x + intercept

def create_res_df(df: pd.DataFrame, slope: float, intercept: float, x: str, y: str) -> pd.DataFrame:
    """ """
    df_res = df.copy()
    df_res['y_hat'] = df_res.apply(lambda row: y_hat(row[x], slope=slope, intercept=intercept), axis=1)
    df_res['err_hat'] = df_res[y] - df_res['y_hat']
    df_res['err_bar'] = df_res[y] - df_res[y].mean()
    return df_res