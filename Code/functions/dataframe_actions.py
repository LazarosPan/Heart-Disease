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

def fill_missing_values(df_train, label_column, df_test=None, fill_categorical='mode', fill_numeric='mean'):
    """
    Fill missing values in a DataFrame.

    Parameters:
    - df_train (DataFrame): The training DataFrame.
    - label_column (str): The label column.
    - df_test (DataFrame, optional): The test DataFrame. Default is None.
    - fill_categorical (str, optional): Method to fill missing values in categorical columns.
        Options: 'mode' (default), 'most_frequent'.
    - fill_numeric (str, optional): Method to fill missing values in numeric columns.
        Options: 'mean' (default), 'median', 'most_frequent'.

    Returns:
    - df_train_filled (DataFrame): The training DataFrame with missing values filled.
    - df_test_filled (DataFrame): The test DataFrame with missing values filled.
    - filled_df (DataFrame): A DataFrame showing the filled values for each column.
    """
    cat_columns = ['object', 'category', 'string']
    
    fill_dict = {}
    
    for col in df_train.columns:
        if col != label_column:
            if df_train[col].dtype.name in cat_columns:
                if fill_categorical == 'mode':
                    fill_values = df_train.groupby(label_column)[col].apply(lambda x: x.mode().iloc[0])
                else:
                    fill_values = df_train.groupby(label_column)[col].apply(lambda x: x.value_counts().index[0])
                df_train[col].fillna(df_train[label_column].map(fill_values), inplace=True)
                fill_dict[col] = fill_values.to_dict()
                if df_test is not None:
                    df_test[col].fillna(df_test[label_column].map(fill_values), inplace=True)
            else:
                if fill_numeric == 'mean':
                    fill_values = df_train.groupby(label_column)[col].mean()
                elif fill_numeric == 'median':
                    fill_values = df_train.groupby(label_column)[col].median()
                else:
                    fill_values = df_train.groupby(label_column)[col].apply(lambda x: x.mode().iloc[0])
                df_train[col].fillna(df_train[label_column].map(fill_values), inplace=True)
                fill_dict[col] = fill_values.to_dict()
                if df_test is not None:
                    df_test[col].fillna(df_test[label_column].map(fill_values), inplace=True)
    
    filled_df = pd.DataFrame(fill_dict)
    
    return df_train, df_test, filled_df


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