import PartA
import sys

def countCommonTokens(file1_tokens, file2_tokens):
    tokens1 = set(file1_tokens.keys())
    tokens2 = set(file2_tokens.keys())

    commonTokens = tokens1 & tokens2

    return commonTokens, len(commonTokens)

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    file1Dict = PartA.computeWordFrequencies(PartA.tokenize(file1))
    file2Dict = PartA.computeWordFrequencies(PartA.tokenize(file2))
    tokens, count = countCommonTokens(file1Dict, file2Dict)
    print(f"Number of Common Tokens: {count}.")
    print(f"Common Tokens: {tokens}.")