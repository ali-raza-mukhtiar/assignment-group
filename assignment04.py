# Task 1 — Scholarship Eligibility

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
athlete = input("Are you a national-level athlete? (yes/no): ")

if (marks >= 85 and attendance >= 80) or athlete.lower() == "yes":
    print("Scholarship Granted")
else:
    print("Scholarship Denied")


# Task 2 — Smart Home Heater

temperature = int(input("Enter temperature: "))
humidity = int(input("Enter humidity: "))
manual = input("Did user manually activate heater? (yes/no): ")

if (temperature < 18 and humidity > 40) or manual.lower() == "yes":
    print("Heater ON")
else:
    print("Heater OFF")


# Task 3 — E-commerce Coupon

purchased = int(input("Enter number of purchased items: "))
total_bill = int(input("Enter total bill: "))
premium = input("Are you a premium member? (yes/no): ")

if (purchased > 3 and total_bill > 10000) or premium.lower() == "yes":
    print("Coupon Activated")
else:
    print("No Coupon Available")


# Task 4 — Flight Boarding

ticket = input("Do you have a valid ticket? (yes/no): ")
passport = input("Do you have a valid passport? (yes/no): ")
vip = input("Are you a VIP passenger? (yes/no): ")

if (ticket.lower() == "yes" and passport.lower() == "yes") or vip.lower() == "yes":
    print("Boarding Allowed")
else:
    print("Boarding Denied")


# Task 5 — Insurance Premium Offer

age = int(input("Enter age: "))
health_score = int(input("Enter health score: "))
premium_plan = input("Did you choose premium plan? (yes/no): ")

if ((age >= 25 and age <= 50) and health_score > 70) or premium_plan.lower() == "yes":
    print("Premium Offered")
else:
    print("Premium Not Offered")


# Task 6 — Exam Retake Decision

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
missed_exam = input("Did student miss final exam? (yes/no): ")

if (marks < 40 and attendance < 70) or missed_exam.lower() == "yes":
    print("Retake Required")
else:
    print("No Retake Needed")


# Task 7 — Loyalty Discount

purchases = int(input("Enter number of purchases: "))
total_spent = int(input("Enter total spent: "))
member = input("Enter membership type (Gold/Normal): ")

if (purchases > 10 and total_spent > 50000) or member.lower() == "gold":
    print("Loyalty Discount Applied")
else:
    print("No Discount")
