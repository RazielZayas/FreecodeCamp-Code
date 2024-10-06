import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('medical_examination.csv')

df['overweight'] = np.where(df['weight'] / ((df['height'] * 0.01) ** 2) > 25, 1, 0)


df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)


def draw_cat_plot():
    
    df_cat = sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat = pd.melt(df, id_vars = 'cardio', value_vars = df_cat)
    
    graph = sns.catplot(x='variable', col='cardio', hue='value', kind='count', data=df_cat).set_axis_labels("variable", "total")

    fig = graph.fig

    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    
    corr = df_heat.corr()


    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    
    fig, ax = plt.subplots(figsize=(10, 10))

    
    ax = sns.heatmap(corr, vmin=0, vmax=.25, square=True, cbar_kws={"shrink": .50}, annot=True, fmt='.1f', linewidths=.5, mask=mask)


    
    fig.savefig('heatmap.png')
    return fig
