import os

from word_frequencies.word_lists import WeightedAdjectives

class Test_WeightedAdjectives:

    def test_mustBeFound(self):
        wn = WeightedAdjectives()
        file_path = wn.get_source_file_path()
        assert '.txt' == file_path[-4:]
        assert os.path.exists(file_path)

    def test_mustBeImportable(self):
        wn = WeightedAdjectives()
        file_path = wn.get_source_file_path()
        assert os.path.exists(file_path)
        result = wn.load_from_path(file_path)
        assert 1336 == result[0][0]
        assert 'other' == result[0][1]
        assert 10 == result[-1][0]
        assert 'disturbing' == result[-1][1]
        assert 1035 == len(result)

    def test_mustBeCreatedWithoutErrors(self):
        wn = WeightedAdjectives()
        adjectives = wn.get_weighted_list()
        assert isinstance(adjectives, list)

