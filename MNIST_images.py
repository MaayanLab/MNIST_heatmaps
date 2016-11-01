def main():

  # save_MNIST_images_from_all_subsets()

  save_784_pixel_images()

def save_784_pixel_images():

  import numpy as np
  import matplotlib.pyplot as plt

  filename = 'processed_MNIST/random_subsampling/MNIST_20x_random_subsample_0.txt'
  df = load_df_using_clustergrammer(filename)

  rows = df.index.tolist()
  print(len(rows))
  # print(rows)

  mat_size = 28
  mat = np.zeros([mat_size, mat_size])

  # set inst_pixel value to 1
  row_index = 10
  col_index = 20

  mat[row_index, col_index] = 100

  for cross in range(3):
    # add surrounding image
    for i in range(4):
      new_row_index = row_index
      new_col_index = col_index
      if i == 0:
        new_row_index = new_row_index + cross
      if i == 1:
        new_row_index = new_row_index -cross
      if i == 2:
        new_col_index = new_col_index + cross
      if i == 3:
        new_col_index = new_col_index -cross

      if new_row_index > 0 and new_row_index < mat_size:
        if new_col_index > 0 and new_col_index < mat_size:
          mat[new_row_index, new_col_index] = 100

  print(mat.shape)
  print(mat.sum())

  # custom colormap
  from matplotlib.colors import LinearSegmentedColormap
  # pass rgba tuples, zero is transparents
  # cmap = LinearSegmentedColormap.from_list('mycmap', [(0, 'red'), (1, 'yellow')])
  cmap = LinearSegmentedColormap.from_list('mycmap', [(0, (0,0,0,0)), (1, 'yellow')])
  # cmap = LinearSegmentedColormap.from_list('mycmap', [(0, 'white'), (1, 'blue')])

  # save image
  plt.imshow(mat, cmap=cmap)
  plt.axis('off')
  # plt.show()

  img_name = 'tmp.png'

  plt.savefig(img_name, transparent=True, bbox_inches='tight', dpi=20)
  # plt.savefig(img_name)
  plt.cla()

def save_MNIST_images_from_all_subsets():
  '''
  save image of each 'real' digit in each of the MNIST subset files
  '''

  import glob

  all_files = glob.glob('processed_MNIST/random_subsampling/*.txt')

  for filename in all_files:

    save_images_of_each_number_in_file(filename)

def save_images_of_each_number_in_file(filename):

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

    # tuple labels
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

    plt.savefig(img_name, bbox_inches='tight', dpi=3)
    plt.cla()

def load_df_using_clustergrammer(filename):
  from copy import deepcopy
  from clustergrammer import Network

  net = deepcopy(Network())
  net.load_file(filename)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  return df

main()