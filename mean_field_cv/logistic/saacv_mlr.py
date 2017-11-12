# coding=utf-8


def saacv_mlr(wV, X, Ycode, Np):
    """ A further simplified approximation of
    a leave-one-out estimator of predictive likelihood
    for multinomial logistic regression with l1 regularization[1]

    Compute and return an very simplified approximation of
    a leave-one-out estimator (LOOE) and its standard error
    of predictive likelihood for multinomial logistic regression
    penalized by l1 norm.

    Args:
        wV:
        X:
        Ycode:
        Np:

    Returns:
        LOOE, ERR (float, float)

    References:
        [1]: T. Obuchi and Y. Kabashima, XXXXXXXXXXXX
    """

    LOOE = 0.0
    ERR = 0.0

    return LOOE, ERR
