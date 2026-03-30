#Corcordance
# An alphabetical index of all the words in a text or corpus of texts, 
# showing every contextual occurrence of a word.

# define concordance, open and read file
def concordance(filename):
    counts = {} #dictionary
    file = open(filename,'r')
    for line in file: #read each word in each line
        for word in line.split(): #Splits each line as indiv words
            if word in counts:
                counts[word] += 1 #if word already there once, add count
            else:
                counts[word] = 1 #if just once
    #Output the unique words and their frequencies in alphabetical order
    file.close()
    for word in sorted(counts):
        print(word, counts[word])

def main():
    # Input the filename
    filename = input("Enter the input file name: ")
    concordance(filename) #applies function above

if __name__ == "__main__":
    main()
