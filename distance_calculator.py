import numpy as np

# calc edit distance between two strings
def calc_distance(str1, str2):
    if len(str1) < len(str2):
        return calc_distance(str2, str1)

    # So now we have len(source) >= len(target).
    if len(str2) == 0:
        return len(str1)

    # We call tuple() to force strings to be used as sequences
    # ('c', 'a', 't', 's') - numpy uses them as values by default.
    str1 = np.array(tuple(str1))
    str2 = np.array(tuple(str2))

    # We use a dynamic programming algorithm, but with the
    # added optimization that we only need the last two rows
    # of the matrix.
    previous_row = np.arange(str2.size + 1)
    for s in str1:
        # Insertion (target grows longer than source):
        current_row = previous_row + 1

        # Substitution or matching:
        # Target and source items are aligned, and either
        # are different (cost of 1), or are the same (cost of 0).
        current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], str2 != s))

        # Deletion (target grows shorter than source):
        current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)

        previous_row = current_row

    return previous_row[-1]

"""
print calc_distance(
    "GACATCCAGATGACCCAGTCTCCATCTTCCGTGTCTGCATCTGTAGGAGACAGAGTCACCATCACTTGTCGGGCGAGTCAGGGTATTAGCAGCTGGTTAGCCTGGTATCAGCAGAAACCAGGGAAAGCCCCTAAGCTCCTGATCTATGCTGCATCCAGTTTGCAAAGTGGGGTCCCATCAAGGTTCAGCGGCAGTGGATCTGGGACAGATTTCACTCTCACCATCAGCAGCCTGCAGCCTGAAGATTTTGCAACTTACTATTGTCAACAGGCTAACAGTTTCCCTCC",
    "GATATTGTGATGACCCAGACTCCACTCTCCTCACCTGTCACCCTTGGACAGCCGGCCTCCATCTCCTGCAGGTCTAGTCAAAGCCTCGTACACAGTGATGGAAACACCTACTTGAGTTGGCTTCAGCAGAGGCCAGGCCAGCCTCCAAGACTCCTAATTTATAAGATTTCTAACCGGTTCTCTGGGGTCCCAGACAGATTCAGTGGCAGTGGGGCAGGGACAGATTTCACACTGAAAATCAGCAGGGTGGAAGCTGAGGATGTCGGGGTTTATTACTGCATGCAAGCTACACAATTTCCTCA"
    )
"""