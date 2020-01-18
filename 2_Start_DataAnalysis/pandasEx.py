# 예제 2-1 pandas 라이브러리 불러오기
import pandas as pd

# 예제 2-2 sample_1.xlsx 엑셀데이터 불러오기
sample_1 = pd.read_excel('./files/sample_1.xlsx', 
                         header=1, 
                         skipfooter=2, 
                         usecols='A:C')
sample_1.head(3)

numbers = ['A01', 'A18']

conditions = (sample_1['국적코드'].isin(numbers))
sample_1[conditions == False]

sample_1['기준년월'] = '2019-11'

sample_1

code_master = pd.read_excel('./files/sample_codemaster.xlsx')
code_master

sample_1_code = pd.merge(left = sample_1,
                        right = code_master,
                        how = 'left',
                        left_on = '국적코드',
                        right_on= '국적코드')

sample_1_code

sample_2 = pd.read_excel('./files/sample_2.xlsx',
                        header=1,
                        skipfooter=2,
                        usecols='A:C')
sample_2['기준년월'] = '2019-12'
sample_2_code = pd.merge(left=sample_2,
                        right=code_master,
                        how='left',
                        left_on='국적코드',
                        right_on='국적코드')
sample_2_code
sample_1_code

sample = sample_1_code.append(sample_2_code, ignore_index = True)
sample

sample.to_excel('./files/sample.xlsx')
sample.to_excel('./files/sample_index_false.xlsx', index = False)

sample_pivot = sample.pivot_table(values='입국객수',
                                index='국적명',
                                columns='기준년월',
                                aggfunc='mean')

sample_pivot

sample_pivot2 = sample.pivot_table(values='입국객수',
                                index='국적명',
                                aggfunc='max')

sample_pivot2