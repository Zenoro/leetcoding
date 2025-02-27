def compress(chars: list[str]) -> int:
    if len(chars) == 1:
        return 1

    chars.append('\0')
    write_idx, prev_idx = 0, 0
    for idx in range(1, len(chars)):
        if chars[idx] == chars[idx-1]:    # last=new
            continue
        else:
            summator = len(chars[prev_idx:idx])
            if summator == 1:
                chars[write_idx] = chars[idx-1]
                write_idx += 1
            else:
                word = chars[idx-1] + str(summator)
                for i in range(len(word)):
                    chars[write_idx+i] = word[i]
                write_idx += len(word)
            prev_idx = idx
    return write_idx

# chars = ["a","a","a","a","a","b"]
# print(compress(chars))

# chars = ["a","a","a","b","b","a","a"]
# print(compress(chars))

# chars = ["a","a","b","b","c","c","c"]
# print(compress(chars))

