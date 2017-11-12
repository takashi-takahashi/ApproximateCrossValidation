# coding=utf-8


def prob_multinomial(x):
    """calc softmax probability from weight vectors x

    Args:
        x: M p-dimensional vectors ((M, p)-shape np.float64 object)

    Returns:
        M p-dimensional probability vectors ((M, p)-shape np.float64 object)
    """
    try:
        if len(x.shape) <= 1:
            raise ValueError("unexpected shape of input vectors matrix \n")
        else:
            pass
    except ValueError as e:
        print(e)
        raise

    pass
