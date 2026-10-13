import pandas as pd 
from matplotlib.axes import Axes
from .constants import groups_palette


def bar_builder(df: pd.DataFrame, ax: Axes) -> None: 
    '''Функция, строящая барплот для аналитического блока 02.'''
    for i, (label, data) in enumerate(df.iterrows()):  
        x = df.columns if i == 0 else [n + (i * .265) for n in range(len(df.columns))]
        ax.bar(
            x=x, height=data, 
            width = .8 / 3, 
            label=label, color=groups_palette[i]
    )
    
    ax.set_xticks([n + .26 for n in range(len(df.columns))])