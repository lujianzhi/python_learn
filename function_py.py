def find_number(array, number):
    '''
    查找指定数字number是否在数组array中
    '''
    for i in array:
        if (i == number):
            print('有%d' % (number))
            return 'True'
    print(array)
    print("中没有要查找的" + number)
    return 'False'


# help(find_number)
