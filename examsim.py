import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.integrate import quad

from scipy.stats import erlang

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

    print("Probability of a correct answer (p_c):", p_c)
    print("Probability of a wrong answer (p_w):", p_w)
    print("Probability of leaving blank (p_b):", p_b)
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
    M = int(input("Enter the score M: "))  # Required score

    # Probability of scoring more than M points
    total_probability = 0
    for correct in range(0, n + 1):
        for wrong in range(0, n - correct + 1):
            net_points = 5*correct - 1.25*wrong
            if net_points > M:
                total_probability += calculate_probabilities(correct, wrong, n - correct - wrong, n, p_c, p_w, p_b)

    print(f"Probability of scoring more than {M} points: {total_probability}")

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

    print("Conditional probability of passing the exam (s):", probability_pass_given_condition)

def question_d():
    M = int(input("Enter the score M: "))  # Required score
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

    print("Conditional probability of passing the exam (s):", probability_pass_given_condition)
    

def question_e():
    n = 100  # Total number of questions
    t = 200  # Full time available
    points_needed = 300
    breaks = [4, 6, 0]  # Break times after each phase
    phases = [(20, 40), (30, 40), (50, 110)]  # (questions, time) for each phase
    probability_less_than_300 = 0
    total_points = 0    # Total points obtained so far
    map_20 = {}
    map_30 = {}
    map_50 = {}

    for i, phase in enumerate(phases):
        questions, time = phase
        print("Questions:", questions, "Time:", time)
        print("Remaining time:", t)
        p_c = 0.6 + (2 * t - 40) / 1000  # Probability of a correct answer
        p_w = 0.2 + (30 - t) / 1000      # Probability of a wrong answer
        p_b = 1 - (p_c + p_w)            # Probability of leaving a question blank

        for correct in range(0, questions + 1):
            for wrong in range(0, questions - correct + 1):
                net_points = correct - wrong // 4
                if net_points < 0:
                    net_points = 0
                net_points = net_points * 5
                if net_points < points_needed: 
                    blank = questions - correct - wrong
                    if questions == 20:
                        map_20[(correct, wrong, blank)] = 5*(correct - wrong//4)
                    elif questions == 30:
                        map_30[(correct, wrong, blank)] = 5*(correct - wrong//4)
                    else:
                        map_50[(correct, wrong, blank)] = 5*(correct - wrong//4)
                    #probability_less_than_300 += calculate_probabilities(correct, wrong, blank, questions, p_c, p_w, p_b)
        
    
    t20 = 200
    t30 = 156
    t50 = 110

    for key20, value20 in map_20.items():
        p_c20 = 0.6 + (2 * t20 - 40) / 1000  
        p_w20 = 0.2 + (30 - t20) / 1000      
        p_b20 = 1 - (p_c20 + p_w20)            
        for key30, value30 in map_30.items():
            p_c30 = 0.6 + (2 * t30 - 40) / 1000
            p_w30 = 0.2 + (30 - t30) / 1000
            p_b30 = 1 - (p_c30 + p_w30)
            for key50, value50 in map_50.items():
                p_c50 = 0.6 + (2 * t50 - 40) / 1000
                p_w50 = 0.2 + (30 - t50) / 1000
                p_b50 = 1 - (p_c50 + p_w50)
                total_points = value20 + value30 + value50
                if total_points < points_needed:
                    probability_less_than_300 += calculate_probabilities(key20[0],key20[1],key20[2],20,p_c20, p_w20, p_b20)
                    probability_less_than_300 += calculate_probabilities(key30[0],key30[1],key30[2],30,p_c30, p_w30, p_b30)
                    probability_less_than_300 += calculate_probabilities(key50[0],key50[1],key50[2],50,p_c50, p_w50, p_b50)

    print("Probability of getting less than 300 points:", probability_less_than_300)


def question_f():
    lambda_1 = 1 / 40  # Rate parameter for phase 1
    x = 25  # Time limit

    # Calculate the probability that phase 1 lasts longer than 25 minutes
    prob = np.exp(-lambda_1 * x)
    print("Probability that phase 1 lasts longer than 25 minutes:", prob)

    # Simulate this process 1000 times
    simulation_times = np.random.exponential(scale=1/lambda_1, size=1000)
    exceeds_25_minutes = simulation_times > x
    probs = []
    counts = np.arange(1, 1001)
    for i in range(1, 1001):
        probs.append(np.mean(exceeds_25_minutes[:i]))


    # Calculate the empirical probability
    empirical_prob = np.mean(exceeds_25_minutes)
    print(f"The empirical probability from the simulation is: {empirical_prob}")
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
    print(f"The probability that the solution time is between 60 and 80 minutes is: {prob_60_80}")

    # Plot the Erlang PDF
    x_values = np.linspace(0, 160, 1000)  # Values for x-axis
    y_values = [erlang_pdf(n, lambda_exp, x) for x in x_values]  # Erlang PDF values

    plt.plot(x_values, y_values, label='Erlang PDF (Custom)')
    plt.fill_between(x_values, y_values, where=((x_values >= 60) & (x_values <= 80)), color='red', alpha=0.3, label='Area between 60 and 80')
    plt.xlabel('Time (minutes)')
    plt.ylabel('Probability Density')
    plt.title('Erlang PDF for the Solution Time of 30 Questions')
    plt.legend()
    plt.grid(True)
    plt.savefig('erlangpdf.png')
    plt.close()

    # Compare with the built-in Erlang distribution from scipy
    erlang_dist = erlang(n, scale=1/lambda_exp)
    prob_60_80_builtin = erlang_dist.cdf(80) - erlang_dist.cdf(60)
    print(f"Built-in Erlang probability: {prob_60_80_builtin}")


question_b()
question_d()