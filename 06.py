def sliding_window(seq_len):
    with open('06.in') as f:
        stream = f.readline().rstrip()
        # Start index of the sliding window
        start = 0
        # Char -> last seen index
        last_seen = dict()
        
        # Scan through the list
        # When we find a duplicate in the window, move the start of the window to 1 past the earlier occurence
        # We have our answer when we reach the end of the window
        for i, c in enumerate(stream):
            if c in last_seen and start <= last_seen[c]:
                # Duplicate char in the window, move the window
                start = last_seen[c] + 1
            elif start + (seq_len - 1) == i:
                # End of window, didn't see any duplicates 
                return i + 1
            last_seen[c] = i

def set_size(seq_len):
    with open('06.in') as f:
        stream = f.readline().rstrip()
        for i in range(seq_len, len(stream) - 1):
            if len(set(stream[i-seq_len : i])) == seq_len:
                return i



print("Part 1 sliding window: ", sliding_window(4))
print("Part 1 set size: ", set_size(4))
print("Part 2 sliding window: ", sliding_window(14))
print("Part 2 set size: ", set_size(14))