# Robotics Navigation Algorithms

Python implementation of a few robotics navigation algorithm. Check [this page](https://atb033.github.io/robotics-navigation-algorithms/) for the website version of this repo.

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


## Usage

### Building the book

If you'd like to develop and/or build the Robotics Navigation Algorithms book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `robotics_navigation_algorithms/` directory
4. Run `jupyter-book clean robotics_navigation_algorithms/` to remove any existing builds
5. Run `jupyter-book build robotics_navigation_algorithms/`

A fully-rendered HTML version of the book will be built in `robotics_navigation_algorithms/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/atb033/robotics_navigation_algorithms/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
