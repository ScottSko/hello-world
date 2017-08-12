years = int(input("How many years? "))
total_rainfall = 0
total_months = years * 12

for x in range(years):
    for y in range(12):
        rainfall = int(input("How many inches of rainfall for this month? "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / total_months
print("There were a total of", total_months, "months for this calculation.")
print("The total amount of rainfall was ", total_rainfall, " inches.", sep='')
print("There was an average of", average_rainfall, "inches of rainfall per month.")