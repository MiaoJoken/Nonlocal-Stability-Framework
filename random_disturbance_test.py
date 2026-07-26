"""
Random Disturbance Robustness Test

Test adaptive nonlocal stability
under continuous external disturbances.
"""


import random

from adaptive_nonlocal_operator import AdaptiveNonlocalOperator



TARGET = 100



def run_test():

    controller = AdaptiveNonlocalOperator(
        alpha=0.1,
        beta=0.05,
        threshold=1
    )


    state = 0

    history = []

    results = []


    for step in range(100):


        # Apply random disturbance

        disturbance = random.uniform(
            -10,
            10
        )


        state = state + disturbance


        # Stability correction

        state = controller.update(
            state,
            TARGET,
            history
        )


        history.append(state)

        results.append(
            state
        )


    return results



if __name__ == "__main__":


    result = run_test()


    print(
        "Random Disturbance Test"
    )

    print("-----------------------")


    for i,value in enumerate(result):

        print(
            "Step",
            i+1,
            ":",
            value
        )
