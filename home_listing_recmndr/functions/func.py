import numpy as np
import matplotlib.pyplot as plt
import missingno
import pandas as pd
from sklearn.impute import SimpleImputer


class cleanup_df():
    """
    Clean up Pandas DataFrame

    ...
    Attributes
    ----------
    dataframe: int, str, float
    dtypes: object, int64, float64

    Returns new dataframe called df1

    """

    def check_df(df):
        """Return an error if DataFrame is empty, continue on if not"""

        try:
            if df.empty == True:
                raise RuntimeError(
                    'DataFrame is empty or dataframe does not exist')
            if df.empty == False:
                pass
        except Exception as e:
            print('There is no DataFrame detected. Try again : {}'.format(e))

    def col_type(df):
        """Return column types"""

        col_by_dtype = df.columns.to_series().groupby(df.dtypes).groups
        col_by_dtype = {k.name: v for k, v, in col_by_dtype.items()}

        return col_by_dtype

    def missing_matrix(dtype, color):
        """Return plot showing missing data by column dtype"""

        missingno.matix(df.columns.object, color)
        plt.show()

    def clean_cat_feat(df):
        """Return clean categorical features. If any values are missing, return 'Unknown' string """

        cat_imputer = SimpleImputer(
            missing_values=np.nan, strategy="constant", fill_value="Unknown")
        df_cats = df[col_by_type['object']]
        df_cats.iloc[:, :] = cat_imputer.fit_transform(df_cats)

    def clean_cont_feat(df):
        """Return clean continuous feature. If any values are missing, return median value"""

        continuous_imputer = SimpleImputer(
            missing_values=np.nan, strategy="median")
        df_floats = df[col_by_dtype['float64']]
        df.floats.iloc[:, :] = continuous_imputer.fit_transform

    def cont_to_ord(df):
        """Transforms some continuous features to categorical"""

        rank = pd.Series(df).rank(pct=True)
        cut = pd.cut(rank, (0, .25, .50, .75, .9, 1), labels=[
                 'MIN', '25%', 'AVG', '75%', 'MAX'])
        return cut

    def dummies(df):
        """Get dummies for categorical encoding"""
        return pd.get_dummies(df, dummy_na=True)

    def clean_df(df):
        """Return clean and imputed df"""

        df_ints = df[col_by_dtype['int64']]
        df_floats = df[col_by_dtype['float64']]
        df_cats = df[col_by_type['object']]
        df1 = pd.concat([df_floats, df_ints, df_cats], axis=1)
        return df1
