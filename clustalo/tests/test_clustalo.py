import unittest

class TestClustalo(unittest.TestCase):
    def test_input_validation(self):
        from clustalo import clustalo, DNA, PROTEIN

        with self.assertRaises(ValueError):
            clustalo( { 1 : "GATTACA" })

        with self.assertRaises(ValueError):
            clustalo( { "A" : "GATTACAX" })

        with self.assertRaises(ValueError):
            clustalo( { "A" : "TESTTEST" })

        clustalo( { "A" : "GATTACA" })
        clustalo( { "A" : "GATTACAN" })

        clustalo( { "A" : "TESTTEST" }, seqtype=PROTEIN)

    def test_alignment(self):
        from clustalo import clustalo, DNA, PROTEIN

        result = clustalo( { "A" : "GATTACA", "B" : "GATTACANN" })

        self.assertEqual(result["A"], "GATTACA--")
        self.assertEqual(result["B"], "GATTACANN")
