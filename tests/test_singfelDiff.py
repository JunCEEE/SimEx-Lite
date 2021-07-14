"""Test singfelDiff data"""

from SimExLite.DiffractionData.singfelDiffr import getPatternTotal, getPatternShape, read, iread
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

h5_file = './testFiles/singfel-multi.h5'

# def test_getParameters():
#     params = getParameters(h5_file)
#     if __name__ == "__main__":
#         print(params)
#     assert params['beam']['photonEnergy'] == 4960.0


def test_getPatternTotal():
    npattern = getPatternTotal(h5_file)
    if __name__ == "__main__":
        print(npattern)
    assert npattern == 13


def test_read():
    diffr_patterns = read(h5_file, poissonize=False)
    assert len(diffr_patterns) == 13
    assert np.sum(diffr_patterns) != 0

    if __name__ == "__main__":
        plt.figure()
        plt.imshow(diffr_patterns[0], norm=mpl.colors.LogNorm())
        plt.figure()
        plt.imshow(diffr_patterns[2], norm=mpl.colors.LogNorm())
        plt.colorbar()
        plt.show()


def test_createArray_one():
    diffr_pattern = read(h5_file, index=2, poissonize=False)
    diffr_pattern = read(h5_file, index="2", poissonize=False)
    diffr_patterns = read(h5_file, poissonize=False)
    assert len(diffr_pattern) == 1
    assert np.array_equal(diffr_patterns[2], diffr_pattern[0]) is True

    if __name__ == "__main__":
        plt.figure()
        plt.imshow(diffr_pattern[0], norm=mpl.colors.LogNorm())
        plt.colorbar()
        plt.show()


def test_createArray_partial():
    diffr_patterns = read(h5_file, index="2:5", poissonize=False)
    diffr_pattern = read(h5_file, index=4, poissonize=False)
    assert len(diffr_patterns) == 3
    assert np.array_equal(diffr_patterns[2], diffr_pattern[0]) is True
    if __name__ == "__main__":
        fig, ax = plt.subplots(1, 2)
        im = ax[0].imshow(diffr_patterns[0],
                          norm=mpl.colors.LogNorm(vmin=1e-8, vmax=1e-3))
        divider = make_axes_locatable(ax[0])
        cax = divider.append_axes("right", size="5%", pad=0.1)
        fig.colorbar(im, cax=cax)
        im = ax[1].imshow(diffr_patterns[1],
                          norm=mpl.colors.LogNorm(vmin=1e-8, vmax=1e-3))
        divider = make_axes_locatable(ax[1])
        cax = divider.append_axes("right", size="5%", pad=0.1)
        fig.colorbar(im, cax=cax)
        fig.tight_layout()
        plt.show()


def test_Poission():
    diffr_patterns = read(h5_file, poissonize=True)
    assert np.sum(diffr_patterns) == 0


def test_pattern_shape():
    my_shape = getPatternShape(h5_file)
    my_shape == (81, 81)
    if __name__ == "__main__":
        print(my_shape)


def test_iterator():
    my_iter = read(h5_file, poissonize=True)
    n = 0
    for ix in my_iter:
        n += 1
        pattern = ix
    assert n == 13
    assert pattern.shape == (81, 81)


# def test_SolidAngles():
#     diffr_patterns = singfelDiffr(h5_file)
#     diffr_patterns.solid_angles
#     if __name__ == "__main__":
#         diffr_patterns.plotSolidAngles()

# def test_QMap():
#     diffr_patterns = singfelDiffr(h5_file)
#     diffr_patterns.q_map
#     if __name__ == "__main__":
#         diffr_patterns.plotQMap()

if __name__ == "__main__":
    test_getPatternTotal()
    test_read()
    test_createArray_one()
    test_createArray_partial()
