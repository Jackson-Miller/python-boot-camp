from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
biddingResults = []
moreBidders = True

while moreBidders:
    print(logo)
    userName = input("What is your name?: ")
    userBid = int(input("What is your bid?: $"))

    current_bid = {
        "Name": userName,
        "Amount": userBid
    }

    biddingResults.append(current_bid)


    userMoreBids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if userMoreBids == "no":
        moreBidders = False
        print(userMoreBids)
    else:
        clear()

highBid = 0
highBidder = ""
for i in biddingResults:
    if i["Amount"] > highBid:
        highBid = i["Amount"]
        highBidder = i["Name"]

print(f"The winner is {highBidder} with a bid of ${highBid}")