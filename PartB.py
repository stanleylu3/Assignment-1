import PartA
import sys

def countCommonTokens(file1_tokens: dict, file2_tokens: dict):
    """
    Time Complexity: This method has a time complexity of O(n) since converting each dict
    to a set is based on the size of the dict, or "n", and doing twice is 2n, which simplifies
    to O(n). Comparing the two sets is based on the size of the smaller set, which is still
    O(n) since the set size is based of the dictionary size.

    Returns the number of common tokens between two files.

    :param file1_tokens: A dict containing tokens of first file passed.
    :param file2_tokens: A dict containing tokens of second file passed.
    :return: A list of the common tokens between the two files and the int of the number of
    common tokens.
    """
    tokens1 = set(file1_tokens.keys())
    tokens2 = set(file2_tokens.keys())

    commonTokens = tokens1 & tokens2

    return commonTokens, len(commonTokens)

if __name__ == "__main__":
    try:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

        file1Dict = PartA.computeWordFrequencies(PartA.tokenize(file1))
        file2Dict = PartA.computeWordFrequencies(PartA.tokenize(file2))
        tokens, count = countCommonTokens(file1Dict, file2Dict)
        print(f"Number of Common Tokens: {count}.")
        #print(f"Common Tokens: {tokens}.")
    except IndexError as e:
        print("Needs two files to compare")
    except TypeError as e:
        print("File not found or does not exist.")