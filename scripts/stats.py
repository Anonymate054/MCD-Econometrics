
import pandas as pd

def generate_detailed_statistics(df):
    """
    Function to generate detailed summary statistics for all numeric columns in a DataFrame.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        
    Returns:
        pd.DataFrame: A DataFrame containing detailed summary statistics for each numeric column.
    """
    stats = []

    for col in df.columns:
        # Verificar si la columna es numérica
        if pd.api.types.is_numeric_dtype(df[col]):
            summary = {
                'Variable': col,
                'Count': df[col].count(),
                'Mean': df[col].mean(),
                'Median': df[col].median(),
                'Mode': df[col].mode()[0] if not df[col].mode().empty else None,
                'Min': df[col].min(),
                'Max': df[col].max(),
                'Range': df[col].max() - df[col].min(),
                'Q1 (25%)': df[col].quantile(0.25),
                'Q2 (50%)': df[col].quantile(0.5),  # Igual a la mediana
                'Q3 (75%)': df[col].quantile(0.75),
                'IQR': df[col].quantile(0.75) - df[col].quantile(0.25),  # Rango intercuartílico
                'Variance': df[col].var(),
                'Std Dev': df[col].std(),
                'Skewness': df[col].skew(),
                'Kurtosis': df[col].kurt(),
                'Coefficient of Variation': df[col].std() / df[col].mean() if df[col].mean() != 0 else None,
                'Percentile 10%': df[col].quantile(0.10),
                'Percentile 90%': df[col].quantile(0.90)
            }
            stats.append(summary)
    
    # Crear un DataFrame con todas las estadísticas
    stats_df = pd.DataFrame(stats)
    
    return stats_df
