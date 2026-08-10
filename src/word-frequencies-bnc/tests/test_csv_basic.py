import csv

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
