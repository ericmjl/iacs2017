from bokeh.models.widgets import CheckboxGroup, Button
from bokeh.layouts import row
from bokeh.plotting import figure, curdoc  # , output_file  #, show,
import pandas as pd

# Load data
df = pd.read_csv('nmi.csv', index_col=0)
print(df.columns)

# Define columns - convenience!
qual_cols = list(df['features'].values)


def make_bar():
    all_active = []
    all_active.extend(chkbx.active)
    all_active.extend(chkbx2.active)

    sel_data = df.iloc[all_active]
    p = figure(plot_width=600, plot_height=400)
    p.vbar(x=range(len(all_active)), width=0.4,
           top=sel_data['mutual_information'])
    return p


def update(attr, old, new):
    r1.children[2] = make_bar()


def clear():
    chkbx.active = [0]
    chkbx2.active = []


# Make interactive stuff.
brk = 27
chkbx = CheckboxGroup(labels=qual_cols[0:brk], active=[0])
chkbx.on_change('active', update)

chkbx2 = CheckboxGroup(labels=qual_cols[brk:], active=[])
chkbx2.on_change('active', update)

clr_button = Button(label='Clear Selections', button_type='success')
clr_button.on_click(clear)

# Layout document.
# controls = widgetbox([chkbx], [chkbx2])
r1 = row(chkbx, chkbx2, make_bar())
r2 = row(clr_button)

curdoc().add_root(r1)
curdoc().add_root(r2)
curdoc().title = "Quantitative Variable Explorer"
