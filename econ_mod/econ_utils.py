import pandas as pd
import numpy as np

def create_cop_df(df: pd.DataFrame, x: str, y: str) -> pd.DataFrame:
    """
    Creates a DataFrame with columns needed to calculate the covariance and variance components 
    for linear regression. Specifically, it adds columns for the means of x and y, 
    the deviations from these means, and the products of these deviations.

    Parameters:
    - df: pd.DataFrame - The input DataFrame containing the data.
    - x: str - The name of the independent variable (predictor).
    - y: str - The name of the dependent variable (response).

    Returns:
    - pd.DataFrame: A copy of the original DataFrame with additional columns for 
      x and y means, deviations, and covariance components.
    """
    df_cop = df.copy()
    df_cop['x_bar'] = df_cop[x].mean()
    df_cop['y_bar'] = df_cop[y].mean()

    df_cop['x-x_bar'] = df_cop[x] - df_cop['x_bar']
    df_cop['y-y_bar'] = df_cop[y] - df_cop['y_bar']

    df_cop['num_b1'] = df_cop['x-x_bar'] * df_cop['y-y_bar']
    df_cop['den_b1'] = df_cop['x-x_bar'] ** 2
    
    return df_cop

def get_lr_metrics(df_cop: pd.DataFrame, x: str, y: str) -> float:
    """
    Calculates the slope (b1) and intercept (b0) of the linear regression line 
    using the prepared DataFrame from `create_cop_df`.

    Parameters:
    - df_cop: pd.DataFrame - The DataFrame with covariance and variance components.
    - x: str - The name of the independent variable (predictor).
    - y: str - The name of the dependent variable (response).

    Returns:
    - tuple: A tuple containing the slope (b1) and intercept (b0).
    """
    b1 = df_cop['num_b1'].sum() / df_cop['den_b1'].sum()
    b0 = df_cop[y].mean() - b1 * df_cop[x].mean()
    
    return b1, b0

def y_hat(x: int | float, slope: float, intercept: float) -> float:
    """
    Predicts the value of y given x using the linear regression equation.

    Parameters:
    - x: int | float - The value of the independent variable.
    - slope: float - The slope (b1) of the regression line.
    - intercept: float - The intercept (b0) of the regression line.

    Returns:
    - float: The predicted value of y.
    """
    return slope * x + intercept

def create_res_df(df: pd.DataFrame, slope: float, intercept: float, x: str, y: str) -> pd.DataFrame:
    """
    Creates a DataFrame with additional columns for the predicted values of y, 
    the residuals, and the deviations of the actual y values from their mean.

    Parameters:
    - df: pd.DataFrame - The input DataFrame containing the data.
    - slope: float - The slope (b1) of the regression line.
    - intercept: float - The intercept (b0) of the regression line.
    - x: str - The name of the independent variable (predictor).
    - y: str - The name of the dependent variable (response).

    Returns:
    - pd.DataFrame: A copy of the original DataFrame with additional columns for 
      predicted y values, residuals, and deviations from the mean.
    """
    df_res = df.copy()
    df_res['y_hat'] = df_res.apply(lambda row: y_hat(row[x], slope=slope, intercept=intercept), axis=1)
    df_res['err_hat'] = df_res[y] - df_res['y_hat']
    df_res['err_bar'] = df_res[y] - df_res[y].mean()
    
    return df_res