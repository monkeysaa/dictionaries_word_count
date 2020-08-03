def print_wordcount(file_to_count):
    """Read a file, return a dictionary that counts each word in file.

    """
    wordcount_dict = {}
    file_string = open(file_to_count).read()
    words = file_string.rstrip().split()
    
    for word in words:
        if word in wordcount_dict:
            value = wordcount_dict.get(word)
            value += 1
            wordcount_dict[word] = value
        else:
            wordcount_dict[word] = 1
    
    for key, value in wordcount_dict.items():
        print(key, value)
        
    return wordcount_dict


print_wordcount("test.txt")