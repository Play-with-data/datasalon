import pandas as pd

kto_201901 = pd.read_excel('./files/kto_201901.xlsx',
                            header=1,
                            usecols='A:G',
                            skipfooter=4)

kto_201901.head()
kto_201901.tail()
kto_201901.info()
kto_201901.describe()

condition = (kto_201901['관광'] == 0) \
    | (kto_201901['상용'] == 0) \
    | (kto_201901['공용'] == 0) \
    | (kto_201901['유학/연수'] == 0)
kto_201901[condition]

kto_201901['기준년월'] = '2019-01'
kto_201901.head()

kto_201901['국적'].unique()

continents_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', \
    '기타대륙', '교포소계']
continents_list

condition = (kto_201901.국적.isin(continents_list) == False)
kto_201901_contury = kto_201901[condition]
kto_201901_contury['국적'].unique()

kto_201901_contury.head()
# drop = True 가 아니면 인덱스 값이 새로운 칼럼으로 생성
kto_201901_contury_newindex = kto_201901_contury.reset_index(drop = True)
kto_201901_contury_newindex.head()

continents = ['아시아'] * 25 + ['아메리카'] * 5 + ['유럽'] * 23 + \
    ['오세아니아'] * 3 + ['아프리카'] * 2 + ['기타대륙'] + ['교포']
continents

kto_201901_contury_newindex['대륙'] = continents
kto_201901_contury_newindex

kto_201901_contury_newindex['관광객비율(%)'] = \
    round(kto_201901_contury_newindex['관광'] / kto_201901_contury_newindex['계'] * 100, 1)
kto_201901_contury_newindex.head()
kto_201901_contury_newindex.tail()

kto_201901_contury_newindex.sort_values(by = '관광객비율(%)', ascending = False).head()
kto_201901_contury_newindex.sort_values(by = '관광객비율(%)', ascending = True).head()

kto_201901_contury_newindex.pivot_table(values = '관광객비율(%)',
                                        index = '대륙',
                                        aggfunc = 'mean')

condition = (kto_201901_contury_newindex.국적 == '중국')
kto_201901_contury_newindex[condition]

tourist_sum = sum(kto_201901_contury_newindex['관광'])
tourist_sum

kto_201901_contury_newindex['전체비율(%)'] = \
    round(kto_201901_contury_newindex['관광'] / tourist_sum * 100, 1)

kto_201901_contury_newindex.head()
kto_201901_contury_newindex.sort_values('전체비율(%)', ascending = False).head()

def create_kto_data(yy, mm):
    file_path = './files/kto_{}{}.xlsx'.format(yy, mm)

    df = pd.read_excel(file_path, header=1, usecols='A:G', skipfooter=4)

    df['기준년월'] = '{}-{}'.format(yy, mm)

    ignore_list = ['아시아주', '미주', '구주', '대양주', \
        '아프리카주', '기타대륙', '교포소계']
    condition = (df['국적'].isin(ignore_list) == False)
    df_contury = df[condition].reset_index(drop = True)

    continents = ['아시아'] * 25 + ['아메리카'] * 5 + \
        ['유럽'] * 23 + ['오세아니아'] * 3 + ['아프리카'] * 2 + \
        ['기타대륙'] + ['교포']
    df_contury['대륙'] = continents

    df_contury['관광객비율(%)'] = \
        round(df_contury['관광'] / df_contury['계'] * 100, 1)

    tourist_sum = sum(df_contury['관광'])
    df_contury['전체비율(%)'] = \
        round(df_contury['관광'] / tourist_sum * 100, 1)

    return(df_contury)

kto_test = create_kto_data('2018', '02')
kto_test.head()

def create_kto_data_frame():
    for yy in range(2010, 2020):
        for mm in range(1, 13):
            try:
                temp = create_kto_data(str(yy), str(mm).zfill(2))
                df = df.append(temp, ignore_index = True)
            except:
                pass

df = pd.DataFrame()
create_kto_data_frame()
df.head()
df.tail()
df.info()

df.to_excel('./files/kto_total.xlsx', index=False)