
import json
import shutil
import os
import tempfile
import webbrowser
from copy import deepcopy
import random
import string

import pandas as pd
import numpy as np

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
    tmpdir = new_html_temp("html")
    with open(os.path.join(tmpdir,'html/data.js'), 'w') as file:
        file.write(f"""voyagerInstance.updateData({{"values\":{df2.to_json(orient='records')}}})""")
    return html_open(tmpdir,'html/main.html')

def new_html_temp(src):
    """
    Create a tmp directory, copy `src` into it, and return the tmp directory
    """
    tmpdir = tempfile.mkdtemp()
    parentdir = os.path.dirname(__file__)
    shutil.copytree(os.path.join(parentdir,src), os.path.join(tmpdir,src))
    return tmpdir
   
def html_open(tmpdir,file):
    """
    Try to open an html file in the OS default web browser. If that fails, 
    provide a link to open it in Jupyter.
    """
    opened = webbrowser.open_new_tab('file://' + os.path.join(tmpdir,file))
    if not opened:
        from IPython.display import FileLink
        localdir = 'tmp-voyager-' + ''.join(random.choice(string.ascii_letters) for _ in range(6))
        shutil.copytree(tmpdir,localdir)
        return FileLink(os.path.join(localdir,file))
        

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
    
def in_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:
            return False
    except ImportError:
        return False
    return True

def clean():
    for file in os.listdir():
        if file.startswith("tmp-voyager-"):
            shutil.rmtree(file)

def tableview(df):
    df2 = deepcopy(df)
    sanitize_colnames(df2)
    df2.insert(0,"idx",df2.index)
    def coldef(i,colName,colType):
        colSpec = {"headerName": colName, 
                   "field": colName}
        if np.issubdtype(colType, np.number):
            colSpec["type"] = "numericColumn"
            colSpec["filter"] = "agNumberColumnFilter"
        if i == 0:
            colSpec["pinned"] = "left"
            colSpec["rowDrag"] = True
        return colSpec
    tmpdir = new_html_temp("ag-grid")
    with open(os.path.join(tmpdir,'ag-grid/data.js'), 'w') as file:
        file.write("var columnDefs = " + json.dumps([coldef(i,colName,colType) for (i, (colName, colType)) in enumerate(zip(df2.columns,df2.dtypes))]) + ";\n\n")
        file.write(f"var rowData = {df2.to_json(orient='records')};")
    return html_open(tmpdir,'ag-grid/index.html')


