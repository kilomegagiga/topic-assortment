
from word_grid.core import WordGrid

class Test_WordGrid_module:

    def exampleList1(self):
        return [
            "aaa", "aaaa", "aaaaa",
            "bbb", "bbbbb", "bbbbbbb",
            "ccc", "cccccc", "ccccccccc",
            "dddd", "ddddd", "dddddd",
            "eeee", "eeeeee", "eeeeeeee",
            "ffff", "fffffff", "ffffffffff",
            "ggggg", "gggggg", "ggggggg",
            "hhhhh", "hhhhhhh", "hhhhhhhhh",
            "iiiii", "iiiiiiii", "iiiiiiiiiii"
        ]

    def exampleList2(self):
        return [w.upper() for w in self.exampleList1()]

    def test_canBeCreated(self):
        wg = WordGrid([],[])
        assert wg

    def test_handlesExampleLists(self):
        wg = WordGrid(self.exampleList1(), self.exampleList2())
        html = wg.generate()
        assert "<!doctype" == html[:9]

