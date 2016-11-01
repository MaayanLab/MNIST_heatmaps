def main():


  filename = 'processed_MNIST/random_subsampling/MNIST_20x_random_subsample_0.txt'
  df = load_df_using_clustergrammer(filename)

  save_to = 'MNIST_digits'
  save_images_of_each_number_in_df(df, save_to)

def save_images_of_each_number_in_df(df, save_to):
  '''
  save image of each column digit to img subdirectory 'save_to'
  '''

  import matplotlib.pyplot as plt
  import numpy as np

  print(df.shape)
  cols = df.columns.tolist()

  for inst_col in cols:
    inst_name = inst_col[0].split(': ')[1]
    inst_digit = inst_name.split('-')[0]

    print('save: '+inst_name)

    inst_pixels = df[inst_col].values
    inst_pixels = inst_pixels.reshape((28,28))

    # invert image
    inst_pixels = 255 - inst_pixels

    # save image
    plt.imshow(inst_pixels, cmap='gray')
    plt.axis('off')

    img_name = 'img/' + save_to + '/' + str(inst_digit) + '/' + \
               inst_name + '.png'

    plt.savefig(img_name, bbox_inches='tight')

def load_df_using_clustergrammer(filename):
  from copy import deepcopy
  from clustergrammer import Network

  net = deepcopy(Network())
  net.load_file(filename)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  return df

main()