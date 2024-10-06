import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Se importa los datos
df = pd.read_csv('medical_examination.csv')

# 2 Se especifica la columna Overweitght
df['overweight'] = np.where(df['weight'] / ((df['height'] * 0.01) ** 2) > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = pd.melt(df, id_vars = 'cardio', value_vars = df_cat)
    

    # 7
    graph = sns.catplot(x='variable', col='cardio', hue='value', kind='count', data=df_cat).set_axis_labels("variable", "total")


    # 8
    fig = graph.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # 14
    fig, ax = plt.subplots(figsize=(10, 10))

    # 15
    ax = sns.heatmap(corr, vmin=0, vmax=.25, square=True, cbar_kws={"shrink": .50}, annot=True, fmt='.1f', linewidths=.5, mask=mask)


    # 16
    fig.savefig('heatmap.png')
    return fig