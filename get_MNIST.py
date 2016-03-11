def main():
  '''
  There are 70,000 digits 
  Each digit is written in a 28x28 image = 784 pixels
  '''


  # overview_mnist_mat()

  # check_digit()

  make_clust()

  # tmp = range(28)
  # tmp = [i - 13.5 for i in tmp]
  # print(tmp)

def make_clust():
  from scipy.io import loadmat 
  import pandas as pd 
  import numpy as np

  mnist_obj = loadmat('custom_data_home/mldata/mnist-original.mat')

  digit_labels = mnist_obj['label']

  print(digit_labels)

  # write matrix to file 
  mat = mnist_obj['data']

  # # 0s 
  # col_num = 0

  # # 3s 
  # col_num = 20500

  # # 7 
  # col_num = 45000


  col_num = 0
  tmp_mat = mat[:,col_num:col_num+100]
  small_mat = tmp_mat
  
  col_num = 20500
  tmp_mat = mat[:,col_num:col_num+100]
  small_mat = np.hstack((small_mat,tmp_mat))

  col_num = 45000
  tmp_mat = mat[:,col_num:col_num+100]
  small_mat = np.hstack((small_mat,tmp_mat))  


  small_size = small_mat.shape

  num_zeros = small_size[1]

  num_pixels = 784


  # write col names 
  col_labels = []
  for i in range(num_zeros):
    if i < 100:
      col_labels.append('Zero-'+str(i))
    if i>= 100 and i < 200:
      col_labels.append('Three-'+str(i))
    if i>=200 and i < 300:
      col_labels.append('Seven-'+str(i))

  # write col category 

  print(len(col_labels))

  row_labels = []
  for i in range(28):
    for j in range(28):
      row_labels.append('pos_'+str(i)+'_'+str(j))


  df = pd.DataFrame(data = small_mat, index=row_labels, columns=col_labels)

  # df.to_csv('example_matrix.txt',sep='\t')

  fw = open('MNIST_labels.txt','w')

  # write names 
  fw.write('\t')
  for inst_name in col_labels:
    fw.write(inst_name+'\t')

  # write categories 
  fw.write('\n\t')
  for inst_name in col_labels:
    inst_cat = inst_name.split('-')[0]
    fw.write(inst_cat+'\t')

  fw.write('\n')

  for i in range(len(row_labels)):
    row_data = small_mat[i,:]

    print(row_data)

    fw.write(row_labels[i]+'\t')

    for inst_data in row_data:
      fw.write(str(inst_data)+'\t')

    fw.write('\n')

  fw.close()


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