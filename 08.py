with open("08.in") as f:
	trees = [[int(y) for y in x.strip()] for x in f.readlines()]
	
	w = len(trees[0])
	h = len(trees)
	
    ### Part 1 ###
	visible = [[False for y in x] for x in trees]
	# Trees on the edge of the forest are visible
	visible[0] = [True] * w
	visible[-1] = [True] * w
	for row in visible:
		row[0] = True
		row[-1] = True
	
	for r in range(h):
		tallest = trees[r][0]
		for c in range(1, w):
			tree = trees[r][c]
			if tree > tallest:
				tallest = tree
				visible[r][c] = True
				
		tallest = trees[r][-1]
		for c in range(w-1, 0, -1):
			tree = trees[r][c]
			if tree > tallest:
				tallest = tree
				visible[r][c] = True
				
	for c in range(w):
		tallest = trees[0][c]
		for r in range(h):
			tree = trees[r][c]
			if tree > tallest:
				tallest = tree
				visible[r][c] = True
				
		tallest = trees[-1][c]
		for r in range(h-1, 0, -1):
			tree = trees[r][c]
			if tree > tallest:
				tallest = tree
				visible[r][c] = True
				
	print("Part 1: ", sum([sum(x) for x in visible]))
	
    ### Part 2 ###
	max_vd = 0
	for r in range(h):
		for c in range(w):
				tree = trees[r][c]
				v1=0
				v2=0
				v3=0
				v4=0
				
				while c - (v1+1) >= 0:
					v1 += 1
					if trees[r][c-v1] >= tree:
						break
				while c + (v2+1) < w:
					v2 += 1
					if trees[r][c+v2] >= tree:
						break
				while r - (v3+1) >= 0:
					v3 += 1
					if trees[r-v3][c] >=tree:
						break
				while r + (v4+1) < h:
					v4 += 1
					if trees[r+v4][c] >= tree:
						break
				
				vd = v1*v2*v3*v4
				max_vd = max(max_vd, vd)
	print("Part 2: ", max_vd)