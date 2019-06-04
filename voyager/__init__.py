
import json
import shutil
import os
import tempfile
import webbrowser
from copy import deepcopy
import pandas as pd

def voyager(df):
    """
    Launch a browser window with a Voyager exploration of the data in 
    the given pandas DataFrame or sklearn Bunch. 
    """
    if not isinstance(df, pd.DataFrame):
        df2 = bunch_to_df(df)
    else:
        df2 = deepcopy(df)
    sanitize_colnames(df2)
    dir = tempfile.mkdtemp()
    parentdir = os.path.dirname(__file__)
    shutil.copytree(os.path.join(parentdir,"html"), os.path.join(dir,"html"))
    with open(os.path.join(dir,'html/data.js'), 'w') as file:
        file.write(f"""voyagerInstance.updateData({{"values\":{df2.to_json(orient='records')}}})""")
    webbrowser.open_new_tab('file://' + os.path.join(dir,'html/main.html'))

def sanitize_colnames(df):
    """
    Remove dots from DataFrame column names
    """
    df.columns = df.columns.str.replace('.','_')

def bunch_to_df(bunch):
    df = pd.DataFrame(bunch.data,
                      columns=bunch.feature_names)
    df['target'] = pd.Series(bunch.target)
    return df