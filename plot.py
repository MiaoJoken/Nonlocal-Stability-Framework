"""
Visualization of Stability Simulation

This script plots the convergence
behavior of the stability operator.
"""

from stability_operator import StabilityOperator
import matplotlib.pyplot as plt


def generate_data():

    controller = StabilityOperator(
        alpha=0.1
    )

    state = 0
    target = 100

    history = []


    for step in range(50):

        state = controller.update(
            state,
            target
        )

        history.append(state)


    return history



if __name__ == "__main__":

    data = generate_data()


    plt.plot(
        data,
        marker="o"
    )

    plt.title(
        "Nonlocal Stability Convergence"
    )

    plt.xlabel(
        "Step"
    )

    plt.ylabel(
        "System State"
    )


    plt.grid(True)

    plt.show()
