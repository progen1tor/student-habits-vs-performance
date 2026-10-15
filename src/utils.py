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
    
    
def probability_counter(df: pd.DataFrame, col_name: str, threshold: int, have_factor: bool = True) -> float: 
    '''Функция, считающая вероятности успешной сдачи экзамена (80+ баллов) при наличии / отсутствии определенного фактора (аналитический блок 04).'''
    if have_factor:
        return df.loc[(df.exam_score >= 80) & (df[col_name] >= threshold)].shape[0] / df.loc[df[col_name] >= threshold].shape[0] * 100
    return df.loc[(df.exam_score >= 80) & (df[col_name] < threshold)].shape[0] / df.loc[df[col_name] < threshold].shape[0] * 100