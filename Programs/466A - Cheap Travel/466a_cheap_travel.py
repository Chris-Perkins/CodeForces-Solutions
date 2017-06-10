# Description of the problem can be found at http://codeforces.com/problemset/problem/466/A

num_rides, num_rides_ticket, price_one_ticket, price_mult_ticket = map(int, input().split())

num_mult_tickets = num_rides // num_rides_ticket

print(min(num_rides * price_one_ticket, 
          num_mult_tickets * price_mult_ticket + (num_rides - num_mult_tickets * num_rides_ticket) * price_one_ticket,
          (num_mult_tickets + 1) * price_mult_ticket))