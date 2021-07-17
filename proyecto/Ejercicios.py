def run():
    
    ##List Comprehension
    """"
    squares=[]
    for i in range(1,101):
        if i % 3 !=0:
         squares.append(i**2)
             print(squares)
      
    list_multiples = [number for number in range(1, 100000) if number % 4 == 0 & number % 6 == 0 & number % 9 == 0 ]
    print(list_multiples)
     """
     ##Diccionarios Comprehensions
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**2

    # print(my_dict)

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)


if __name__ == "__main__":
    run()