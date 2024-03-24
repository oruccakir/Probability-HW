import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.stats import binom
from scipy.integrate import quad


# Binomial PMF calculation
def binomial_pmf(k, n, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

def calculate_probabilities(correct, wrong, blank, n, p_c, p_w, p_b):
    return comb(n, correct) * (p_c**correct) * comb(n - correct, wrong) * (p_w**wrong) * comb(n - correct - wrong, blank) * (p_b**blank)

def question_a():
    # Define the probabilities
    t = 200  # starting time
    p_c = 0.6 + (2*t - 40) / 1000  # probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000    # probability of a wrong answer
    p_b = 1 - (p_c + p_w)          # probability of leaving blank

    n = 100  # total number of questions

    # Arrays to store PMF valu           es
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
    M = int(input())  # Required score

    # Probability of scoring more than M points
    total_probability = 0
    for correct in range(0, n + 1):
        for wrong in range(0, n - correct + 1):
            net_points = 5*correct - 1.25*wrong
            if net_points > M:
                total_probability += calculate_probabilities(correct, wrong, n - correct - wrong, n, p_c, p_w, p_b)

    print(f"mtMor400: {total_probability}")
    return M

def question_c():
    # Probabilities with 120 minutes remaining
    t = 120
    p_c = 0.6 + (2*t - 40) / 1000  # Probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000    # Probability of a wrong answer
    p_b = 1 - (p_c + p_w)          # Probability of leaving a question blank

    # Initial condition
    initial_correct = 20
    initial_wrong = 7
    initial_blank = 4
    total_initial_questions = initial_correct + initial_wrong + initial_blank
    n = 100
    
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
            blank = remaining_questions - correct - wrong
            if additional_score >= required_additional_score:
                probability_pass_given_condition += calculate_probabilities(correct,wrong,blank,remaining_questions,p_c,p_w,p_b)

    print("s:", probability_pass_given_condition)

def question_d(M):
    n = 100  # Total number of questions
     # Initial probabilities at the start of the exam
    t = 200  # Full time available
    p_c = 0.6 + (2 * t - 40) / 1000  # Probability of a correct answer
    p_w = 0.2 + (30 - t) / 1000      # Probability of a wrong answer
    p_b = 1 - (p_c + p_w)            # Probability of leaving a question blank
    probability_pass_given_condition = 0
    for correct in range(0, n + 1):
        for wrong in range(0, n - correct + 1):
            net_points = correct - wrong // 4
            net_points = net_points * 5
            blank = n - correct - wrong
            if blank >= 8 and net_points > M:  # Skip if less than 8 questions are left blank
                probability_pass_given_condition += calculate_probabilities(correct,wrong,blank,n,p_c,p_w,p_b)
            
    divider = 0
    for i in range(0, 8):
        divider += comb(n,i)*(p_b**i)*((1-p_b)**(n-i))
    divider = 1 - divider
    print("news:", probability_pass_given_condition/divider)


def phase_probability(questions, t, correct, incorrect,blank):
    pc = 0.6 + (2 * t - 40) / 1000
    pw = 0.2 + (30 - t) / 1000
    pb = 1 - pc - pw

    # Binomial probabilities for correct and incorrect answers
    prob_correct = binom.pmf(correct, questions, pc)
    prob_incorrect = binom.pmf(incorrect, questions - correct, pw)
    prob_blank = binom.pmf(blank, questions - correct - incorrect, pb)

    # Return combined probability
    return prob_correct * prob_incorrect*prob_blank


def compute_score(correct, incorrect):
    net_correct = correct - incorrect // 4
    return max(net_correct, 0) * 5

def question_e():
    total_prob = 0
    probs1 = []
    probs2 = []
    probs3 = []

    for correct1 in range(21):
        for incorrect1 in range(21 - correct1):
            blank1 = 20 - correct1 - incorrect1
            probs1.append([phase_probability(20, 200, correct1, incorrect1, blank1),compute_score(correct1, incorrect1)])
    
    for correct2 in range(31):
        for incorrect2 in range(31 - correct2):
            blank2 = 30 - correct2 - incorrect2
            probs2.append([phase_probability(30, 156, correct2, incorrect2, blank2),compute_score(correct2, incorrect2)])
    
    for correct3 in range(51):
        for incorrect3 in range(51 - correct3):
            blank3 = 50 - correct3 - incorrect3
            probs3.append([phase_probability(50, 110, correct3, incorrect3, blank3),compute_score(correct3, incorrect3)])
    # Iterate through all combinations for each phase
    for prob1,score1 in probs1:
        for prob2, score2 in probs2:
            for prob3, score3 in probs3:
                score = 0
                score += score1 + score2 + score3
                if score < 300:
                    total_prob += prob1 * prob2 * prob3

    print("It300:", total_prob)

def question_f():
    lambda_1 = 1 / 40  # Rate parameter for phase 1
    x = 25  # Time limit

    # Calculate the probability that phase 1 lasts longer than 25 minutes
    prob = np.exp(-lambda_1 * x)
    print("p1m25:", prob)

    # Simulate this process 1000 times
    simulation_times = np.random.exponential(scale=1/lambda_1, size=1000)
    exceeds_25_minutes = simulation_times > x
    probs = []
    counts = np.arange(1, 1001)
    for i in range(1, 1001):
        probs.append(np.mean(exceeds_25_minutes[:i]))


    # Calculate the empirical probability
    plt.plot(counts, probs, label='Count Probability Function')
    plt.xlabel('Number of Simulations')
    plt.xlim(0, 1000)
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Time Spent in Phase 1')
    plt.legend()
    plt.savefig('countprob.png')
    plt.close()


# Define the Erlang PDF function
def erlang_pdf(n, lambda_exp, x):
    return (lambda_exp**n) * (x**(n-1)) * np.exp(-lambda_exp * x) / np.math.factorial(n-1)

def question_g():
    # Define the parameters for the Erlang distribution
    n = 2  # Because we have the sum of two exponential random variables
    lambda_exp = 1/40.0  # The rate parameter of the exponential distribution
    # Calculate the probability between 60 and 80 minutes using the custom Erlang PDF
    prob_60_80, _ = quad(lambda x: erlang_pdf(n, lambda_exp, x), 60, 80)
    print(f"b6080: {prob_60_80}")

    # Plot the Erlang PDF
    x_values = np.linspace(0, 160, 1000)  # Values for x-axis
    y_values = [erlang_pdf(n, lambda_exp, x) for x in x_values]  # Erlang PDF values

    plt.plot(x_values, y_values, label='Erlang PDF (Custom)')
    plt.fill_between(x_values, y_values, where=((x_values >= 60) & (x_values <= 80)), color='red', alpha=0.3, label='Area between 60 and 80')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Probability Density')
    plt.ylim(0, 0.01)
    plt.title('Erlang PDF for the Solution Time of 30 Questions')
    plt.legend()
    plt.grid(True)
    plt.savefig('erlangpdf.png')
    plt.close()




question_a()
M = question_b()
question_c()
question_d(M)
question_e()
question_f()
question_g()