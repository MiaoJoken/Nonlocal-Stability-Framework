"""
Simulation of Nonlocal Stability Framework

This script tests the convergence
behavior of the stability operator.
"""


from stability_operator import StabilityOperator


def run_simulation():

    # Create stability operator
    controller = StabilityOperator(
        alpha=0.1
    )

    # Initial condition
    state = 0

    # Desired stable state
    target = 100


    history = []


    # Run simulation
    for step in range(50):

        state = controller.update(
            state,
            target
        )

        history.append(state)


    return history



if __name__ == "__main__":

    result = run_simulation()


    print(
        "Simulation Result:"
    )


    for i, value in enumerate(result):

        print(
            "Step",
            i + 1,
            ":",
            value
        )
