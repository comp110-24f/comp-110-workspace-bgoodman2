"""concatenation python cq04"""

__author__ = "73045290"


def concat(str1: str, str2: str) -> str:  # defining concat
    """Concatenates two strings."""
    return str1 + str2  # returning the concatentation of strings


# Global variables
word1 = "happy"
word2 = "tuesday"

# Call the concat function
if __name__ == "__main__":
    print(concat(word1, word2))
