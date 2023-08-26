import h5py
f = h5py.File('datasets/TaxiBJ/BJ16_M32x32_T30_InOut.h5')
for ke in f.keys():
    print(ke, f[ke].shape)