
# voyager-launch

This simple package provides a function `voyager` for launching a [Voyager](https://github.com/vega/voyager) interactive data visualization window in your browser. The argument to `voyager` should be a Pandas `DataFrame` or an Scikit-Learn `Bunch`. 

It also provides a function `tableview` for opening a DataFrame in your browser using [ag-Grid](https://www.ag-grid.com). With this tool, you can filter, sort, re-arrange rows, and export to CSV with a button click.

This package was inspired by the Julia packages [`DataVoyager.jl`](https://github.com/queryverse/DataVoyager.jl) and [`TableView.jl`](https://github.com/JuliaComputing/TableView.jl).

## Example

### Voyager

```python
from voyager import voyager
import pandas as pd
iris = pd.read_csv("http://bit.ly/iris-dataset")
voyager(iris)
```
![demo](https://raw.githubusercontent.com/sswatson/voyager-launch/master/images/voyager.png)

### Table View

```python
from voyager import tableview
tableview(iris)
```

![demo](https://raw.githubusercontent.com/sswatson/voyager-launch/master/images/tableview.png)

### Data frame heatmaps with hover text

```python
from voyager import imshow
imshow(iris)
```

![demo](https://raw.githubusercontent.com/sswatson/voyager-launch/master/images/imshow.png)

## Installation

`pip install voyager-launch`