import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
        header=None,
        names=[
            'age', 'workclass', 'fnlwgt', 'education', 'education-num',
            'marital-status', 'occupation', 'relationship', 'race', 'sex',
            'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
        ],
        na_values=' ?', skipinitialspace=True
    )

    df.dropna(inplace=True)

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. % with Bachelor's degree
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. % >50K with advanced education
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced)]
    lower_edu = df[~df['education'].isin(advanced)]

    higher_edu_rich = round(
        (higher_edu['salary'] == '>50K').sum() / len(higher_edu) * 100, 1)

    # 5. % >50K without advanced education
    lower_edu_rich = round(
        (lower_edu['salary'] == '>50K').sum() / len(lower_edu) * 100, 1)

    # 6. Min work hours
    min_hours = df['hours-per-week'].min()

    # 7. % rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_hours]
    rich_min_workers = round(
        (min_workers['salary'] == '>50K').sum() / len(min_workers) * 100, 1)

    # 8. Country with highest % of >50K
    rich_country_df = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country_df = df['native-country'].value_counts()
    rich_percent = (rich_country_df / total_country_df * 100).round(1)
    highest_earning_country = rich_percent.idxmax()
    highest_earning_country_percentage = rich_percent.max()

    # 9. Most popular occupation in India among >50K
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    # Final dictionary
    result = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage_min_hours': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    if print_data:
        for key, value in result.items():
            print(f"{key}: {value}")

    return result
