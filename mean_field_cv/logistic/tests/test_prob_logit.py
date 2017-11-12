# coding=utf-8
import unittest
import numpy as np
import mean_field_cv.logistic.prob_logit as prob_logit
from numpy.testing import assert_almost_equal, assert_array_almost_equal_nulp, assert_allclose


class TestProbLogit(unittest.TestCase):
    def test_calculation(self):
        """ test calculation accuracy """
        x = np.linspace(1, 10, 10)
        input_vector = -1.0 * np.log(
            x
        )

        expected = np.concatenate(
            (
                (x / (1 + x)).reshape(x.shape[0], 1),
                (1.0 / (1.0 + x)).reshape(x.shape[0], 1)
            ),
            axis=1
        )

        actual = prob_logit.prob_logit(input_vector)
        try:
            assert_allclose(actual, expected, rtol=1e-10)
        except AssertionError as e:
            print(e)
            for num in range(expected.shape[0]):
                print("### content ")
                print(actual[num], expected[num])

    def test_type_check(self):
        """ test type_check function """
        x = np.array(1.)
        self.assertRaises(ValueError, prob_logit.prob_logit, x)


if __name__ == '__main__':
    unittest.main()
