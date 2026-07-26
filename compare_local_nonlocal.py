"""
Comparison experiment

Compare:

1. Local feedback
2. Nonlocal feedback
3. Adaptive nonlocal feedback
"""


from stability_operator import StabilityOperator
from nonlocal_operator import NonlocalStabilityOperator
from adaptive_nonlocal_operator import AdaptiveNonlocalOperator



def run_local():

    model = StabilityOperator(
        alpha=0.1
    )

    state = 0
    target = 100

    history = []


    for i in range(50):

        state = model.update(
            state,
            target
        )

        history.append(state)


    return history



def run_nonlocal():

    model = NonlocalStabilityOperator(
        alpha=0.1,
        beta=0.05
    )

    state = 0
    target = 100

    history = []


    for i in range(50):

        state = model.update(
            state,
            target,
            history
        )

        history.append(state)


    return history



def run_adaptive():

    model = AdaptiveNonlocalOperator(
        alpha=0.1,
        beta=0.05,
        threshold=1
    )

    state = 0
    target = 100

    history = []


    for i in range(50):

        state = model.update(
            state,
            target,
            history
        )

        history.append(state)


    return history



if __name__ == "__main__":


    local = run_local()

    nonlocal_result = run_nonlocal()

    adaptive = run_adaptive()



    print("Local final state:")
    print(local[-1])


    print("\nNonlocal final state:")
    print(nonlocal_result[-1])


    print("\nAdaptive Nonlocal final state:")
    print(adaptive[-1])
