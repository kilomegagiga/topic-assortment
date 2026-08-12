from word_frequencies.core import WeightedNouns
from word_frequencies.core import WeightedAdjectives
from reservoir_sampling.core import WeightedSample
from word_grid.core import WordGrid

from topic_ideas.core import TopicAssortment


class Test_TopicAssortment:

    def test_canGenerateHTML(self):

        ta = TopicAssortment()

        ta.load_nouns()
        ta.load_adjectives()
        ta.write_html("output.html")
