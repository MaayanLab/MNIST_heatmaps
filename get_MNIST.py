def main():
  '''
  There are 70,000 digits
  Each digit is written in a 28x28 image = 784 pixels
  '''

  # overview_mnist_mat()

  # check_digit()

  make_clust()

def make_clust():
  from scipy.io import loadmat
  import pandas as pd
  import numpy as np
  # import random
  import math

  mnist_obj = loadmat('custom_data_home/mldata/mnist-original.mat')

  digit_labels = mnist_obj['label'][0]

  print(len(digit_labels))

  label_dict = {}
  label_dict[0] = 'Zero'
  label_dict[1] = 'One'
  label_dict[2] = 'Two'
  label_dict[3] = 'Three'
  label_dict[4] = 'Four'
  label_dict[5] = 'Five'
  label_dict[6] = 'Six'
  label_dict[7] = 'Seven'
  label_dict[8] = 'Eight'
  label_dict[9] = 'Nine'

  num_digit = {}
  num_digit[0] = 0
  num_digit[1] = 0
  num_digit[2] = 0
  num_digit[3] = 0
  num_digit[4] = 0
  num_digit[5] = 0
  num_digit[6] = 0
  num_digit[7] = 0
  num_digit[8] = 0
  num_digit[9] = 0

  col_labels = []
  for i in range(len(digit_labels)):

    inst_label = digit_labels[i]

    inst_count = num_digit[inst_label]

    num_digit[inst_label] = num_digit[inst_label] + 1

    # inst_count = 0
    inst_label = label_dict[inst_label] + '-' + str(inst_count)

    col_labels.append(inst_label)

  print('number of instances of each digit')
  print(num_digit)

  # write matrix to file
  mat = mnist_obj['data']

  # construct row labels: 28x28 pixel image
  row_labels = []
  for i in range(28):
    for j in range(28):
      row_labels.append('pos_'+str(i)+'-'+str(j))

  # keep_cols = ['Zero-0','Zero-1','Zero-2','Zero-3','Zero-4','Zero-5','Zero-6','Zero-7','Zero-8','Zero-9']
  keep_cols = []


  # random.seed(100)
  for inst_digit in label_dict:
    tmp_name = label_dict[inst_digit]

    for i in range(20):
      # tmp = int(math.floor(random.random()*1000))
      tmp = i
      inst_name = tmp_name+'-'+str(tmp)

      keep_cols.append(inst_name)

  df = pd.DataFrame(data = mat, index=row_labels, columns=col_labels)


  df = df[keep_cols]

  # add categories to columns
  ###############################
  new_col_labels = df.columns.tolist()

  tuple_col_labels = []
  for inst_label in new_col_labels:
    # add number name
    inst_name = 'Numbers: ' + inst_label
    # add category name
    inst_cat = 'Digit: ' + inst_label.split('-')[0]
    inst_tuple = ( inst_name, inst_cat )
    tuple_col_labels.append(inst_tuple)

  df.columns = tuple_col_labels

  # add row categories
  ###############################
  new_row_labels = df.index.tolist()
  tuple_row_labels = []

  max_radius = np.sqrt( np.square(28) + np.square(28) )

  for inst_row in new_row_labels:

    # make name
    inst_name = 'Pixels: '+ inst_row

    # make radius category
    pos = inst_row.split('pos_')[1]
    inst_x = int(pos.split('-')[0])
    inst_y = int(pos.split('-')[1])
    inst_radius = max_radius - np.sqrt( np.square(inst_x) + np.square(inst_y) )
    inst_cat = 'Center: '+ str(inst_radius)

    inst_tuple = ( inst_name, inst_cat )

    tuple_row_labels.append(inst_tuple)

  df.index = tuple_row_labels

  print(df.shape)

  df.to_csv('MNIST_labels.txt',sep='\t')

def check_digit():
  from scipy.io import loadmat
  mnist_obj = loadmat('custom_data_home/mldata/mnist-original.mat')

  mat = mnist_obj['data']

  print(mat.shape)

  # 7
  # inst_digit = 45000

  # # 3: 20500
  inst_digit = 20100
  # digit = mat[:,inst_digit]

  # 3: 20500
  # inst_digit = 69000
  digit = mat[:,inst_digit]

  for tmp in range(100):
    print(mnist_obj['label'][0][inst_digit+tmp])

  img_width = 28

  f = open('example_image.txt','w')

  for i in range(img_width):
    f.write('col-'+str(i)+'\t')

  f.write('\n')

  for inst_row in range(img_width):

    img_row =  digit[ inst_row*28: (inst_row+1)*28 ]

    f.write('row-'+str(inst_row))
    for i in range(len(img_row)):

      f.write( str( img_row[i] ) +'\t')

    f.write('\n')



  f.close()

def overview_mnist_mat():
  from scipy.io import loadmat
  mat = loadmat('custom_data_home/mldata/mnist-original.mat')

  print(mat.keys())

  print(type(mat['data']))

  print(mat['data'].shape)

  print('\n\nml_data_descr_ordering')
  print(type(mat['mldata_descr_ordering']))
  print(mat['mldata_descr_ordering'].shape)
  print(mat['mldata_descr_ordering'])

  print('\n\nlabel')
  print(mat['label'].shape)

  print('\n\nglobals')
  print(mat['__globals__'])

def download_mnist_from_server():
  from sklearn.datasets import fetch_mldata

  mnist = fetch_mldata('MNIST original', data_home='custom_data_home')

  print(mnist.shape)

main()