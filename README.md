
# voyager-launch

This simple package provides a function `voyager` for launching a [Voyager](https://github.com/vega/voyager) window in your browser, for interactive data exploration. The argument to `voyager` should be a Pandas `DataFrame` or an Scikit-Learn `Bunch`. 

## Example

```python
from voyager import voyager
import pandas as pd
voyager(pd.read_csv("http://bit.ly/iris-dataset"))
```

## Installation

`pip install git+https://github.com/sswatson/voyager-launch`