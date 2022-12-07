# fs = filesystem, wd = working directory

def add_file(fs_root, wd, filesize, filename):
    # cd = current directory
    cd = fs_root
    for folder in wd:
        if folder not in cd:
            cd[folder] = dict()
        cd = cd[folder]
    cd[filename] = filesize

def calc_dir_sizes(dir, path, flat_fs):
    dir_size = 0
    for name, data in dir.items():
        # Leaf node / file
        if isinstance(data, int):
            dir_size += data
        else:
            dir_size += calc_dir_sizes(data, path + "/" + name, flat_fs)
    flat_fs[path] = dir_size
    return dir_size

with open('07.in') as f:
    fs = dict()
    wd = []

    # Parse input
    for line in f.readlines():
        tokens = line.strip().split(' ')
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    wd.clear()
                elif tokens[2] == "..":
                    wd.pop()
                else:
                    wd.append(tokens[2])
        elif tokens[0] == "dir":
            # Do nothing
            pass
        else:
            add_file(fs, wd, int(tokens[0]), tokens[1])

    # Part 1
    flatdirsizes = dict()
    calc_dir_sizes(fs, "/", flatdirsizes)

    small_dir_sizes = sum([x for x in flatdirsizes.values() if x < 100000])
    print("Part 1: ", small_dir_sizes)

    used_space = flatdirsizes["/"]
    free_space = 70000000 - used_space
    required_space = 30000000 - free_space
    print("Part 2: ", min([x for x in flatdirsizes.values() if x >= required_space]))