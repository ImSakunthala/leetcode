min_value = int(input('Enter Minimum Value:'))

max_value = int(input('Enter Maximum Value'))

result = []

for element in range(min_value, max_value+1):
    
    if element > 1:
        
        for divisor in range (2,element):
            
            if (element%divisor)==0:
                
                break
        else:

            result.append(element)

print ('No. of prime numbers:', len(result))

print (result)
