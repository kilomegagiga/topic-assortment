import os
import csv

class Test_os_module:

    def test_mustFindLocationOfCurrentFile(self):
        file_path = os.path.realpath(__file__)
        assert file_path
        assert '/' == file_path[:1]
        assert '.py' == file_path[-3:]

class Test_csv_module:

    def test_mustImportTabSeparatedValues(self):
        ## Reading from a list instead of a file is not
        ## documented to work, but it does.

        fake_file = ['\tfirst\tsecond\tthird']
        reader = csv.reader(fake_file, delimiter='\t')
        result = ''
        for row in reader:
            result = result + ', '.join(row) + '\n'
        assert ', first, second, third\n' == result
