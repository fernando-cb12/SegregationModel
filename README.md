# Technical log

## Requirements

Python 3

### Quick setup

#### Install dependencies

```
pip install agentpy
pip install matplotlib
pip install seaborn
```

#### Execution

    python agentpy_segregation.py

Or, for interactive experimentation, open the notebook:

    jupyter notebook agentpy_segregation.ipynb

## Structure

    agentpy_segregation/
    ├── agentpy_segregation.py # Core simulation logic for Schelling's segregation model using AgentPy;
    ├── agentpy_segregation.ipynb # Jupyter notebook for interactive experimentation of the segregation model
    └── README.md # Project overview, setup instructions, usage examples, and documentation.

## Overview

On this repo, we will be adding improvements to the agentpy segregation model.

### Features

- **Customizable group proportions:** Simulate scenarios where population groups are not evenly distributed.  
  Example:
  ```
  'group_proportions': [0.6, 0.3, 0.1],  # 60% group 0, 30% group 1, 10% group 2
  ```
- **Customized colors:** Each group is visualized with a distinct color. The color palette can be changed by modifying the `cmap` parameter in the visualization code (see the notebook for details).

- **Visualization of unhappy agents** A new parameter is displayed in the simulation window, showing the number of unhappy agents at each step.

### Approach

#### Proportion per color

In real-life scenarios, population groups are rarely evenly distributed. Minority groups may experience higher relocation rates due to fewer available neighbors of the same group. This parameter allows you to simulate such scenarios.

#### Executions
<img width="800" height="670" alt="first execution" src="https://github.com/user-attachments/assets/f52a80f0-af20-4eeb-9613-55b586fea00c" />

<img width="800" height="622" alt="second execution" src="https://github.com/user-attachments/assets/fd944120-3fbf-44a7-96bc-6e76c23694ba" />

<img width="800" height="736" alt="third execution" src="https://github.com/user-attachments/assets/7be0e563-f673-4346-8253-1027ee3d797b" />

<img width="800" height="400" alt="happinesRate" src="https://github.com/user-attachments/assets/710c60a2-cfe9-4800-8b0f-2a167a4200e5" />

This plot shows the evolution of the happiness rate of agents over 100 iterations in the segregation model. At the beginning, only about half of the agents are satisfied with their neighborhood, but as the model progresses and agents relocate, the happiness rate increases rapidly. The growth slows down after around 30 iterations and gradually approaches an upper limit close to 100%, indicating that nearly all agents eventually reach a state of satisfaction. This behavior reflects the self organizing dynamics of Schelling’s segregation model, where even simple relocation rules drive the system toward a stable equilibrium.

#### Authors:

Fernando Camou Bejarano A01255376  
Antonio Jesus Calderon Burgos A01255264  
Marco Antonio Ibarra Yedra A01253770  
Luis Carlos Mares Ibarra A01255399  
Mariangel Jose Loaiza Urbina A00838582

#### References
Wilensky, U. (1997). NetLogo Segregation model. http://ccl.northwestern.edu/netlogo/models/Segregation. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
