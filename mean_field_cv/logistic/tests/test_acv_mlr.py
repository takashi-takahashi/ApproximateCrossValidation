# coding=utf-8
import unittest
import numpy as np
from numpy.testing import assert_allclose
import csv
from mean_field_cv.logistic.acv_mlr import acv_mlr


class TestAcvMlr(unittest.TestCase):
    def test_calculation(self):
        # read test data
        X = []
        X_reader = csv.reader(open("./sample_data_mlr/dummy_x.csv", "r"))
        for data in X_reader:
            X.append(data)
        X = np.array(X, dtype=np.float64)

        Ycode = []
        Ycode_reader = csv.reader(open("./sample_data_mlr/dummy_Ycode.csv", "r"))
        for data in Ycode_reader:
            Ycode.append(data)
        Ycode = np.array(Ycode, dtype=np.int64)

        wV = []
        wV_reader = csv.reader(open("./sample_data_mlr/dummy_wV.csv", "r"))
        for data in wV_reader:
            wV.append(data)
        wV = np.array(wV, dtype=np.float64)

        desired = [3.8876, 0.7742]
        actual = acv_mlr(wV, X, Ycode, Ycode.shape[1])

        assert_allclose(actual, desired, rtol=1e-3)

    def test_type_checker(self):
        # make ideal dummy data
        N = 10
        M = 20
        p = 4
        wV = np.random.rand(p, N)
        X = np.random.rand(M, N)
        Ycode = np.zeros((M, p))
        for index, row in enumerate(Ycode):
            Ycode[index][np.random.randint(p)] = 1

        self.assertRaises(ValueError, acv_mlr, 0.0, X, Ycode)
        self.assertRaises(ValueError, acv_mlr, wV, 0.0, Ycode)
        self.assertRaises(ValueError, acv_mlr, wV, X, 0.0)
        self.assertRaises(ValueError, acv_mlr, wV, X, Ycode, 2.0)

    def test_shape_checker(self):
        # make ideal dummy data
        N = 10
        M = 20
        p = 4
        wV = np.random.rand(p, N)
        X = np.random.rand(M, N)
        Ycode = np.zeros((M, p))
        for index, row in enumerate(Ycode):
            Ycode[index][np.random.randint(p)] = 1

        self.assertRaises(ValueError, acv_mlr, np.random.rand(1, 2, 3), X, Ycode)
        self.assertRaises(ValueError, acv_mlr, np.random.rand(1), X, Ycode)

        self.assertRaises(ValueError, acv_mlr, wV, np.random.rand(1, 2, 3), Ycode)
        self.assertRaises(ValueError, acv_mlr, wV, np.random.rand(1), Ycode)

        self.assertRaises(ValueError, acv_mlr, wV, X, np.random.rand(1, 2, 3))
        self.assertRaises(ValueError, acv_mlr, wV, X, np.random.rand(1))

    def test_shape_matching_checker(self):
        # make ideal dummy data
        N = 10
        M = 20
        p = 4
        wV = np.random.rand(p, N)
        X = np.random.rand(M, N)
        Ycode = np.zeros((M, p))
        for index, row in enumerate(Ycode):
            Ycode[index][np.random.randint(p)] = 1

        self.assertRaises(ValueError, acv_mlr, np.random.rand(p, N - 1), X, Ycode)
        self.assertRaises(ValueError, acv_mlr, wV, np.random.rand(M, N - 1), Ycode)

        self.assertRaises(ValueError, acv_mlr, wV, np.random.rand(M + 1, N), Ycode)
        self.assertRaises(ValueError, acv_mlr, wV, X, np.random.rand(M + 1, p))

        self.assertRaises(ValueError, acv_mlr, np.random.rand(p + 1, N), X, Ycode)
        self.assertRaises(ValueError, acv_mlr, wV, X, np.random.rand(M, p + 1))


if __name__ == '__main__':
    unittest.main()
