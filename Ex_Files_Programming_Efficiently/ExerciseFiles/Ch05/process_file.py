
def process_file(file):
    this_dict={}
    with open("sonnets/"+file) as f:
        for lineno, line in enumerate(f):
            for word in line.split():
                # strip punctuation, quotes, ..
                clean_word = word.strip(',.:;\'?').lower()
                location = file + '/' + str(lineno+1)
                #print(clean_word, location)
                if clean_word not in this_dict:
                    this_dict[clean_word] = [location]
                else:
                    this_dict[clean_word].append(location)
    return this_dict

def ListMerge(dict1, dict2):
    mydict2 = {**dict1, **dict2}
    for key, value in mydict2.items():
        if key in dict1 and key in dict2:
               mydict2[key] = [value , dict1[key]]
    return mydict2
