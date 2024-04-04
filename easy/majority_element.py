def mostFrequent(array):
    max_count = 0
    element_having_most_freq = 0
    for i in range(0, len(array)):
        count = 0
        for j in range(0, len(array)):
            if array[i] == array[j]:
                count += 1
            if count > max_count:
                max_count = count
                element_having_most_freq = array[i]
    return element_having_most_freq
    
array = [2,4,8,3,8,1,8,0]
print(mostFrequent(array))



# faster implementation
def mostFrequent(array):
    # Create a dictionary to store the frequency of each element
    freq_dict = {}
    
    # Iterate through the array and count the occurrences of each element
    for element in array:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    
    # Find the element with the maximum frequency
    max_freq_element = max(freq_dict, key=freq_dict.get)
    
    return max_freq_element

# Test the function
array = [2, 4, 8, 3, 8, 1, 8, 0]
print(mostFrequent(array))
