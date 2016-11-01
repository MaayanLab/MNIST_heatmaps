def main():


  filename = 'processed_MNIST/random_subsampling/MNIST_100x_random_subsample_0.txt'
  df = load_df_using_clustergrammer(filename)

  import matplotlib.pyplot as plt
  import numpy as np

  print(df.shape)
  cols = df.columns.tolist()

  inst_pixels = df[cols[77]].values

  print(inst_pixels.shape)
  inst_pixels = inst_pixels.reshape((28,28))
  print(inst_pixels.shape)

  max_val = np.amax(inst_pixels)
  print('max val: '+str(max_val))

  # invert image
  inst_pixels = 255 - inst_pixels

  plt.imshow(inst_pixels, cmap='gray')
  plt.show()

def load_df_using_clustergrammer(filename):
  from copy import deepcopy
  from clustergrammer import Network

  net = deepcopy(Network())
  net.load_file(filename)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  return df

main()