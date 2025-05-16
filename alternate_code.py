import pandas as pd

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
    'marital-status', 'occupation', 'relationship', 'race', 'sex', 
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
]
df = pd.read_csv(url, header=None, names=columns, na_values=' ?', skipinitialspace=True)

# Clean the data
df = df.dropna()

# 1. How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()

# 2. What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

# 4. What percentage of people with advanced education make more than 50K?
higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

# 5. What percentage of people without advanced education make more than 50K?
lower_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

# 6. What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# 7. What percentage of people who work the minimum number of hours have a salary of >50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

# 8. What country has the highest percentage of people that earn >50K?
country_stats = (df[df['salary'] == '>50K']['native-country'].value_counts() / 
                df['native-country'].value_counts() * 100)
highest_earning_country = country_stats.idxmax()
highest_earning_country_percentage = round(country_stats.max(), 1)

# 9. Identify the most popular occupation for those who earn >50K in India
top_IN_occupation = df[(df['native-country'] == 'India') & 
                      (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

# Print all results
print("1. Race Count:\n", race_count)
print("\n2. Average age of men:", average_age_men)
print("\n3. Percentage with Bachelors degree:", percentage_bachelors)
print("\n4. Percentage with higher education earning >50K:", higher_education_rich)
print("\n5. Percentage without higher education earning >50K:", lower_education_rich)
print("\n6. Minimum work hours per week:", min_work_hours)
print("\n7. Percentage of minimal workers earning >50K:", rich_percentage)
print("\n8. Country with highest percentage of rich:", highest_earning_country)
print("   Percentage:", highest_earning_country_percentage)
print("\n9. Top occupation in India for >50K earners:", top_IN_occupation)
