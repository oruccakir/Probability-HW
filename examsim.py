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


def question_c():
    # Probabilities with 120 minutes remaining
    t = 120
    p_c = 0.6 + (2*t - 40) / 1000  # probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000    # probability of a wrong answer

    # Current state
    correct_so_far = 20
    wrong_so_far = 7
    blank_so_far = 4
    remaining_questions = 100 - (correct_so_far + wrong_so_far + blank_so_far)

    # Current net points
    current_net_points = correct_so_far - wrong_so_far / 4
    current_score = current_net_points * 5

    # Required additional net points to pass
    required_additional_net = (200 - current_score) / 5

    # Calculate the probability of passing
    probability_pass = 0
    for correct in range(0, remaining_questions + 1):
        for wrong in range(0, remaining_questions - correct + 1):
            net_points = correct - wrong / 4
            if net_points >= required_additional_net:
                prob_correct = comb(remaining_questions, correct) * (p_c ** correct) * ((1 - p_c) ** (remaining_questions - correct))
                prob_wrong = comb(remaining_questions - correct, wrong) * (p_w ** wrong) * ((1 - p_w) ** (remaining_questions - correct - wrong))
                probability_pass += prob_correct * prob_wrong

    print("Probability of passing the exam (s):", probability_pass)


question_a()