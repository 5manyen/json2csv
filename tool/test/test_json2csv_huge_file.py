from ..main.json2csv import convert_json_to_csv

def test_convert_json_to_csv_case_huge(mocker):
    # 巨大なJSONの変換（1件あたり5KB,1,000,000件）
    column_def_list = ['wwwwwwwwwwe85vx\n', 'wwwwwwwwww4qOhZ\n', 'wwwwwwwwwwHINyb\n', 'wwwwwwwwwwY9xkr\n', 'wwwwwwwwwwzSAgu\n', 'wwwwwwwwwwTZrCz\n', 'wwwwwwwwwwvTGcB\n', 'wwwwwwwwwwxIzbx\n', 'wwwwwwwwwwB3mku\n', 'wwwwwwwwww45AO6\n', 'wwwwwwwwwwoKVrT\n', 'wwwwwwwwwwTD6hP\n', 'wwwwwwwwwwnR2JJ\n', 'wwwwwwwwwwyirha\n', 'wwwwwwwwwwnhNzZ\n', 'wwwwwwwwwwRjGEL\n', 'wwwwwwwwwwd5Dxc\n', 'wwwwwwwwwwgLMHY\n', 'wwwwwwwwwwysf8w\n', 'wwwwwwwwwwtzl6q\n', 'wwwwwwwwwwmyfzy\n', 'wwwwwwwwwwsgz4d\n', 'wwwwwwwwwwqBakB\n', 'wwwwwwwwwwSyGdU\n', 'wwwwwwwwwwXHP2f\n', 'wwwwwwwwwwqCAxE\n', 'wwwwwwwwwwJHCEu\n', 'wwwwwwwwwwAPcos\n', 'wwwwwwwwwwhviUf\n', 'wwwwwwwwwwELrCK\n', 'wwwwwwwwwwbDWOU\n', 'wwwwwwwwwwxcf7q\n', 'wwwwwwwwwwxaXKZ\n', 'wwwwwwwwwwrSsz6\n', 'wwwwwwwwwwvMd5q\n', 'wwwwwwwwwwhOtt5\n', 'wwwwwwwwwwtG4Jc\n', 'wwwwwwwwwwcA0DP\n', 'wwwwwwwwwwTiMt3\n', 'wwwwwwwwwwEqdtz\n', 'wwwwwwwwwwe4JRr\n', 'wwwwwwwwwwqe1jE\n', 'wwwwwwwwww72Ld3\n', 'wwwwwwwwwwjgJiP\n', 'wwwwwwwwwwRZmxG\n', 'wwwwwwwwwwB1gAO\n', 'wwwwwwwwwwvbcnh\n', 'wwwwwwwwww1EqiO\n', 'wwwwwwwwwwyd8wH\n', 'wwwwwwwwww5Pini\n', 'wwwwwwwwwwTSWjP\n', 'wwwwwwwwwwYCmZn\n', 'wwwwwwwwwwAGVqg\n', 'wwwwwwwwwwKlGRe\n', 'wwwwwwwwwwWDvBX\n', 'wwwwwwwwwwcqGml\n', 'wwwwwwwwwwkLS4o\n', 'wwwwwwwwwwxvEpl\n', 'wwwwwwwwwwsJzmg\n', 'wwwwwwwwwwGOhuo\n', 'wwwwwwwwww1ei4r\n', 'wwwwwwwwwww2gZI\n', 'wwwwwwwwwwY5O3X\n', 'wwwwwwwwwwzGgNW\n', 'wwwwwwwwwwvBoJA\n', 'wwwwwwwwwwxxU1J\n', 'wwwwwwwwwwTkELh\n', 'wwwwwwwwwwWzmc7\n', 'wwwwwwwwwwRsfHb\n', 'wwwwwwwwwwwtOwJ\n', 'wwwwwwwwwwdEyyA\n', 'wwwwwwwwww0ua71\n', 'wwwwwwwwwwGxL5L\n', 'wwwwwwwwwwVFf2I\n', 'wwwwwwwwwwQtNRe\n', 'wwwwwwwwwwyIo7z\n', 'wwwwwwwwwwoLIJt\n', 'wwwwwwwwwwFPxNr\n', 'wwwwwwwwwwC5xAX\n', 'wwwwwwwwwwNDAxL\n', 'wwwwwwwwwwpoV90\n', 'wwwwwwwwwwMEmfi\n', 'wwwwwwwwwwonKaq\n', 'wwwwwwwwwwndHPy\n', 'wwwwwwwwwwbeARL\n', 'wwwwwwwwww3v8Si\n', 'wwwwwwwwwwgoora\n', 'wwwwwwwwwwr8hLo\n', 'wwwwwwwwwwhoDpe\n', 'wwwwwwwwwwbXqlI\n', 'wwwwwwwwwwecrSV\n', 'wwwwwwwwwwvpSjh\n', 'wwwwwwwwwwjYumU\n', 'wwwwwwwwwwJ2OFM\n', 'wwwwwwwwwwD23H3\n', 'wwwwwwwwwwdlnbJ\n', 'wwwwwwwwwwNCwNc\n', 'wwwwwwwwww8aWvB\n', 'wwwwwwwwwwruM73\n', 'wwwwwwwwwwsUq70\n', 'wwwwwwwwww5M1f2\n', 'wwwwwwwwwwvjG9T\n', 'wwwwwwwwwwZ6i8x\n', 'wwwwwwwwwwSLS5n\n', 'wwwwwwwwwwPiCYP\n', 'wwwwwwwwww956UC\n', 'wwwwwwwwwwXP6qk\n', 'wwwwwwwwwwY2wUq\n', 'wwwwwwwwwwe7PwO\n', 'wwwwwwwwwwtesWa\n', 'wwwwwwwwwwoXkZr\n', 'wwwwwwwwww33iM8\n', 'wwwwwwwwwwb7qiE\n', 'wwwwwwwwwwWFtz9\n', 'wwwwwwwwww7QOXe\n', 'wwwwwwwwwwAeSwF\n', 'wwwwwwwwww98mLn\n', 'wwwwwwwwwwilXUI\n', 'wwwwwwwwww7jDRe\n', 'wwwwwwwwwwN1CHF\n', 'wwwwwwwwwwK4L5I\n', 'wwwwwwwwww7yoOs\n', 'wwwwwwwwwwdclcA\n', 'wwwwwwwwwwHsFTa\n', 'wwwwwwwwwwLqPod\n', 'wwwwwwwwwwm5Eng\n', 'wwwwwwwwwwovoIl\n', 'wwwwwwwwwwJsp7e\n', 'wwwwwwwwwwbwrSG\n', 'wwwwwwwwwwEQ251\n', 'wwwwwwwwwwPkcXV\n', 'wwwwwwwwww4cH2P\n', 'wwwwwwwwww7BI3x\n', 'wwwwwwwwwwcN6do\n', 'wwwwwwwwwwUbEP4\n', 'wwwwwwwwww2z31k\n', 'wwwwwwwwwwnbSMQ\n', 'wwwwwwwwwwi8w0a\n', 'wwwwwwwwww5688P\n', 'wwwwwwwwwwBFJYy\n', 'wwwwwwwwwwc3XbY\n', 'wwwwwwwwwwT8WWJ\n', 'wwwwwwwwwwemC5J\n', 'wwwwwwwwwwx0nBL\n', 'wwwwwwwwwwYNK0q\n', 'wwwwwwwwwwB9cSs\n', 'wwwwwwwwwwkZQoA\n', 'wwwwwwwwww1tzjg\n', 'wwwwwwwwwwaGgEn\n', 'wwwwwwwwww6sTst\n', 'wwwwwwwwwwoqoSz\n', 'wwwwwwwwww5fZEx\n', 'wwwwwwwwwwBjw8I\n', 'wwwwwwwwwwJdjT4\n', 'wwwwwwwwwwuu9Dc\n', 'wwwwwwwwww8oR8X\n', 'wwwwwwwwwwsNf6n\n', 'wwwwwwwwwwNle35\n', 'wwwwwwwwwwFeAqm\n', 'wwwwwwwwwwAjtNY\n', 'wwwwwwwwwwRC0MO\n', 'wwwwwwwwwwkpJqb\n', 'wwwwwwwwwwlq7A0\n', 'wwwwwwwwwwDK7T3\n', 'wwwwwwwwwwppW5F\n', 'wwwwwwwwwwOMhsw\n', 'wwwwwwwwww7Z7ir\n', 'wwwwwwwwwwOBnlo\n', 'wwwwwwwwwwH7DQB\n', 'wwwwwwwwwwib5uj\n', 'wwwwwwwwwwFGiGZ\n', 'wwwwwwwwww2Ftej\n', 'wwwwwwwwwwJEAQx\n', 'wwwwwwwwwwLnlZG\n', 'wwwwwwwwwwhALLn\n', 'wwwwwwwwwwFZ0cY\n', 'wwwwwwwwww8u9V5\n', 'wwwwwwwwwwoQ3k2\n', 'wwwwwwwwwwOB9tE\n', 'wwwwwwwwwwha7t9\n', 'wwwwwwwwwwWZBHn\n', 'wwwwwwwwww6qVe9\n', 'wwwwwwwwwwt5GTt\n', 'wwwwwwwwwwpqi2P\n', 'wwwwwwwwwwF8F0U\n', 'wwwwwwwwwwn2ug3\n', 'wwwwwwwwwwcbWy4\n', 'wwwwwwwwww0hoQo\n', 'wwwwwwwwwwXxXjc\n', 'wwwwwwwwwwnnncJ\n', 'wwwwwwwwwwMsQAN\n', 'wwwwwwwwwwTV9XS\n', 'wwwwwwwwwwkwAvG\n', 'wwwwwwwwwwymVbD\n', 'wwwwwwwwwwahjlp\n', 'wwwwwwwwww0Booz\n', 'wwwwwwwwwwYlJY4\n', 'wwwwwwwwwwBW6G3\n', 'wwwwwwwwwwwdotD\n', 'wwwwwwwwwwXBPAO']
    json_file = 'test_huge_file.json'
    csv_file = 'test_huge_file.csv'
    mocker.patch('tool.main.json_to_csv_converter.getTargetDir', return_value='../test/test_data/huge_file/')
    records = convert_json_to_csv(json_file, csv_file, column_def_list)
    assert records == 1000000