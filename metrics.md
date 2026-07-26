# Stability Evaluation Metrics

## 1. Introduction

This document defines evaluation metrics for comparing different stability control methods.

The purpose is to measure convergence ability, stability performance, and disturbance recovery.

---

# 2. Convergence Speed

## Definition

Convergence speed measures how quickly a system approaches the target state.

A faster convergence indicates stronger adjustment capability.

Measurement:

Number of steps required to reach the stability region.

---

# 3. Steady-State Error

## Definition

The steady-state error describes the remaining deviation after the system reaches equilibrium.

Formula:

Error = |Target - State|

A smaller error indicates better stability.

---

# 4. Stability Fluctuation

## Definition

A stable system should avoid unnecessary oscillation.

The fluctuation level can be evaluated by:

- State variation
- Overshoot
- Oscillation amplitude

---

# 5. Disturbance Recovery

## Definition

A stable system should recover after external disturbances.

Experiment:

1. Allow system to reach stable state.

2. Apply external disturbance.

3. Measure recovery time.

---

# 6. Energy Efficiency

For practical systems, unnecessary control actions should be minimized.

Evaluation:

- Number of corrections
- Total adjustment amount
- Control cost

---

# 7. Comparison Framework

Methods to compare:

1. Local feedback

2. Nonlocal feedback

3. Adaptive nonlocal feedback with passive stability detection


Evaluation dimensions:

- Convergence speed
- Stability error
- Robustness
- Control efficiency

---

# 8. Future Work

Future experiments will implement automatic measurement of these metrics.
