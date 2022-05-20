# Have the function LetterCount(str) take the str parameter being passed 
# and return the first word with the greatest number of repeated letters. 
# For example: "Today, is the greatest day ever!" should return greatest 
# because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. 
# If there are no words with repeating letters return -1. Words will be separated by spaces.

def LetterCountI(str) :
    arr = str.split(" ")
    l = len(arr)
    count = 0
    word = "-1"
    for i in range( l):
        for a in range(len(arr[i])):
            countNew = 0
            b = a + 1
            for b in range (len(arr[i])):
                if arr[i][a] == arr[i][b]:
                    countNew += 1
            
            if (countNew > count):
                count = countNew
                word = arr[i]
    return word

if __name__ == "__main__":
    str = input("Enter ur value")
    print(LetterCountI(str))
