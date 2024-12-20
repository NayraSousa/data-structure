from collections import deque

def permutation(word):
    queue = deque([("", word)])

    while queue:

        prefix, remaining = queue.popleft()

        if not remaining:
            print(prefix)
        else:
            for i in range(len(remaining)):
                newPrefix = prefix + remaining[i]
                newRemaining = remaining[:i]+remaining[i+1:]
                queue.append((newPrefix, newRemaining))

permutation('ABC')
