from word_frequencies.core import WeightedNouns
from word_frequencies.core import WeightedAdjectives
from reservoir_sampling.core import WeightedSample
from word_grid.core import WordGrid

from topic_ideas.core import TopicAssortment


class Test_TopicAssortment:

    def test_canUseOtherPackages(self):


        wn = WeightedNouns()
        nouns = wn.get_weighted_list()
        assert 3030 == len(nouns)

        ws = WeightedSample(nouns, 27)
        sampleNouns = [j[1] for j in ws.extract()]
        assert 27 == len(sampleNouns)


        wn = WeightedAdjectives()
        adjectives = wn.get_weighted_list()
        assert 1035 == len(adjectives)

        ws = WeightedSample(adjectives, 27)
        sampleAdjectives = [j[1] for j in ws.extract()]
        assert 27 == len(sampleAdjectives)


        wg = WordGrid(sampleAdjectives, sampleNouns)
        html = wg.generate()

        with open("output.html", "w", encoding="utf-8") as f:
            f.write(html)
