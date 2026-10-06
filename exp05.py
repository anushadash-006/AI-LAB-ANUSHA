import math


def alpha_beta(depth, node_index, maximizing_player, values, height, alpha, beta):
    if depth == height:
        return values[node_index]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                height,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                height,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


scores = list(map(int, input("Enter the leaf node values: ").split()))

height = 3

result = alpha_beta(
    0, 0, True, scores, height, -math.inf, math.inf
)

print("The optimal value using Alpha-Beta Pruning is:", result)