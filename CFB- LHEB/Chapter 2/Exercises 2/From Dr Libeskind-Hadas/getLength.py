def getLenth(DNAlist, length):
    output = []
    for seq in DNAlist:
        if len(seq) == length:
            output.append(seq)  # or output = output + [seq]
    return output