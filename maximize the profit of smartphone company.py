""" You are developing a smartphone app. You have a list of potential customers for your app.
Each customer has a budget and will buy the app at your declared price if and only if the price is
le ss than or equal to the customer's budget.
  
 
Y ou want to fix a price so that the revenue you earn from the app is maximized. Find this maximum possible revenue.
 
 
Fo r instance, suppose you have 4 potential customers and their budgets are 30, 20, 53 and 14.
I n this case, the maximum revenue you can get is 60 ."""

# first inpuit(N)  " :- Total number of potential costumers
# now for i in N  ask the budget
# store the bud gets of costumer into list
#sort the list
# mulitply i[0 ] N times
# similary i  [1] N-1 times
# upto i[N]


N = int(input())
x = []
for i in range(1,N+1):
    n = int(input())
    x.append(n)
x = sorted(x)
profits = []
for element in x :
    profits.append(N*element)
    N = N-1
print(max(profits))
