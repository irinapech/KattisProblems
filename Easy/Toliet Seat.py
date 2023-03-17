preferences = input()

def up_or_dowm_policy_adjustment(policy_condition):
    adjustments = 0
    for i in range(1, len(preferences)):
        if i == 1 and preferences[1] != preferences[0]:
            adjustments += 1
        if i == 1 and preferences[1] != policy_condition:
            adjustments += 1
        elif preferences[i] != policy_condition:
            adjustments += 2
    return adjustments

def whatever_policy():
    adjustments = 0
    for i in range(1, len(preferences)):
        if preferences[i] != preferences[i - 1]:
            adjustments += 1
    return adjustments

print(up_or_dowm_policy_adjustment('U'))
print(up_or_dowm_policy_adjustment('D'))
print(whatever_policy())