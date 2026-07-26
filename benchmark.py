"""
Benchmark Test

Evaluate different stability methods.

Metrics:

- convergence speed
- final error
- control efficiency
"""


from stability_operator import StabilityOperator
from nonlocal_operator import NonlocalStabilityOperator
from adaptive_nonlocal_operator import AdaptiveNonlocalOperator



TARGET = 100

THRESHOLD = 1



def evaluate(history):

    steps = len(history)

    final_state = history[-1]

    error = abs(TARGET - final_state)

    return steps, error



def run_local():

    model = StabilityOperator(
        alpha=0.1
    )

    state = 0

    history = []


    for i in range(100):

        state = model.update(
            state,
            TARGET
        )

        history.append(state)


        if abs(TARGET-state)<THRESHOLD:
            break


    return history



def run_nonlocal():

    model = NonlocalStabilityOperator(
        alpha=0.1,
        beta=0.05
    )

    state = 0

    history = []


    for i in range(100):

        state = model.update(
            state,
            TARGET,
            history
        )

        history.append(state)


        if abs(TARGET-state)<THRESHOLD:
            break


    return history



def run_adaptive():

    model = AdaptiveNonlocalOperator(
        alpha=0.1,
        beta=0.05,
        threshold=THRESHOLD
    )

    state = 0

    history = []


    for i in range(100):

        state = model.update(
            state,
            TARGET,
            history
        )

        history.append(state)


        if abs(TARGET-state)<THRESHOLD:
            break


    return history



if __name__ == "__main__":


    methods = {

        "Local Feedback":
            run_local(),

        "Nonlocal Feedback":
            run_nonlocal(),

        "Adaptive Nonlocal":
            run_adaptive()
    }



    print(
        "Benchmark Results"
    )

    print("------------------")


    for name, data in methods.items():

        steps, error = evaluate(data)


        print(name)

        print(
            "Steps:",
            steps
        )

        print(
            "Final Error:",
            error
        )

        print()
