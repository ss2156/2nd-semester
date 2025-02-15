# M/M/1 Queue Simulation and Analysis Report

## 1. Introduction

The objective of this task is to simulate an M/M/1 queue system using MATLAB and compute relevant performance metrics such as the average number of packets in the queue (\(N_q\)), average number of customers in the system (\(N\)), and average time spent by a customer in the system (\(T\)). The simulation results will be compared with theoretical values.

## 2. MATLAB Simulation Code

The provided MATLAB code consists of several files:

- `mm1_lab.m`: Main simulation file.
- `arrive.m`: Handles packet arrival events.
- `depart.m`: Handles packet departure events.
- `initialize_sys.m`: Initializes system variables.
- `poisson.m`: Generates Poisson-distributed random variables for packet arrival times.
- `timing.m`: Determines the next event to occur and updates simulation time.

## 3. Simulation Parameters

- Arrival rate (\(\lambda\)): \(1\) packet per minute
- Service rate (\(\mu\)): \(2\) packets per minute
- Maximum queue size: \(\infty\)
- Target number of packets for simulation termination: \(100,000\)

## 4. Simulation Execution

The simulation is executed using the given parameters, and relevant statistics are collected during the simulation, such as total time packets spend in the queue (`delay`), total number of packets served (`num_pkts_svc`), and server busy time (`sv_busy`).

## 5. Simulation Results

The following simulation-based metrics are computed:

- Average number of packets in queue (\(N_q\)): \(\frac{\text{q_avg}}{\text{sim_time}}\)
- Average number of customers in the system (\(N\)): \(\frac{\text{delay} + \text{sv_busy}}{\text{sim_time}}\)
- Average time spent by a customer in the system (\(T\)): \(\frac{\text{delay}}{\text{num_pkts_svc}}\)

## 6. Theoretical Formulas

Theoretical values for the M/M/1 queue are calculated using the following formulas:

- \(N_q = \frac{\lambda^2}{\mu(\mu - \lambda)}\)
- \(N = \frac{\lambda}{\mu - \lambda}\)
- \(T = \frac{1}{\mu - \lambda}\)

## 7. Comparison

The simulation-based results are compared with the theoretical values to validate the accuracy of the simulation model.

## 8. Conclusion

The M/M/1 queue simulation was successfully implemented in MATLAB. The simulation-based metrics were computed and compared with theoretical values, demonstrating the accuracy of the simulation model in representing an M/M/1 queue system.
