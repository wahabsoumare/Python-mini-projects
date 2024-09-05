import sys
import os
def read_words(filename) :
    words_list = []
    with open(filename, 'r') as fileread :
        for line in fileread:
            line = line.strip().upper()
            if len(line) >= 3 :
                words_list.append(line)
    print(f"Nombre de mots lu : {len(words_list)}")
    return words_list

def read_sequence(filename) :
    dict_sequence = {}
    with open(filename, 'r') as fileread :
        for line in fileread :
            if line.startswith('>') :
                id = line.split('|')[1]
                dict_sequence[id] = ''
            else :
                dict_sequence[id] += line.strip()
    print(f"Nombre de sequences lues : {len(dict_sequence)}")
    return dict_sequence

def search_words_in_proteome(words_list, dict_sequence) :
    found_word_dict = {}
    for word in words_list :
        seq_count = 0
        for prot_id in dict_sequence :
            if word in dict_sequence[prot_id] :
                seq_count += 1
        if seq_count != 0 :
            found_word_dict[word] = seq_count
            print(f"{word} trouve dans {seq_count} sequence(s) du proteome")
    print(f"Nombre de mots trouves : {len(found_word_dict)}")
    return found_word_dict

def find_most_frequent_words(words_list) :
    maxi = max(words_list.values())
    for word in words_list:
        if words_list[word] == maxi :
            print(f"Le mot le plus frequent est {word} trouve dans {maxi} sequences")


if __name__ == "__main__" :
    if len(sys.argv) < 3 :
        print("Assurez vous de renseigner les fichieers necessaires")
        sys.exit(0)
    else :
        filename = sys.argv[1]
        filesequence = sys.argv[2]
        if not (os.path.exists(filename) and os.path.exists(filesequence)) :
            print("Imposible de trouver les fichiers requis")
            sys.exit(0)
        else :
            dict_sequence = read_sequence(filesequence)
            words_list = read_words(filename)
            words_found = search_words_in_proteome(words_list, dict_sequence)
            find_most_frequent_words(words_found)