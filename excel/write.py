import pandas as pd

# df=pd.read_excel('lemon.xlsx')
# df.to_excel("sample.xlsx",sheet_name='python',index=False)

def find_need_data():
    raw_data = pd.read_excel("lemon.xlsx")
    print(type(raw_data))
    all_need = []
    need_list = ["正常", "密码"]
    for n in need_list:
        # find need data
        need = raw_data[raw_data["title"].str.contains(n)]
        # print(type(need))
        # print("need \n",need[0:].values)

        all_need.append(need)

    # print(all_need)
    # write all need data into excel

    w = pd.concat(all_need)
    print(type(w))
    l = []
    for i in range(len(w)):
        l.append('m')
    w['sex'] = l
    print(w['sex'])
    w.iloc[3] = ['小火猴', 1, '火', 'None']
    print(w)
    w.to_excel("sample.xlsx",sheet_name='python',index=False)

find_need_data()