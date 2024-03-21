import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

# Binomial PMF calculation
def binomial_pmf(k, n, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

def question_a():
    # Define the probabilities
    t = 200  # starting time
    p_c = 0.6 + (2*t - 40) / 1000  # probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000    # probability of a wrong answer
    p_b = 1 - (p_c + p_w)          # probability of leaving blank

    print("Probability of a correct answer (p_c):", p_c)
    print("Probability of a wrong answer (p_w):", p_w)
    print("Probability of leaving blank (p_b):", p_b)
    n = 100  # total number of questions

    # Arrays to store PMF values
    x_values = np.arange(n + 1)
    px = [binomial_pmf(k, n, p_c) for k in x_values]
    py = [binomial_pmf(k, n, p_w) for k in x_values]
    pz = [binomial_pmf(k, n, p_b) for k in x_values]

    # Save plots as PNG files

    # Plot for correct answers
    plt.figure()
    plt.bar(x_values, px, color='green')
    plt.title('PMF of Correct Answers')
    plt.xlabel('Number of Correct Answers')
    plt.ylabel('Probability')
    plt.savefig('pxpmf.png')

    # Plot for wrong answers
    plt.figure()
    plt.bar(x_values, py, color='red')
    plt.title('PMF of Wrong Answers')
    plt.xlabel('Number of Wrong Answers')
    plt.ylabel('Probability')
    plt.savefig('pypmf.png')

    # Plot for blank answers
    plt.figure()
    plt.bar(x_values, pz, color='blue')
    plt.title('PMF of Blank Answers')
    plt.xlabel('Number of Blank Answers')
    plt.ylabel('Probability')
    plt.savefig('pzpmf.png')

def question_b():
    # Initial probabilities at the start of the exam
    t = 200  # Full time available
    p_c = 0.6 + (2 * t - 40) / 1000  # Probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000      # Probability of a wrong answer
    p_b = 1 - (p_c + p_w)            # Probability of leaving a question blank

    n = 100  # Total number of questions
    M = int(input("Enter the score M: "))  # Required score

    # Probability of scoring more than M points
    total_probability = 0
    for correct in range(0, n + 1):
        for wrong in range(0, n - correct + 1):
            net_points = 5*correct - 1.25*wrong 
            if net_points >= M:
                prob_correct = binomial_pmf(correct, n, p_c)
                prob_wrong = binomial_pmf(wrong, n - correct, p_w)
                blank = n - correct - wrong
                prob_blank = binomial_pmf(blank, n - correct - wrong, p_b)
                total_probability += prob_correct * prob_wrong * prob_blank

    print(f"Probability of scoring more than {M} points: {total_probability}")

def question_c():
    # Probabilities with 120 minutes remaining
    t = 120
    p_c = 0.6 + (2*t - 40) / 1000  # Probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000    # Probability of a wrong answer

    # Initial condition
    initial_correct = 20
    initial_wrong = 7
    initial_blank = 4
    total_initial_questions = initial_correct + initial_wrong + initial_blank

    # Probability of the initial condition
    prob_initial_condition = (comb(total_initial_questions, initial_correct) * p_c**initial_correct *
                            comb(total_initial_questions - initial_correct, initial_wrong) * p_w**initial_wrong)

    # Remaining questions
    remaining_questions = 100 - total_initial_questions

    # Current score
    current_score = initial_correct * 5 - (initial_wrong // 4) * 5

    # Required additional score to pass
    required_additional_score = 200 - current_score

    # Calculate the probability of passing given the initial condition
    probability_pass_given_condition = 0
    for correct in range(0, remaining_questions + 1):
        for wrong in range(0, remaining_questions - correct + 1):
            net_points = correct - wrong // 4
            additional_score = net_points * 5
            if additional_score >= required_additional_score:
                prob_correct = comb(remaining_questions, correct) * (p_c ** correct) * ((1 - p_c) ** (remaining_questions - correct))
                prob_wrong = comb(remaining_questions - correct, wrong) * (p_w ** wrong) * ((1 - p_w) ** (remaining_questions - correct - wrong))
                probability_pass_given_condition += (prob_correct * prob_wrong) / prob_initial_condition

    print("Conditional probability of passing the exam (s):", probability_pass_given_condition)



question_b()
