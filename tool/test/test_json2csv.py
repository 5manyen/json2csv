
import sys
import os
import pytest
from unittest.mock import call

from ..main import json2csv
from ..main.json2csv import (
    is_valid_args,
    is_exist_file,
    read_column_def_file,
    convert_json_to_csv,
    main
)

# ========= is_valid_args =========
def test_is_valid_args():
    assert is_valid_args([]) == False
    assert is_valid_args(['one']) == False
    assert is_valid_args(['one', 'two']) == False
    assert is_valid_args(['one', 'two', 'three']) == True
    assert is_valid_args(['one', 'two', 'three', 'four']) == False

# ========= is_exist_file =========
def test_is_exist_file_case_1(mocker):
    # ファイルが存在するケース
    mocker.patch('os.path.isfile', return_value=True)
    assert is_exist_file('true case') == True

def test_is_exist_file_case_2(mocker):
    # ファイルが存在しないケース
    mocker.patch('os.path.isfile', return_value=False)
    assert is_exist_file('false case') == False

# ========= read_column_def_file =========
def test_read_column_def_file_case_1(mocker):
    # 普通に定義したケース
    expected = ['one', 'two', 'three']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/read_column_def_file/')

    result_case1 = read_column_def_file('case_1.csv')
    assert result_case1 == expected
    
def test_read_column_def_file_case_2(mocker):
    # 半角空白、全角空白、タブ、空行が無視され、定義が1件もないケース
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/read_column_def_file/')

    with pytest.raises(ValueError):
        result_case2 = read_column_def_file('case_2.csv')

def test_read_column_def_file_case_3(mocker):
    # 正しい定義の中に空行と重複が混ざっているケース
    expected = ['one', 'two', 'three']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/read_column_def_file/')

    result_case3 = read_column_def_file('case_3.csv')
    assert result_case3 == expected

def test_read_column_def_file_case_4(mocker):
    # キーの中に記号が含まれるケース
    expected = ['one', 'two,', 'th re/e']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/read_column_def_file/')

    result_case4 = read_column_def_file('case_4.csv')
    assert result_case4 == expected

# ========= convert_json_to_csv =========
def test_convert_json_to_csv_case_1(mocker):
    # シンプルなJSONが10件あるケース
    case_1_column_def_list = ['one', 'two', 'three']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/convert_json_to_csv/')

    case_1_json_file = 'case_1.json'
    case_1_csv_file = 'case_1.csv'
    records = convert_json_to_csv(case_1_json_file, case_1_csv_file, case_1_column_def_list)

    assert records == 10
    output_path = os.path.join(os.path.dirname(__file__), f'../test/test_data/convert_json_to_csv/{case_1_csv_file}')
    with open(output_path, encoding='UTF-8', newline='') as output_file:
        for line in output_file.readlines():
            assert not line.endswith('\r\n')
            assert line.endswith('\n')

def test_convert_json_to_csv_case_2(mocker):
    # シンプルなJSONが10件あり、かつカラム定義が全量でないケース
    case_2_column_def_list = ['one', 'three']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/convert_json_to_csv/')

    case_2_json_file = 'case_2.json'
    case_2_csv_file = 'case_2.csv'
    records = convert_json_to_csv(case_2_json_file, case_2_csv_file, case_2_column_def_list)
    assert records == 10

def test_convert_json_to_csv_case_3(mocker):
    # シンプルなJSONが10件あり、かつJSONにないカラム定義があるケース
    case_3_column_def_list = ['one', 'dos', 'three']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/convert_json_to_csv/')

    case_3_json_file = 'case_3.json'
    case_3_csv_file = 'case_3.csv'
    records = convert_json_to_csv(case_3_json_file, case_3_csv_file, case_3_column_def_list)
    assert records == 10

def test_convert_json_to_csv_case_4(mocker):
    # JSONのバリューにカンマが入っているケース
    case_4_column_def_list = ['one', 'two', 'three']
    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/convert_json_to_csv/')

    case_4_json_file = 'case_4.json'
    case_4_csv_file = 'case_4.csv'
    records = convert_json_to_csv(case_4_json_file, case_4_csv_file, case_4_column_def_list)
    assert records == 10

