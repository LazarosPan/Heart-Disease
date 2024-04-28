import pandas as pd
import numpy as np

def df_info(dataframes, dataframe_names):
    """
    Finds useful information about all dataframes given in the function.

    Usage: pass a list of dataframes and their names into the function
    
    Parameters:
        dataframes = [df1, df2, ...]
        dataframe_names = ["df1", "df2", ...]

    Output: print's information about schema, missing values, duplicate values and value counts for target column.
    """

    for df, df_name in zip(dataframes, dataframe_names):
        # Check if the dataframe has at least one column
        if not df.empty:
            print("----- information for ", df_name, " -----")
            print(df_name, " : ", df.shape, "(rows, columns)")
            print(df_name, " : ", df.isna().sum().sum(), "missing values")
            print(df_name, " : ", df.duplicated().sum(), "duplicate values")

            # Identify and count values of the last column
            last_column = df.columns[-1]
            value_counts = df[last_column].value_counts()

            print(df_name, " : Value counts for ", last_column)
            print(value_counts)
        else:
            print(df_name, ': The dataframe is empty.')




def df_clean(df):
  """
  Eliminate invalid data from the dataframe.

  This function replaces non-numeric values, in all the columns of the dataframe,
  with NaN and then removes rows containing these NaN values.

  Parameters:
    df: pandas DataFrame

  Returns:
    Cleaned DataFrame
  """
  df_columns = df.columns.to_list()

  # https://stackoverflow.com/questions/21771133/finding-non-numeric-rows-in-dataframe-in-pandas
    
  num_df = (
      df.drop(df_columns, axis=1)
        .join(df[df_columns].apply(pd.to_numeric, errors='coerce'))
  )

  num_df = num_df[num_df[df_columns].notnull().all(axis=1)]

  return num_df




def show_value_counts(df):
    for col in df.columns:
        print(f"Data Type: {df[col].dtype}")
        print(df[col].value_counts())
        print("\n")


### needs improvement to handle all of the data types available in pandas
def fill_missing_values(df, label_column):
    cat_columns = ['object', 'category', 'string']
    filled_values = df.drop(label_column, axis=1).apply(lambda x: x.mode().iloc[0] if x.dtype.name in cat_columns else x.mean())
    
    fill_dict = {}
    for col in df.columns:
        if col != label_column:
            if df[col].dtype.name in cat_columns:
                fill_values = df.groupby(label_column)[col].apply(lambda x: x.mode().iloc[0])
                df[col].fillna(df[label_column].map(fill_values), inplace=True)
                fill_dict[col] = fill_values.to_dict()
            else:
                fill_values = df.groupby(label_column)[col].mean()
                df[col].fillna(df[label_column].map(fill_values), inplace=True)
                fill_dict[col] = fill_values.to_dict()
    
    print("Filled values:")
    for col, fill_value in fill_dict.items():
        print(f"Column: {col}")
        print(f"Values filled: {fill_value}")
        print()
    
    return df


# def fill_missing_values(df, label_column):
#     cat_columns = ['object', 'category', 'string']
#     filled_values = df.drop(label_column, axis=1).apply(lambda x: x.mode().iloc[0] if x.dtype.name in cat_columns else x.mean())
    
#     for col in df.columns:
#         if col != label_column:
#             if df[col].dtype.name in cat_columns:
#                 fill_values = df.groupby(label_column)[col].apply(lambda x: x.mode().iloc[0])
#                 df[col].fillna(df[label_column].map(fill_values), inplace=True)
#             else:
#                 fill_values = df.groupby(label_column)[col].mean()
#                 df[col].fillna(df[label_column].map(fill_values), inplace=True)
    
#     return df