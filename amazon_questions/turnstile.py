"""
https://leetcode.com/discuss/interview-question/798231/

amazon go store has turnstile

Time : O(n)
Space : O(n)
"""

from collections import deque


def turnstile(no_customers, arrival, direction):
    inqueue, outqueue = deque([]), deque([])
    cost = 0
    pivot = 0
    result = [-1 for _ in range(no_customers)]
    isout = False
    # process if any of the below condition holds true
    while inqueue or outqueue or pivot<no_customers:
        # process belo condition if we have still customers and customer is present in that point
        # of time
        while pivot<no_customers and arrival[pivot] == cost:
            if direction[pivot] == 1:
                outqueue.append(pivot)
                if cost == 0:
                    isout=True
            else:
                inqueue.append(pivot)
            pivot+=1

        # process if the person wants to exit and the first person done exit or there is no one for entry and first
        # customer didn't exit and there are customers to exit
        if (outqueue and isout) or (not isout and not inqueue and outqueue):
            element = outqueue.popleft()
            result[element] = cost
            cost+=1
            isout=True

        elif inqueue:
            element = inqueue.popleft()
            result[element] = cost
            cost += 1
            isout = False

        else:
            isout = True
            cost+=1

    return result


print(turnstile(4, [0, 0, 1, 5], [0, 1, 1, 0]))
print(turnstile(5, [0, 1, 1, 3, 3], [0, 1, 0, 0, 1]))