# ========= main =========
def test_main_case_1(mocker):
    # 正常に終了するケース
    args = ['test.py', 'case_1.json', 'case_1.csv']
    header_list = ['one', 'two', 'three']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    mock_read_column_def_file = mocker.patch('tool.main.json2csv.read_column_def_file', return_value=header_list)
    spy_convert_json_to_csv = mocker.spy(json2csv, 'convert_json_to_csv')

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_has_calls([call('header_def.csv'), call(args[1])])
    mock_read_column_def_file.assert_called_once_with('header_def.csv')
    spy_convert_json_to_csv.assert_called_once_with(args[1], args[2], header_list)

def test_main_case_2(mocker):
    # 引数不足でエラーになるケース
    args = ['test.py', 'case_1.json']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    spy_read_column_def_file = mocker.spy(json2csv, 'read_column_def_file')
    spy_convert_json_to_csv = mocker.spy(json2csv, 'convert_json_to_csv')

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_not_called()
    spy_read_column_def_file.assert_not_called()
    spy_convert_json_to_csv.assert_not_called()

def test_main_case_3(mocker):
    # カラム定義ファイルが存在せずエラーになるケース
    args = ['test.py', 'case_1.json', 'case_1.csv']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    mocker.patch('os.path.isfile', return_value=False)
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    spy_read_column_def_file = mocker.spy(json2csv, 'read_column_def_file')
    spy_convert_json_to_csv = mocker.spy(json2csv, 'convert_json_to_csv')

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_called_once_with('header_def.csv')
    spy_read_column_def_file.assert_not_called()
    spy_convert_json_to_csv.assert_not_called()


def test_main_case_4(mocker):
    # 変換元JSONファイルが存在せずエラーになるケース
    args = ['test.py', 'not_exist.json', 'case_1.csv']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    spy_read_column_def_file = mocker.spy(json2csv, 'read_column_def_file')
    spy_convert_json_to_csv = mocker.spy(json2csv, 'convert_json_to_csv')

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_has_calls([call('header_def.csv'), call(args[1])])
    spy_read_column_def_file.assert_not_called()
    spy_convert_json_to_csv.assert_not_called()

def test_main_case_5(mocker):
    # カラム定義が不正でエラーになるケース
    args = ['test.py', 'case_1.json', 'case_1.csv']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    mock_read_column_def_file = mocker.patch('tool.main.json2csv.read_column_def_file', side_effect=ValueError("test"))
    spy_convert_json_to_csv = mocker.spy(json2csv, 'convert_json_to_csv')

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_has_calls([call('header_def.csv'), call(args[1])])
    mock_read_column_def_file.assert_called_once_with('header_def.csv')
    spy_convert_json_to_csv.assert_not_called()

def test_main_case_6(mocker):
    # カラム定義ファイルの読み込み中に予期せぬエラーになるケース
    args = ['test.py', 'case_1.json', 'case_1.csv']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    mock_read_column_def_file = mocker.patch('tool.main.json2csv.read_column_def_file', side_effect=Exception("test"))
    spy_convert_json_to_csv = mocker.spy(json2csv, 'convert_json_to_csv')

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_has_calls([call('header_def.csv'), call(args[1])])
    mock_read_column_def_file.assert_called_once_with('header_def.csv')
    spy_convert_json_to_csv.assert_not_called()

def test_main_case_7(mocker):
    # CSVファイルへの変換中に予期せぬエラーになるケース
    args = ['test.py', 'case_1.json', 'case_1.csv']
    header_list = ['one', 'two', 'three']

    mocker.patch('tool.main.json2csv.getTargetDir', return_value='../test/test_data/main/')
    mocker.patch.object(sys, 'argv', args)
    spy_is_valid_args = mocker.spy(json2csv, 'is_valid_args')
    spy_is_exist_file = mocker.spy(json2csv, 'is_exist_file')
    mock_read_column_def_file = mocker.patch('tool.main.json2csv.read_column_def_file', return_value=header_list)
    mock_convert_json_to_csv = mocker.patch('tool.main.json2csv.convert_json_to_csv', side_effect=Exception('test'))

    main()

    spy_is_valid_args.assert_called_once_with(args)
    spy_is_exist_file.assert_has_calls([call('header_def.csv'), call(args[1])])
    mock_read_column_def_file.assert_called_once_with('header_def.csv')
    mock_convert_json_to_csv.assert_called_once_with(args[1], args[2], header_list)