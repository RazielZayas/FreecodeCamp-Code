import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    print(df.info())  # Muestra información sobre el DataFrame

    # How many of each race are represented in this dataset?
    race_count = df["race"].value_counts()  # Cuenta la cantidad de cada raza

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)  # Calcula edad promedio de hombres

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df["education"] == "Bachelors"]) / len(df)) * 100, 1)

    # Percentage of people with advanced education making more than 50K
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Percentage with salary >50K
    higher_ed_above_50k = len(higher_education[higher_education["salary"] == ">50K"])
    lower_education_above_50k = len(lower_education[lower_education["salary"] == ">50K"])

    higher_education_rich = round((higher_ed_above_50k / len(higher_education)) * 100, 1)
    lower_education_rich = round((lower_education_above_50k / len(lower_education)) * 100, 1)

    # Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of people who work the minimum number of hours per week and earn >50K
    num_min_workers = len(df[df["hours-per-week"] == min_work_hours])
    num_min_workers_above_50k = len(df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")])

    if num_min_workers > 0:  # Evita la división por cero
        rich_percentage = round((num_min_workers_above_50k / num_min_workers) * 100, 1)
    else:
        rich_percentage = 0

    # Country with the highest percentage of people earning >50K
    country_percentage = (df[df["salary"] == ">50K"]["native-country"].value_counts() /
                          df["native-country"].value_counts()) * 100
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # Most popular occupation for those earning >50K in India
    top_IN_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# This code will only run when executed directly
if __name__ == "__main__":
    calculate_demographic_data()

