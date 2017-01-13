import pandas as pd
import numpy as np
from bokeh.plotting import figure, curdoc
# from palettable.colorbrewer.qualitative import Accent_8
from bokeh.models import Select, ColumnDataSource
from bokeh.layouts import row, widgetbox
# from bokeh.charts import Scatter

df = pd.read_csv('covtype_preprocess.csv', index_col=0)
df.sort_values(by='Cover_Type', ascending=True, inplace=True)
df = df.rename(columns={'Hillshade_9am': 'Hillshade_9Am',
                        'Hillshade_3pm': 'Hillshade_3Am'})
df_samp = df.sample(frac=0.001)

cover_types = sorted(np.unique(df['Cover_Type'].values))
n_types = len(cover_types)
# colors = Accent_8.mpl_colormap
colors = ['DarkSeaGreen', 'Firebrick', 'Gold', 'Indigo', 'LightCoral',
          'LimeGreen', 'MistyRose']
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

    f1 = figure(plot_height=500, plot_width=500, tools=TOOLS)
    f1.scatter(x=x_title, y=y1_title, color='colors', source=src)

    return f1


def create_scatter2():
    x_title = x.value.title()
    y2_title = y2.value.title()
    print(x_title, y2_title)

    kw = dict()
    kw['title'] = "{0} vs {1}".format(x_title, y2_title)

    f2 = figure(plot_height=500, plot_width=500, tools=TOOLS)
    f2.scatter(x=x_title, y=y2_title, color='colors', source=src)
    return f2


def update(attr, old, new):
    # This doesn't work...
    # layout.children[1] = create_scatter1()
    # print(layout.children[1])
    # layout.children[2] = create_scatter2()

    # And this doesn't work either...
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

# controls = widgetbox([y1, y2])
controls = widgetbox([x, y1, y2], width=300)
# controls = widgetbox([x, y1], width=300)
layout = row(controls, create_scatter1(), create_scatter2())
# layout = row(controls, create_scatter1())

curdoc().add_root(layout)
curdoc().title = "Quantitative Variable Explorer"
