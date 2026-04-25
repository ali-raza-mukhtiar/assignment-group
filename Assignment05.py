# Assignment 03

# 1. Shopping Discount
price = 3200
discount = 450

final_price = price - discount
print("Final Price:", final_price)


# 2. Bill Calculator
item1 = 1200
item2 = 850
item3 = 430

total_bill = item1 + item2 + item3
average_price = total_bill / 3

print("Total Bill:", total_bill)
print("Average Price:", average_price)


# 3. String Cleaning Task
text = " data science is amazing "

clean_text = text.strip()
upper_text = clean_text.upper()
final_text = clean_text.replace("amazing", "powerful")

print("Removed Spaces:", clean_text)
print("Uppercase:", upper_text)
print("Replaced Text:", final_text)


# 4. Username Formatter
name = "Faisal Amin"

username = name.lower().replace(" ", "_")
print("Final Username:", username)


# 5. Name Formatter
name = "MuhammadFaisal"

first_name = name[:8]
last_name = name[8:]

print("First Name:", first_name)
print("Last Name:", last_name)


# 6. Email Generator
name = "Faisal Amin"

email = name.lower().replace(" ", ".") + "@gmail.com"
print("Generated Email:", email)


# 7. String Analysis Task
text = "MachineLearning"

length = len(text)
first_part = text[:7]
last_part = text[-8:]

print("Length:", length)
print("First 7 Characters:", first_part)
print("Last 8 Characters:", last_part)


# 8. Product Code Generator
product = "LaptopDell"

first_three = product[:3]
last_four = product[-4:]

product_code = first_three + last_four

print("Product Code:", product_code)


# 9. String Transformer
sentence = "python programming language"

upper_sentence = sentence.upper()
replaced_sentence = sentence.replace("python", "AI")
programming_word = sentence[7:18]

print("Uppercase:", upper_sentence)
print("Replaced Sentence:", replaced_sentence)
print("Extracted Word:", programming_word)


# 10. Reverse & Style
text = "DataScience"

reverse_text = text[::-1]
upper_reverse = reverse_text.upper()

print("Reversed String:", reverse_text)
print("Uppercase Reverse:", upper_reverse)
