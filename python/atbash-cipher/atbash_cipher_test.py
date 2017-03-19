import unittest

from atbash_cipher import decode, encode


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class AtbashCipherTest(unittest.TestCase):

    def test_encode_no(self):
        self.assertMultiLineEqual("ml", encode("no"))

    def test_encode_yes(self):
        self.assertMultiLineEqual("bvh", encode("yes"))

    def test_encode_OMG(self):
        self.assertMultiLineEqual("lnt", encode("OMG"))

    def test_encode_O_M_G(self):
        self.assertMultiLineEqual("lnt", encode("O M G"))

    def test_encode_long_word(self):
        self.assertMultiLineEqual("nrmwy oldrm tob", encode("mindblowingly"))

    def test_encode_numbers(self):
        self.assertMultiLineEqual("gvhgr mt123 gvhgr mt",
                                  encode("Testing, 1 2 3, testing."))

    def test_encode_sentence(self):
        self.assertMultiLineEqual("gifgs rhurx grlm",
                                  encode("Truth is fiction."))

    def test_encode_all_things(self):
        plaintext = "The quick brown fox jumps over the lazy dog."
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        self.assertMultiLineEqual(ciphertext, encode(plaintext))

    def test_decode_word(self):
        self.assertMultiLineEqual("exercism", decode("vcvix rhn"))

    def test_decode_sentence(self):
        self.assertMultiLineEqual(
            "anobstacleisoftenasteppingstone",
            decode("zmlyh gzxov rhlug vmzhg vkkrm thglm v")
        )

    def test_decode_numbers(self):
        self.assertMultiLineEqual(
            "testing123testing",
            decode("gvhgr mt123 gvhgr mt")
        )

    def test_decode_all_the_letters(self):
        ciphertext = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        plaintext = "thequickbrownfoxjumpsoverthelazydog"
        self.assertMultiLineEqual(plaintext, decode(ciphertext))

    # additional track specific test
    def test_encode_decode(self):
        self.assertMultiLineEqual(
            "testing123testing",
            decode(encode("Testing, 1 2 3, testing."))
        )


if __name__ == '__main__':
    unittest.main()
