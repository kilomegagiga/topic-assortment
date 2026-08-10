
from word_frequencies.word_lists import WeightedNouns

class Test_WeightedNouns:

    def test_mustBeCreatedWithoutErrors(self):
        wn = WeightedNouns()
        nouns = wn.get_weighted_list()
        assert isinstance(nouns, list)
        #assert 3030 == len(nouns)

        
