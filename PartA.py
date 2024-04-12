import sys
def tokenize(TextFilePath: str) -> list:
    """
    Time Complexity: This method has a time complexity of O(n) since the time to read data is
    based on how large the file is. Reading bytes, splitting the lines, and appending them to
    the tokenList are all based on how large the file is.

    Takes a text file and returns a list of alphanumeric tokens, independent of capitalization.

    :param TextFilePath: A string that contains a path to a text file.
    :return: A list of tokens in the text file.
    """
    tokenList = []
    temp = ""
    #attempts to open a file with the given filepath
    try:
        with open(TextFilePath, 'r', encoding = 'utf-8') as file:
            while True:
                #read files in chunks of 256 bytes
                data = file.read(256)
                #breaks out of loops when there is no data left to read
                if not data:
                    break

                temp += data
                lines = temp.split('\n')
                temp = lines.pop() if lines else ""

                for line in lines:
                    words = line.split()
                    #adds the words if they are alphanumeric
                    for word in words:
                        #strips non-alphanumeric characters from words
                        result = ''.join(char for char in word if char.isalnum() and char.isascii())
                        if result:
                            tokenList.append(result.lower())
            #processes remaining temp data
            words = temp.split()
            for word in words:
                result = ''.join(char for char in word if char.isalnum() and char.isascii())
                if result:
                    tokenList.append(result.lower())
        return tokenList

    except FileNotFoundError:
        pass
    except UnicodeDecodeError:
        pass
    except OSError as e:
        print(f"OS error: {e}")

def computeWordFrequencies(tokenList: list) -> dict:
    """
    Time Complexity: This method has a time complexity of O(n), since loop will only
    iterate as "n" times based on the length of tokenList.

    Counts the number of occurrences of each token and returns them in a dictionary.

    :param tokenList: list of tokens
    :return: dictionary, maps each token to frequency of occurrences
    """
    frequencies = {}
    #runs through all the tokens in the given list
    for token in tokenList:
        #adds 1 to the counter if the entry exists
        if token in frequencies:
            frequencies[token] += 1
        #creates the k/v pair if entry does not exist
        else:
            frequencies[token] = 1

    return frequencies

def printFrequencies(wordCount: dict):
    """
    Time complexity: This method is O(n log n), since the builtin function sorted()
    in Python has a worse case time complexity of O(n log n).

    Prints out the word frequency count, highest to lowest.

    :param wordCount: dictionary, mapping each token to number of frequencies
    """
    #sorts the dictionary based on the highest frequency word
    sorted_dict = sorted(wordCount.items(), key = lambda x: (-x[1], x[0]))
    for word, freq in sorted_dict:
        print(f"{word} -> {freq}")


if __name__ == '__main__':
    try:
        filePath = sys.argv[1]
        tokens = tokenize(filePath)
        freqCount = computeWordFrequencies(tokens)
        printFrequencies(freqCount)
    except TypeError as e:
        print("File not found or does not exist.")
