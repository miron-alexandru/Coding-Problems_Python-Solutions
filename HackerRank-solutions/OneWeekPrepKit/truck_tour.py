# problem link: https://www.hackerrank.com/challenges/truck-tour/problem


# my solution:


def truckTour(petrolpumps):
    n = len(petrolpumps)
    start = 0
    end = 1
    petrol = petrolpumps[start][0] - petrolpumps[start][1]

    while end != start or petrol < 0:
        while petrol < 0 and start != end:
            petrol -= petrolpumps[start][0] - petrolpumps[start][1]
            start = (start + 1) % n
            if start == 0:
                return -1

        petrol += petrolpumps[end][0] - petrolpumps[end][1]
        end = (end + 1) % n

    return start
