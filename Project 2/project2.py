# Name: Thomas Nguyen
# Course: EE 381
# Date: 12/11/2023
# Description: Create a markov chain from three states devices and print out the probability of each state


import numpy as np

def markov_chain(iteration, start_state = "Disk"):
    # Create a markov chain from three states devices
    state = ["Disk", "Network", "CPU"]
    p = [[0.7, 0.2, 0.1], [0.1, 0.8, 0.1], [0.3, 0.3, 0.4]]
    iter = iteration
    result = [0,0,0]

    current_state = start_state
    for i in range(iter):
        if current_state == "Disk":
            result[0] += 1
        if current_state == "Network":
            result[1] += 1
        if current_state == "CPU":
            result[2] += 1
        current_state = np.random.choice(state, p = p[state.index(current_state)])

    print("Disk: ", round(result[0]/iter*100, 2), "%")
    print("Network: ", round(result[1]/iter*100, 2), "%")
    print("CPU: ", round(result[2]/iter*100, 2), "%")
    print("Busiest: ", state[result.index(max(result))])
    print("Least Busy: ", state[result.index(min(result))])

def main():
    # Create a markove chain
    markov = markov_chain(1000)
    return 0

if __name__ == '__main__':
    main()