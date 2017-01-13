"""
To load this example, in the directory containing this script, run

    bokeh serve --show bokehscatter.py

Your browser will open up at the appropriate address:

    http://localhost:5006/bokehscatter
"""

import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models import Select, ColumnDataSource
from bokeh.layouts import row, widgetbox
from bokeh.palettes import brewer

print('loading data...')
df_samp = pd.read_csv('covtype_preprocess.sampled.csv', index_col=0)
df_samp.sort_values(by='Cover_Type', ascending=True, inplace=True)
df_samp = df_samp.rename(columns={'Hillshade_9am': 'Hillshade_9Am',
                                  'Hillshade_3pm': 'Hillshade_3Am'})


print('preprocessing data...')
cover_types = sorted(np.unique(df_samp['Cover_Type'].values))
n_types = len(cover_types)
colors = brewer['Accent'][n_types]
src = ColumnDataSource(df_samp)
src.data['colors'] = df_samp['Cover_Type'].apply(lambda x: colors[x - 1])

TOOLS = "pan,wheel_zoom,box_zoom,undo,redo,reset,box_select,save"

quantcols = ['Elevation', 'Aspect', 'Slope',
             'Horizontal_Distance_To_Hydrology',
             'Vertical_Distance_To_Hydrology',
             'Horizontal_Distance_To_Roadways',
             'Hillshade_9Am',
             'Hillshade_Noon',
             'Hillshade_3Am',
             'Horizontal_Distance_To_Fire_Points',
             ]


def create_scatter1():
    x_title = x.value.title()
    y1_title = y1.value.title()
    print(x_title, y1_title)

    kw = dict()
    kw['title'] = "{0} vs {1}".format(x_title, y1_title)

    f1 = figure(plot_height=400, plot_width=400, tools=TOOLS, **kw)
    f1.scatter(x=x_title, y=y1_title, color='colors', source=src)
    f1.xaxis.axis_label = x_title
    f1.yaxis.axis_label = y1_title
    return f1


def create_scatter2():
    x_title = x.value.title()
    y2_title = y2.value.title()
    print(x_title, y2_title)

    kw = dict()
    kw['title'] = "{0} vs {1}".format(x_title, y2_title)

    f2 = figure(plot_height=400, plot_width=400, tools=TOOLS, **kw)
    f2.scatter(x=x_title, y=y2_title, color='colors', source=src)
    f2.xaxis.axis_label = x_title
    f2.yaxis.axis_label = y2_title
    return f2


def update(attr, old, new):
    update1(attr, old, new)
    update2(attr, old, new)


def update1(attr, old, new):
    layout.children[1] = create_scatter1()


def update2(attr, old, new):
    layout.children[2] = create_scatter2()


x = Select(title='X-Axis', value='Elevation', options=quantcols)
x.on_change('value', update)

y1 = Select(title='Y1-Axis', value='Horizontal_Distance_To_Hydrology',
            options=quantcols)
y1.on_change('value', update1)

y2 = Select(title='Y2-Axis', value='Aspect',
            options=quantcols)
y2.on_change('value', update2)

controls = widgetbox([x, y1, y2], width=300)
layout = row(controls, create_scatter1(), create_scatter2())

curdoc().add_root(layout)
curdoc().title = "Quantitative Variable Explorer"
