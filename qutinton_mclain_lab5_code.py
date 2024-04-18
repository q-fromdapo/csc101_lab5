'''
Author: Quinton McLain
Program Title: T-Shirt Shop
File Description:
This program will help Matthew keep track of the T-shirt sales at his store.
'''

# SHOW STATISTICS FUNCTION
def show_stats(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales):
    print('T-Shirt Style Statistics')
    print(' ')
    print(f'Basic: {style_basic}')
    print(f'Graphic: {style_graphic}')
    print(f'Tour/Band: {style_band}')
    print(' ')
    print('T-Shirt Size Statistics: ')
    print(' ')
    print(f'Small: {size_small}')
    print(f'Medium: {size_medium}')
    print(f'Large: {size_large}')
    print(' ')
    print(' ')
    print(' ')
    print('Total Store Sales: ${:.2f}'.format(total_sales))

# PURCHASE T-SHIRT FUNCTION
def purchase_t_shirt(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales):
    print('Styles:')
    print('1. Basic T-Shirt - $12.99')
    print('2. Graphic T-Shirt - $16.99')
    print('3. Band T-Shirt - $24.99')
    style = get_choice('Choose a style for your T-shirt: ', 1, 3)

    print('Sizes:')
    print('1. Small')
    print('2. Medium (+$2.00)')
    print('3. Large (+$4.00)')
    size = get_choice('Choose a size for your T-shirt: ', 1, 3)

    price = calculate_price(style, size)
    total_sales += price

    if style == 1:
        style_basic += 1
    elif style == 2:
        style_graphic += 1
    elif style == 3:
        style_band += 1

    if size == 1:
        size_small += 1
    elif size == 2:
        size_medium += 1
    elif size == 3:
        size_large += 1

    return style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales

# MENU FUNCTION
def show_menu():
    print('Menu:')
    print('1. Purchase a T-Shirt')
    print('2. Show Statistics')
    print('3. Exit')
    while True:
        choice = input('Choose an option: ')
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return int(choice)
        print('Invalid input. Enter a number between 1 and 3.')

# MAIN FUNCTION
def main():
    style_basic = 0
    style_graphic = 0
    style_band = 0
    size_small = 0
    size_medium = 0
    size_large = 0
    total_sales = 0

    while True:
        choice = show_menu()

        if choice == 1:
            purchase_t_shirt(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales)
        elif choice == 2:
            show_stats(style_basic, style_graphic, style_band, size_small, size_medium, size_large, total_sales)
        elif choice == 3:
            return

# STYLE AND SIZE CHOOSING FUNCTION
def get_choice(choice, min_val, max_val):
    while True:
        choice = input(choice)
        if choice.isdigit():
            choice = int(choice)
            if min_val <= choice <= max_val:
                return choice
        print('Invalid input. Enter a number between {} and {}'.format(min_val, max_val))

# CALCULATE PRICE FUNCTION
def calculate_price(style, size):
    basic_price = 12.99
    graphic_price = 16.99
    band_price = 24.99
    medium_size_fee = 2.00
    large_size_fee = 4.00
    if style == 1:
        price = basic_price
    elif style == 2:
        price = graphic_price
    else:
        price = band_price

    if size == 2:
        price += medium_size_fee
    elif size == 3:
        price += large_size_fee

    return price


main()





