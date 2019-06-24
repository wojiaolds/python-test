import pandas as pd

# df=pd.read_excel('lemon.xlsx')
# df.to_excel("sample.xlsx",sheet_name='python',index=False)


def find_need_data():
    raw_data = pd.read_excel("lemon.xlsx")
    print(raw_data)
    all_need = []
    need_list = ["正常", "密码",'正常充']
    for n in need_list:
        # find need data
        need = raw_data[raw_data["title"].str.contains(n)]
        # print(type(need))
        print("need \n",need)

        all_need.append(need)

    print(all_need)
    # write all need data into excel

    w = pd.concat(all_need,ignore_index=True)
    print(type(w))
    l = []
    for i in range(len(w)):
        l.append('m')
    w['sex'] = l
    print(w['sex'])
    print(w)
    w.loc[2] = ['小火猴', 1, '火', 'None']
    try:
        f = pd.DataFrame([['小火', 1, '火', 'None']],columns=w.columns)
        w = w.append(f)
    except BaseException as ex:
        print(ex)
    print(w)
    w.to_excel("sample.xlsx",sheet_name='python',index=False)

find_need_data()