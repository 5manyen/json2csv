import random
import string
import json

def generate_huge_json():
    entry = {}
    json_list = []
    for i in range(200):
        # 10桁の固定文字列と5桁のランダム文字列でキーを作る
        key_fixed_part = 'wwwwwwwwww'
        key_random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        key = key_fixed_part + key_random_part

        # 値はランダム文字列100桁
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        entry[key] = value
    keys_string = '\n'.join(entry.keys())

    # キー情報の出力
    print(f'KEYS:\n{keys_string}')

    # 増幅処理
    for i in range(1000000):
        json_list.append(entry)
    with open('generated.json', encoding='UTF-8', mode='w') as json_file:
        json.dump(json_list, json_file)

if __name__ == '__main__':
    # DO NOT RUN UNLESS NECESSARY
    generate_huge_json()