<p align="center">
<img src="/InfrastructuresPlanner/envs/etc/infraplanner_logo.png" height="160">

<p align="center">
Open-Source RL Environment for Planning Interventions on Transportation Infrastructure
</p>

InfraPlanner is a Python open-source RL environment developed in accordance to the gym environment standards. This environment enables emulating the visual insepctions process, and produces probablistic estimates for the deteriroation condition and speed. The deterioration state in this environment can be obtained at the element-level, the structural category level, and bridge-level.

Paper presnetation: [YouTube](https://youtu.be/4jnUAYb9kkI).

## How to cite

*Hierarchical reinforcement learning for transportation infrastructure maintenance planning* <br/>[Hamida, Z.](https://zachamida.github.io) and [Goulet, J.-A.](http://profs.polymtl.ca/jagoulet/Site/Goulet_web_page_MAIN.html)<br/>Reliablity Engineering \& System Safety 
 [[DOI](https://doi.org/10.1016/j.ress.2023.109214)] <!---[[EndNote]()] [[BibTex]()] -->
 
## Prerequisites

- Python 3.x

- Pytorch: load pre-traind models (Optional).

- Access to GPU computing (Optional)

## Getting Started

To get started, open the terminal and clone the repo,

```{.py}
git clone https://github.com/CivML-PolyMtl/InfrastructuresPlanner-gym.git
```

Access the project folder and install infra_planner package using,

```{.py}
cd InfrastructuresPlanner
pip install -e .
```

Create an instance of the environment,

```{.py}
import gym
import InfrastructuresPlanner
env = gym.make('InfraPlanner-v0')
env.reset()
print(env.cs)
```

## Remarks

The Infra Planner package is originally developed based on the inspection and interventions database of the Transportation Ministry of Quebec (MTQ).


* **Note**: RayEnvWrapper is an external package; therefore, it is required to verify the compatiblity with the OS in use.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on the process for submitting pull requests.

## Authors

* **Zachary Hamida** - *Methodology & code development* - [webpage](https://zachamida.github.io)
* **James-A. Goulet** - *Methodology review & development* - [webpage](http://profs.polymtl.ca/jagoulet/Site/Goulet_web_page_MAIN.html)

## Acknowledgments

- The funding for this project is provided by the Transportation Ministry of Quebec Province (MTQ), Canada.
