from word_frequencies.core import WeightedNouns
from word_frequencies.core import WeightedAdjectives
from reservoir_sampling.core import WeightedSample
from word_grid.core import WordGrid

from topic_ideas.core import TopicAssortment


class Test_TopicAssortment:

    def test_canGenerateGrid(self):

        ta = TopicAssortment()

        ta.load_nouns()
        ta.load_adjectives()
        ta.write_html("html-output.html")

    def test_canGenerateSampledWords(self):

        ta = TopicAssortment()

        ta.load_nouns()
        ta.load_adjectives()
        ta.write_sample("sample-output.html")

    def test_canGenerateGridFromFile(self):

        ta = TopicAssortment()

        ta.load_nouns()
        ta.load_adjectives()
        ta.write_sample("sample-output.html")
        ta.read_sample("sample-output.html")
        ta.write_html("html-output.html")
