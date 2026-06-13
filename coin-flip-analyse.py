import matplotlib.pyplot as plt
import numpy as np

def coin_flip_experiment():
    coin1 = ["Heads", "Tails"]
    coin2 = ["Heads", "Tails"]

    coin1_result = np.random.choice(coin1)
    coin2_result = np.random.choice(coin2)

    if coin1_result == "Heads" and coin2_result == "Heads":
        return 1
    else:
        return 0

num_trials = 1000
prop = []
flips = []
two_heads_counter = 0

for flip in range(num_trials):
    two_heads_counter += coin_flip_experiment()

    prop.append(two_heads_counter / (flip + 1))
    flips.append(flip + 1)

plt.plot(flips, prop, label = "Experimental Probability")
plt.xlabel("Number of Flips")
plt.ylabel("Proportion of Two Heads")

plt.hlines(0.25, 0, num_trials, colors = "orange", label = "True Probability")
plt.legend()

plt.show()

