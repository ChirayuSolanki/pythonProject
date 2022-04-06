#N teams participate in a league cricket tournament on Mars, where each pair of distinct teams plays each other exactly once.
# Thus, there are a total of (N × (N-1))/2 matches. An expert has assigned a strength to each team,
# a positive integer. Strangely, the Martian crowds love one-sided matches
# and the advertising revenue earned from a match is the absolute value of the difference between the strengths of the two matches.
# Given the strengths of the N teams, find the total advertising revenue earned from all the matches.


#For example, suppose N is 4 and the team strengths for teams 1, 2, 3, and 4 are 3, 10, 3, and 5 respectively. Then
# the advertising revenues from the 6 matches are as follows:

# absolut function


# taking the input of number of teams
N = int(input())
s = [int(i) for i in input().split()][:N]
#matches = int((N*(N-1))/2)
x = []
k = len(s)
for i in range(k-1):
    for j in  range(i+1,k):
        x.append(abs(s[i]-s[j]))
print(sum(x))