import pandas as pd
import eel
import os

def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_name, save_path):
    # 検索対象取得
    df=pd.read_csv("./{}".format(csv_name))
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』はあります".format(word))
        res = True
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はありません".format(word))
        eel.view_log_js("『{}』を追加します".format(word))
        res = False
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    
    save_file_at_dir(save_path, 'source_new.csv', str(df))
    
    df.to_csv("./source.csv",encoding="utf_8-sig")
    print(source)
    
    
