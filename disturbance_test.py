"""
Disturbance Recovery Test

Test whether the adaptive nonlocal
stability operator can recover after
external disturbances.
"""


from adaptive_nonlocal_operator import AdaptiveNonlocalOperator



def run_disturbance_test():


    controller = AdaptiveNonlocalOperator(
        alpha=0.1,
        beta=0.05,
        threshold=1
    )


    target = 100

    state = 0

    history = []


    results = []


    # Phase 1:
    # System approaches stability

    for step in range(30):

        state = controller.update(
            state,
            target,
            history
        )

        history.append(state)

        results.append(state)



    # Phase 2:
    # External disturbance

    print(
        "Disturbance applied!"
    )

    state = 70


    results.append(state)



    # Phase 3:
    # Recovery process

    for step in range(30):

        state = controller.update(
            state,
            target,
            history
        )

        history.append(state)

        results.append(state)



    return results



if __name__ == "__main__":


    result = run_disturbance_test()


    for i, value in enumerate(result):

        print(
            "Step",
            i,
            ":",
            value
        )
