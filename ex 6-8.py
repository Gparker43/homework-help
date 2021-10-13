def main():
    read_file=open('c:\\rnums.dat','r')
    numbers=[]
    for number in read_file:
        numbers.append(int(number))
        print(numbers)
        print('the sum is: ',(added_nums))
        print ('there are',(total_numbers),'numbers in the file')
        print ('the average of all the numbers is: ',(average))

        

def added_numbers():
    added_nums= sum(numbers)
    return added_nums



def total_numbers():
    total_numbers= len(numbers)
    return total_numbers

def average_number():
    average= numbers / total_numbers
    return average



main()
    
        
