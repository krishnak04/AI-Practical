tree = [[[5, 1, 2], [8, -8, -9], [9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

def childern(branch, depth, alpha, beta):
    global tree
    global root
    global pruned

    i = 0
    for child in branch:
        if isinstance(child, list):
            (nalpha, nbeta) = childern(child, depth + 1, alpha, beta)

            if depth % 2 == 1:
                beta = min(beta, nalpha)
            else:
                alpha = max(alpha, nbeta)

            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:
            if depth % 2 == 0:
                alpha = max(alpha, child)
            else:
                beta = min(beta, child)

        if alpha >= beta:
            pruned += 1
            break
        if depth == root:
            tree = alpha if root == 0 else beta
        return (alpha, beta)


def alphabeta(in_tree=tree, start=root, upper=-15, lower=15):
    global tree
    global pruned
    global root
    (alpha, beta) = childern(tree, start, upper, lower)

    if start == root:
        beta = alpha

    print("(alpha,beta):", alpha, beta)
    print("Result:", tree)
    print("Time pruned:", pruned)

    return (alpha, beta, tree, pruned)

if __name__ == "__main__":
    alphabeta()


