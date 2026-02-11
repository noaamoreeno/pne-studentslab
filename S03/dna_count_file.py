#It is correct but the lines are one basis as a whole, not 3 different ones
#reading files
#lines=["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
#print("From variable:", lines)

from dna_count import count_bases #import functions from other codes

f = open("dna.txt", "r") #r means we are reading
#Here we put the code
lines = f.readlines()
f.close() #If you forget to put the close function the file could corrupt when working in other terminals
#another way of opening files
#with open("dna.txt", "r") as f: #with this you don't need to use the close function
    #lines = f.readlines()

total_number = 0
bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for sequence in lines:
    sequence = sequence.strip() #Remove spaces and newline characters at the end of the string
    total_number += len(sequence)
    result = count_bases(sequence)
    for key in result:
        bases[key] += result[key]

print("Total number of bases:", total_number)

for base, count in bases.items():
    print(f'{base}:{count}')