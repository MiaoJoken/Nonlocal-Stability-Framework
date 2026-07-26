"""
Nonlocal Stability Operator

Prototype implementation of a feedback operator
with nonlocal information.
"""


class NonlocalStabilityOperator:

    def __init__(
        self,
        alpha=0.1,
        beta=0.05
    ):
        """
        alpha:
        local feedback strength

        beta:
        nonlocal feedback strength
        """

        self.alpha = alpha
        self.beta = beta


    def update(
        self,
        state,
        target,
        history
    ):

        # Local error
        local_error = target - state


        # Nonlocal information
        if len(history) > 0:

            average_state = sum(history) / len(history)

        else:

            average_state = state


        nonlocal_error = target - average_state


        # Combined feedback

        adjustment = (
            self.alpha * local_error
            +
            self.beta * nonlocal_error
        )


        new_state = state + adjustment


        return new_state
