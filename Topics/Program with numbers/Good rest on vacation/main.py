days = int(input())
food = int(input()) * days
flight = int(input()) * 2
hotel = int(input()) * (days - 1)

total = food + flight + hotel
print(total)
