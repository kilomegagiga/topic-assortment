
import heapq

class Test_heapq_module:

    oneTenth = 1.0/10.
    oneSeventh = 1.0/7.
    oneFifth = 1.0/5.
    oneHalf = 1.0/2.

    def test_mustInsertRealNumber(self):
        # priority queue pq
        pq = []
        heapq.heappush(pq, (self.oneSeventh, "a seventh"))
        assert self.oneSeventh == pq[0][0]

