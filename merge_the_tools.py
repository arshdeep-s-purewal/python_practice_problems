def merge_the_tools(string, k):
    # import pdb;pdb.set_trace()
    sub_set = k
    s = len(string)
    no_of_sub_strings = int(s/k)
    if s%k == 0:
        temp = 0
        sub_string_unique = ""
        for i in range(0, no_of_sub_strings):
            # print(i)
            # import pdb;pdb.set_trace()
            sub_string = string[temp:sub_set]   #aa
            temp = sub_set
            sub_set = temp + k
            # print(sub_string)
            for j in sub_string:
                # print(j)
                if j not in sub_string_unique:
                    sub_string_unique = sub_string_unique+j
            print(sub_string_unique)
            sub_string_unique = ""
                    
            
                

if __name__ == '__main__':
    # string, k = input(), int(input())
    string = 'aabbbcggjhdf'
    k = 2
    merge_the_tools(string, k)