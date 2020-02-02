"""
Desc: find the no of matches played by each team for the given no of input
"""


def generate_test_cases():
    pass


def match_count(team_nos, final_list):
    """
    Desc: count the matches between the given n teams

    Args:
        no of teams

    Return:
        no of matches to be played within the given teams
    """
    if team_nos == 1:
        return final_list
    if team_nos % 2 == 0:
        val = int(team_nos//2)
        final_list.append(val)
        return match_count(val, final_list)
    else:
        val = int(team_nos // 2)
        final_list.append(val)
        return match_count(val+1, final_list)


if __name__ == '__main__':
    n = int(input("enter the no of teams \n"))
    if isinstance(n, int):
        final_list = list()
        res = match_count(n, final_list)
        print(sum(res))