def reverse_list(input_list):
    input_list=input_list[::-1]
    return input_list

def count_digits(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return  count