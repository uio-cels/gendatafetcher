import unittest
from sequences import get_sequence


class TestSequences(unittest.TestCase):
    def test_get_ucsc_sequence(self):
        seq = get_sequence("chr11_KI270831v1_alt", 400, 410)
        correct = "gtcttttttct"
        #print("Got sequence " + seq)
        self.assertEqual(correct, seq, "%s is not equal to the sequence fetched from ucsc (%s" % (correct, seq))


if __name__ == "__main__":
    unittest.main()
