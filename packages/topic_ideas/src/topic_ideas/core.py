from word_frequencies.core import WeightedNouns
from word_frequencies.core import WeightedAdjectives
from reservoir_sampling.core import WeightedSample
from word_grid.core import WordGrid

class TopicAssortment:

    def __init__(self):
        self.sampleSize = 27;
        self.sampleAdjectives = []
        self.sampleNouns = []

    def sample(self, set):
        ## Select 27 items for 3x3x3 grid.
        ## Items are tuples of form (frequency, word).
        ## Select the word from each tuple.

        assert len(set) >= 27
        ws = WeightedSample(set, self.sampleSize)
        return [j[1] for j in ws.extract()]

    def load_nouns(self):
        self.sampleNouns = self.sample(WeightedNouns().get_weighted_list())

    def load_adjectives(self):
        self.sampleAdjectives = self.sample(WeightedAdjectives().get_weighted_list())

    def write_sample(self, filename):
        assert 27 == len(self.sampleAdjectives)
        assert 27 == len(self.sampleNouns)
        with open(filename, "w", encoding="utf-8") as f:
            for item in self.sampleAdjectives:
                f.write(item + "\n")
            for item in self.sampleNouns:
                f.write(item + "\n")

    def read_sample(self, filename):
        text = []
        with open(filename, "r", encoding="utf-8") as f:
            text = [line for line in f]
        assert len(text) >= 54
        self.sampleAdjectives = text[0:27]
        self.sampleNouns = text[27:54]

    def write_html(self, filename):
        assert 27 >= len(self.sampleAdjectives)
        assert 27 >= len(self.sampleNouns)
        wg = WordGrid(self.sampleAdjectives, self.sampleNouns)
        html = wg.generate()

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)


