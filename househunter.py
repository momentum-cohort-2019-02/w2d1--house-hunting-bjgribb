print("You're finally ready to buy a home...")

total_cost = float(input("How much does your dream home cost? "))
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("What portion of your annual salary are you saving? (as a decimal) "))
r = float(input("What is your annualized savings rate? (as a decimal) "))

current_savings = 0
down_payment = total_cost * 0.25
months = 0

while current_savings < down_payment:

    monthly_savings = (annual_salary * portion_saved / 12)
    current_savings = (current_savings * (r/12)) + monthly_savings + current_savings
    # print(current_savings)
    months += 1

print("It will take you " + str(months) + " months to save enough for your down payment.")

# Took me a long time to conceptualize the counting aspect... i.e. how does months += 1 actually work to count the months?
# What happens when I type Python3 in the terminal? I can't easily get back to my repository? i.e. can't Python3 the file




