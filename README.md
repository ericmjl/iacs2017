# IACS Contest

My contest entries are present in the `analysis.ipynb` notebook.

## Running the interactive plots

You'll need to clone this repository locally, and have `bokeh`, `pandas` and `numpy` installed. After that, run:

```bash
$ bokeh serve --show bokehscatter.py --port 5001
```

or

```bash
$ bokeh serve --show bokehselect.py --port 5002
```



## Before Running Notebook...
Prior to running the notebook, the data file (`covtype_preprocess.csv.zip`) has to be unzipped first.


## Contest Entry
My contest entry has two figures, one interactive and one static, and they can be found under the **"Contest Entry"** header (a `Ctrl-F` or `Cmd-F` should do). Alternatively, simply scroll to the end of the notebook.

The interactive figure requires that the entire notebook be run from scratch. This takes roughly 1-2 minutes in total. The static figure is also present in the directory under the name `overview_plot.pdf`. Figure captions are inside the notebook.
