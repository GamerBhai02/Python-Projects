"""
This program calculates the Body Mass Index (BMI) based on user input for height, weight, age, and gender.
It categorizes the BMI into various ranges and provides personalized health recommendations accordingly.

The BMI categories are as follows:
- Severely Underweight
- Underweight
- Mildly Underweight
- Healthy
- Overweight
- Obese Class 1 (Moderate)
- Obese Class 2 (Severe)
- Obese Class 3 (Very Severe)

Health recommendations are given based on the BMI and other inputs.
"""

def calculate_bmi(weight, height):
    height = height / 100  # Convert height to meters
    bmi = weight / (height ** 2)  # BMI formula
    return bmi

def get_bmi_category(bmi):
    if bmi <= 16:
        return "Severely Underweight"
    elif 16 < bmi <= 16.9:
        return "Underweight"
    elif 17 <= bmi <= 18.4:
        return "Mildly Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "Obese Class 1 (Moderate)"
    elif 35 <= bmi <= 39.9:
        return "Obese Class 2 (Severe)"
    else:
        return "Obese Class 3 (Very Severe)"

def health_recommendation(bmi, age, gender):
    if bmi <= 18.5:
        return "You may need to focus on gaining weight by improving your diet and speaking with a healthcare professional."
    elif bmi >= 25:
        return "Consider a balanced diet and regular exercise. You may want to consult a healthcare provider for weight management."
    elif 18.5 <= bmi <= 24.9:
        return "You have a healthy weight! Maintain a balanced diet and regular physical activity to stay healthy."
    else:
        return "Please consult a healthcare provider for personalized advice."

def main():
    try:
        height = float(input("Enter your height in centimeters: "))
        weight = float(input("Enter your weight in kilograms: "))
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ").strip().lower()

        if height <= 0 or weight <= 0 or age <= 0:
            print("Please enter valid positive values for height, weight, and age.")
            return

        bmi = calculate_bmi(weight, height)
        print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")

        category = get_bmi_category(bmi)
        print(f"BMI Category: {category}")

        recommendation = health_recommendation(bmi, age, gender)
        print("Health Recommendation:", recommendation)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
