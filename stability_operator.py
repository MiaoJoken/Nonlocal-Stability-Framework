"""
Nonlocal Stability Operator

A simple prototype implementation
of a feedback stabilization mechanism.

"""

class StabilityOperator:

    def __init__(self, alpha=0.1):
        """
        alpha:
        feedback strength
        """

        self.alpha = alpha


    def update(self, state, target):

        """
        Update system state through feedback.

        state:
        current system state

        target:
        desired stable state
        """

        error = target - state

        adjustment = self.alpha * error

        new_state = state + adjustment

        return new_state



# Simple demonstration

if __name__ == "__main__":

    operator = StabilityOperator(alpha=0.1)

    state = 0

    target = 100


    print("Initial state:", state)


    for step in range(20):

        state = operator.update(
            state,
            target
        )

        print(
            "Step",
            step + 1,
            ":",
            state
        )
