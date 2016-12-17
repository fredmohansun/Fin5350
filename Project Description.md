Mohan Sun
A02024337
Fa16-FIN5350 Project Description

## LSM model with stochastic volatility

The LSM model, developed by E. Schwartz and F. Longstaff, is an approach use Monte-Carlo simulation to valuing an Vanilla American style option. And the stochastic volatility is added to the model to meet further demand of the model to value an stock in real-option approach, which is assumed have stochastic volatility during its life.

The Model can be divided into two parts: Calculating Stock Price Matrix with simulation, and a recursive payoff solution:

### Calculating Stock Price Matrix with Simulation

We assume that the stock price follow the Ito process, and its stochastic differential equation is:

$$ dS_{t} = (r-div) S_{t} dt + \sqrt{v_{t}} S_{t} dz_{1,t} $$

and we assume that the volatility of the spot price is volatilem following the following stochastic differential equation:

$$ d\sqrt{v_{t}} = -\beta \sqrt{v_{t}} dt + \delta dz_{2,t} $$

For simplicity we assume the correlation between Z1 and Z2 is 0.

The algorithm is Vectorized. And the calulation of the spot price is done with the same column of Volatility vector, and 2 epsilon vector randomly drawn from the normal distribution

### Recursive Payoff Solution:

First, a vector of calculated payoff is set up as CF vector.

For ith column, we do:

    1. if the option is in the money at time i, then it is singled out and put in another vector for linear regression.
    2. Then we run a regression with spot price at i, spot price square at time i, and the PV of payoff at time i+1.
    3. Then we cacluated the PVhat of the payoff, if the PVhat is greater than the payoff at time i, we choose to exercise the model later. Vice versa.
    4. The payoff of a simulation is then calculated by discounting all future payoff back to time 0.
    5. The price is calculated by averagign all pv of payoff of option.
