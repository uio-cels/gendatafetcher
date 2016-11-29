import unittest
from sequences import get_sequence
import genes

class TestSequences(unittest.TestCase):
    def test_get_ucsc_sequence(self):
        seq = get_sequence("chr11_KI270831v1_alt", 400, 410)
        correct = "gtcttttttct"
        #print("Got sequence " + seq)
        self.assertEqual(correct, seq, "%s is not equal to the sequence fetched from ucsc (%s" % (correct, seq))


class TestGenes(unittest.TestCase):
    def test_get_gene(self):
        gene = genes.get_gene("uc011jmc.2")
        self.assertTrue(3016876 in gene["exonStarts"], "Gene uc011jmc.2 should have exonStart 3016876")
        self.assertTrue(len(gene["exonStarts"]) == 6, "Gene uc011jmc.2 should have 6 exonStarts")


if __name__ == "__main__":
    unittest.main()
