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

#### Authors:

Fernando Camou Bejarano A01255376  
Antonio Jesus Calderon Burgos A01255264  
Marco Antonio Ibarra Yedra A01253770  
Luis Carlos Mares Ibarra A01255399  
Mariangel Jose Loaiza Urbina A00838582
