import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('./files/kto_total.xlsx')
df.head()

def resolve_korean_font_problem():  
    from matplotlib import font_manager, rc
    import platform

    if platform.system() == 'Windows':
        path = 'C:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=path).get_name()
        rc('font', family = font_name)
    elif platform.system() == 'Darwin':
        rc('font', family = 'AppleGothic')
    else:
        print('Check your OS system')

resolve_korean_font_problem()

condition = (df['국적'] == '중국')
df_filter = df[condition].reset_index(drop=True)
df_filter.head()

plt.figure(figsize= (12, 4))
plt.plot(df_filter['기준년월'], df_filter['관광'])
plt.title('중국 국적의 관광객 추이')
plt.xlabel('기준년월')
plt.ylabel('관광객수')

plt.xticks(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01'])
plt.show()

cntry_list = ['중국', '일본', '대만', '미국', '홍콩']
for cntry in cntry_list:
    condition = (df['국적'] == cntry)
    df_filter = df[condition]

    plt.figure(figsize= (12, 4))
    plt.plot(df_filter['기준년월'], df_filter['관광'])
    plt.title('{} 국적의 관광객 추이'.format(cntry))
    plt.xlabel('기준년월')
    plt.ylabel('관광객수')

    plt.xticks(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01'])
    plt.show()

df['년도'] = df['기준년월'].str.slice(0, 4)
df['월'] = df['기준년월'].str.slice(5, 7)
df.head()

condition = (df['국적'] == '중국')
df_filter = df[condition]
df_filter.head()

df_pivot = df_filter.pivot_table(values='관광',
                                index='년도',
                                columns='월')
df_pivot

plt.figure(figsize= (16, 10))
sns.heatmap(df_pivot, annot=True, fmt='.0f', cmap='rocket_r')
plt.title('중국 관광객 히트맵')
plt.show()

cntry_list = ['중국', '일본', '대만', '미국', '홍콩']
for cntry in cntry_list:
    condition = (df['국적'] == cntry)
    df_filter = df[condition]

    df_pivot = df_filter.pivot_table(values='관광',
                                index='년도',
                                columns='월')

    plt.figure(figsize= (16, 10))
    sns.heatmap(df_pivot, annot=True, fmt='.0f', cmap='rocket_r')
    plt.title('{} 관광객 히트맵'.format(cntry))
    plt.show()