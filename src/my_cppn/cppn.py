import numpy as np


class CPPN(object):

    def __init__(self, nn):
        self.nn = nn

    def render(self, grid_shape, ranges=None):
        if ranges is None:
            ranges = [(-1., 1.) for _ in range(len(grid_shape))]
        # rectangular coordinates
        inputs = np.meshgrid(
            *[
                np.linspace(low, high, n)
                for n, (low, high) in zip(grid_shape, ranges)
            ]
        )
        indexes_arr = np.array(inputs)
        # radius
        index_r = np.sqrt(np.sum(np.square(indexes_arr), axis=0))
        inputs.append(index_r)
        # bias
        inputs.append(np.ones(indexes_arr.shape[1:]))
        inputs = np.array(inputs)
        y = self.nn.eval(inputs)
        return y
