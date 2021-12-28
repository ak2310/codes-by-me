def get_tuples():
    tuples = int(input('Enter number of tuples: '))
    i = 0
    list_tuples = []
    while i < tuples:
        list_item = []
        count = 0
        tuple_elem = create_tuple()
        for item in tuple_elem:
            try:
                count += int(item)
            except:
                continue
        tuple_cat = tuple_elem[0]
        list_item.append(tuple_cat)
        list_item.append(count)
        list_tuples.append(tuple(list_item))
        i += 1
    return tuple(list_tuples)

def create_tuple():
    list_len = int(input('Enter number items of tuple: '))
    i = 0
    list_elem = []
    while i < list_len:
        list_item = input('Enter tuple item: ')
        list_elem.append(list_item)
        i += 1
    tuple_elem = tuple(list_elem)
    return tuple_elem

def main():                                          # Call main function
    result = get_tuples()
    print(result)

if __name__ == '__main__':
    main()