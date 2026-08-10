import os

from word_frequencies.core import WeightedNouns

class Test_WeightedNouns:

    def test_mustBeFound(self):
        wn = WeightedNouns()
        file_path = wn.get_source_file_path()
        assert '.txt' == file_path[-4:]
        assert os.path.exists(file_path)

    def test_mustBeImportable(self):
        wn = WeightedNouns()
        file_path = wn.get_source_file_path()
        assert os.path.exists(file_path)
        result = wn.load_from_path(file_path)
        assert 1833 == result[0][0]
        assert 'time' == result[0][1]
        assert 10 == result[-1][0]
        assert 'morale' == result[-1][1]
        assert 3030 == len(result)

    def test_mustBeCreatedWithoutErrors(self):
        wn = WeightedNouns()
        nouns = wn.get_weighted_list()
        assert isinstance(nouns, list)
        
