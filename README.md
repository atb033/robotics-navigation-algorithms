# Robotics Navigation Algorithms

In this repo, I'll be attempting to implement in Python a few robotics navigation algorithms that are currently supported in [Navigation2](https://navigation.ros.org/). The main inspiration for this project was this [awesome publication](https://arxiv.org/pdf/2307.15236.pdf) by the maintainers of Navigation2.

Please don't hesitate to reach out to me and/or raise PR in case you are interested in contributing to this repo. :)

# Algorithms

## Global Path Planners

- Holonomic Planners
  - Navigation Function
  - Lazy Theta*-P
  - 2D-A*
- Kinematically Feasible Planners
  - Hybrid-A*
  - State Lattice

## Local Trajectory Planners

- Reactive Controllers
  - Dynamic Window Approach
- Predictive Controllers
  - Timed Elastic Band
  - Model Predictive Path Integral
- Geometric and Control-Law Controllers
  - Regulated Pure Pursuit
  - Graceful Controller
  - Rotation Shim 

## Path Smoothing

- Simple Smoother
- Constrained Smoother
- Savitzky-Golay Smoother 

