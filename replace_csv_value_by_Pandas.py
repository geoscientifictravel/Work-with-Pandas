import pandas as pd

df2 = pd.read_csv('currency1.csv', index_col=None)


def KYRGYZ_SOM(df2):
    """Return changed value for 'Kyrgyz Soms' into 'KYRGYZ SOM'"""
    df2['Name'] = df2['Name'].str.strip()  # Clear fields in .csv file
    df2 = df2.replace('Kyrgyz Soms', 'KYRGYZ SOM')  # Replace value
    return df2.to_excel("file1.xlsx", index=False, header=True)  # Save result as excel file


KYRGYZ_SOM(df2)
