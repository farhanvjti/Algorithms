def find_frnds(p,tup,frnds):
    
    frnds_data = []  
    for data in frnds:            #Make a new list as on manipulating
        lst = [data[0],data[1]]
        frnds_data.append(lst)
                                  #changes will also reflect in original list
    for item in frnds_data:
        if p in item:
            item.remove(p)
            if item[0] not in tup:
                tup += (item[0],)
            else:
                continue
    return tup
            
        
    
def make_teams(frnds_pair,per,pair):

    teams = []     #A list of tuples of person making a team

    people = [i for i in range(1,per+1)]

    for person in people:
        found = False
        for tup in teams:
            if person in tup:
                new_tup = find_frnds(person,tup,frnds_pair)
                teams.remove(tup)
                teams.append(new_tup)
                found = True
        if not found:
            tup = (person,)
            new_tup = find_frnds(person,tup,frnds_pair)
            teams.append(new_tup)
    return teams
    
    
if __name__== '__main__':

    cases = int(input())
    results= []
    for i in range(cases):
        d =[]
        persons, pairs = input().split()
        frnds_pair = []
        for j in range(int(pairs)):
            frnds_pair.append(list(map(int,input().split())))
        bazinga = make_teams(frnds_pair,int(persons),int(pairs))

        doors = len(bazinga)
        d.append(doors)
        ways = 1
        for b in bazinga:
            ways *=len(b)
        d.append(ways)

        results.append(d)
        
    for result in results:
        print (str(result).replace('[','').replace(']','').replace(', ',' '))
        
    
'''
Fire Escape Routes
Problem code: FIRESC
	

    Submit
    My Submissions
    All Submissions

All submissions for this problem are available.

Chef has been constantly expanding his chain of restaurants. It was getting too difficult for him to manage the finances of so many businesses all by himself. So he has opened up a new accounts office and hired people to help him with this task. There are N people working in this building and each one works in a separate cabin. Chef employees are numbered by integers from 1 to N, inclusive. Chef wants to ensure the safety of his employees. He wants to have fire escapes in the building and wants to train the employees to use these by conducting mock drills.

Chef knows that the number of people working in his office can be very large. In order to avoid crowding of a common fire escape route during emergency, Chef has decided to build multiple fire escapes. For the safety of every employee, each cabin has a fire exit which is connected to one of the fire escape routes.

A lot of employees are friends with each other. The friendship is mutual. This means that if employee i is a friend of employee j then employee j is a friend of employee i as well. But friendship is NOT necessarily transitive. This means that if employee i is a friend of employee j AND employee j is a friend of employee k, then employee i and employee k need not necessarily be friends.

If two employees are friends, they do not want to escape through different routes.

This complicates the task for the Chef. As already mentioned, he wants to have the maximum number of fire escape routes to ensure maximum safety. Also, for every escape route, one of the employees using that route needs to be appointed as the fire drill captain. The captain will be responsible for conducting the mock drills and train all the employees using that route. Your task is simple. Given the number of employees and the friendship list, you need to tell the Chef the maximum number of fire escape routes that he can have in the building and the number of ways of selecting the captains for every route. Since the number of ways can be really large, output this value modulo 109 + 7.
Input

The first line of the input contains a single integer T, denoting the number of test cases. The description of T test cases follows. The first line of each test case contains two space-separated integers N and M, denoting the number of employees and the number of friendship relations, respectively. Each of the following M lines contains two space-separated integers i and j, denoting employee i and employee j are friends.
Output

For each test case, output a single line containing two space separated integers, denoting the maximum number of distinct fire escape routes that can be constructed and the number of ways of selecting the captains modulo 109 + 7.
Constraints

    1 ≤ T ≤ 5
    1 ≤ N ≤ 100000 (105)
    0 ≤ M ≤ 100000 (105)
    1 ≤ i, j ≤ N
    i ≠ j
    For any pair of employees i and j such that 1 ≤ i < j ≤ N, at most one pair among (i, j) and (j, i) will appear in the input

Example

Input:
3
4 2
1 2
2 3
5 3
1 2
2 3
1 3
6 3
1 2
3 4
5 6

Output:
2 3
3 3
3 8

Explanation

Example case 1. Here employees 1 and 2 are friends and should share the
same fire escape. Also employees 2 and 3 share the same fire escape.
This means employees 1, 2 and 3 will have a common route. But to maximize
number of routes Chef could assign another route to employee 4 since it is
not a friend of other employee. So we have two escape routes with the
following distribution of employees by routes: {1, 2, 3}, {4}.
Therefore, there are 3 ways to chose drill captains:
(1, 4), (2, 4), (3, 4),
where first element in the pair denotes the captain for the first route
and second element denotes the captain for the second route.

Example case 2. Here the optimal distribution of employees by routes is
{1, 2, 3}, {4}, {5}. Therefore, there are 3 ways to chose drill
captains: (1, 4, 5), (2, 4, 5), (3, 4, 5).

Example case 3. Here the optimal distribution of employees by routes is
{1, 2}, {3, 4}, {5, 6}. Therefore, there are 8 ways to chose drill captains:
(1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (2, 3, 5), (2, 3, 6), (2, 4, 5),
(2, 4, 6).
'''
'''
#In case data is passed as a parameter

from sys import argv
import re

file_name = argv[1]
fp = open(file_name,'r+')

contents = [int(line.strip('\n')) for line in fp]

#print (contents)
'''