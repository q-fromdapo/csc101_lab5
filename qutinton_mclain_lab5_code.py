'''
Author: Quinton McLain
Program Title: T-Shirt Shop
File Description:
The program will help Matthew keep track of the T-shirt sales at his stoes.
'''

#CONSTANT BASE PRICES AND ADDITIONAL COSTS
basic_price = 12.99
graphic_price = 16.99
band_price = 24.99
medium_size_fee = 2.00
large_size_fee = 4.00

def show_stats(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales)
  print('T-Shirt Style Statistics')
  print(' ')
  print(f'Basic: {style_basic}')
  print(f'Graphic: {style_graphic}')
  print(f'Tour/Band: {style_band}')
  print(f' ')
  print('T-Shirt Size Statistics')
  print(' ')
  print(f'Small: {size_small}')
  print(f'Medium: {size_medium}')
  print(f'Large:{size_large}')
  print(' ')
  print(' ')
  print(' ')
  print(f'Total Store Sales: ${total_sales:.2f}')

#PURCHASE T-SHIRT FUNCTION
def purchase_t_shirt(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales):
  #FINISH PURCHASE FUNC
