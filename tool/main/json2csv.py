import sys
import os
import csv
import re
import datetime

import ijson

# 主処理
def main():
    # 処理開始時間の取得
    start_time = datetime.datetime.now()

    # コマンドライン引数の取得
    args = sys.argv
    # カラム定義ファイル名
    column_def_file = 'header_def.csv'
    
    # 引数が不足している場合、エラーメッセージを出力して終了する
    if (not is_valid_args(args)):
        error('引数が不足しています。')
        usage('targetディレクトリに変換元JSONファイルと変換先CSVファイルのカラム定義ファイル（header_def.csv）を配置し、下記コマンドを実行してください。')
        usage('python json2csv.py 変換元JSONファイル名 変換先CSVファイル名')
        return
    
    # カラム定義ファイルがない場合、エラーメッセージを出力して終了する
    if (not is_exist_file(column_def_file)):
        error('変換先CSVファイルのカラム定義ファイルがありません。')
        usage(f'targetディレクトリに変換先CSVファイルのカラム定義ファイル（{column_def_file}）を配置してください。')
        return
    
    # 変換元JSONファイル名
    json_file_name = sys.argv[1]
    # 変換先CSVファイル名
    csv_file_name = sys.argv[2]

    # 変換元JSONファイルが存在しない場合、エラーメッセージを出力して終了する
    if (not is_exist_file(json_file_name)):
        error(f'変換元JSONファイルがありません。 ファイル名：{json_file_name}')
        usage('targetディレクトリに変換元JSONファイルを配置してください。')
        return

    # 変換先CSVファイルのカラム定義取得
    info('カラム定義ファイルの読み込みを開始します。')
    try:
        column_def_list = read_column_def_file(column_def_file)
        info('カラム定義ファイルの読み込みが正常に完了しました。')
    except ValueError as ve:
        error('カラム定義ファイルの読み込み中にエラーが発生しました。有効な定義がありません。')
        return
    except Exception as e:
        error(f'カラム定義ファイルの読み込み中に予期せぬエラーが発生しました。')
        return
    
    # 変換元JSONから変換先CSVへの変換実行
    info('CSVファイルへの変換を開始します。')
    try:
        record_processed = convert_json_to_csv(json_file_name, csv_file_name, column_def_list)
        end_time = datetime.datetime.now()
        elapsed_time = end_time - start_time
        info(f'CSVファイルへの変換が正常に完了しました。処理件数：{record_processed}, 処理時間：{elapsed_time}')
    except Exception as e:
        error('CSVファイルへの変換中に予期せぬエラーが発生しました。')
        return

# 引数の数が正しいか判定する関数
def is_valid_args(args):
    if (len(args) != 3):
        return False
    return True

# ファイルの存在を確認する関数
def is_exist_file(file):
    file_path = os.path.join(os.path.dirname(__file__), f'{getTargetDir()}{file}')
    if (not os.path.isfile(file_path)):
        return False
    return True

# カラム定義ファイルを読み込む関数
def read_column_def_file(def_file_name):
    # カラム定義ファイルはtargetディレクトリに配置することにする
    def_file_name = os.path.join(os.path.dirname(__file__), f'{getTargetDir()}{def_file_name}')
    with open(def_file_name, encoding='UTF-8') as column_def_file:
        # 読み込んだ結果を改行コードで分割し、リスト化する
        column_def = column_def_file.read()
        column_def_list = column_def.split('\n')

        # 重複を削除
        column_def_list = sorted(set(column_def_list), key=column_def_list.index)

        # 空白系文字、カンマなどはすべて無視する
        mapped_list = map(lambda key: str.strip(key), column_def_list)
        filtered_list = filter(lambda key: key != '', list(mapped_list))
        column_def_list = list(filtered_list)

        # クレンジングした結果、定義が1件もない場合は例外を送出する
        if (len(column_def_list) < 1):
            raise ValueError()

        return column_def_list

# JSONからCSVへ変換する関数
def convert_json_to_csv(json_file_name, csv_file_name, column_def_list):
    csv_file_name = os.path.join(os.path.dirname(__file__), f'{getTargetDir()}{csv_file_name}')
    json_file_name = os.path.join(os.path.dirname(__file__), f'{getTargetDir()}{json_file_name}')
    # Windows 環境だと \r\n になってしまうので、\n を指定して開く
    with open(csv_file_name, encoding='UTF-8', mode='w', newline='\n') as csv_file:
        # カラム定義ファイルに従ってヘッダ行を書き込む
        csv_writer = csv.DictWriter(csv_file, fieldnames=column_def_list, extrasaction='ignore', lineterminator='\n')
        csv_writer.writeheader()

        # 処理件数の初期化
        record_processed = 0

        # 変換元JSONファイルを1レコードずつ読み込み、CSVファイルへ書き出す
        with open(json_file_name, mode='br') as json_file:
            for entry in ijson.items(json_file, "item"):
                csv_writer.writerow(entry)
                record_processed += 1
    
    # 処理件数を呼び出し元へ返却する
    return record_processed

# ログ用ユーティリティ
def log(type, message):
    timestamp = datetime.datetime.now()
    print(f'{timestamp} [{type}] {message}')

def error(message):
    log('ERROR', message)

def info(message):
    log('INFO ', message)

def usage(message):
    log('USAGE', message)

def getTargetDir():
    return '../target/'

# モジュールとして呼ばれることは想定しない
if __name__ == '__main__':
    main()