# Model design
import agentpy as ap

# Visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

class Person(ap.Agent):

    def setup(self):
        """ Initiate agent attributes. """
        self.grid = self.model.grid
        self.random = self.model.random
        self.group = None
        self.share_similar = 0
        self.happy = False

    def update_happiness(self):
        """ Be happy if rate of similar neighbors is high enough. """
        neighbors = self.grid.neighbors(self)
        similar = len([n for n in neighbors if n.group == self.group])
        ln = len(neighbors)
        self.share_similar = similar / ln if ln > 0 else 0
        self.happy = self.share_similar >= self.p.want_similar

    def find_new_home(self):
        """ Move to random free spot and update free spots. """
        new_spot = self.random.choice(self.model.grid.empty)
        self.grid.move_to(self, new_spot)


class SegregationModel(ap.Model):

    def setup(self):

        # Parameters
        s = self.p.size
        n = self.n = int(self.p.density * (s ** 2))

        # Create grid and agents
        self.grid = ap.Grid(self, (s, s), track_empty=True)
        self.agents = ap.AgentList(self, n, Person)
        self.grid.add_agents(self.agents, random=True, empty=True)

        # Assign groups based on proportions
        proportions = self.p.group_proportions
        if sum(proportions) != 1:
            print("Group proportions are not equal to 1")

        # Create list of group IDs with given proportions
        group_list = []
        for group_id, prop in enumerate(proportions):
            group_list.extend([group_id] * int(round(prop * n)))

        # Adjust length in case of rounding errors
        while len(group_list) < n:
            group_list.append(0)
        while len(group_list) > n:
            group_list.pop()

        # Shuffle and assign
        self.random.shuffle(group_list)
        for agent, group_id in zip(self.agents, group_list):
            agent.group = group_id

    def update(self):
        # Update list of unhappy people
        self.agents.update_happiness()
        self.unhappy = self.agents.select(self.agents.happy == False)

        # Stop simulation if all are happy
        if len(self.unhappy) == 0:
            self.stop()

    def step(self):
        # Move unhappy people to new location
        self.unhappy.find_new_home()

    def get_segregation(self):
        # Calculate average percentage of similar neighbors
        return round(sum(self.agents.share_similar) / self.n, 2)

    def end(self):
        # Measure segregation at the end of the simulation
        self.report('segregation', self.get_segregation())


# Updated parameters with proportions
parameters = {
    'want_similar': 0.3,   # For agents to be happy
    'n_groups': 3,         # Number of groups
    'group_proportions': [0.6, 0.3, 0.1],  # 70% group 0, 30% group 1, # 10% group 2
    'density': 0.95,       # Density of population
    'size': 50,            # Height and length of the grid
    'steps': 100            # Maximum number of steps
}


model = SegregationModel(parameters)
model.setup()

figure, axes = plt.subplots(figsize=(6, 6))
sns.set_style("white")

def update_frame(frame):
    axes.clear()
    model.update()
    model.step() 
    model.t += 1
    group_grid = model.grid.attr_grid('group')
    cmap = plt.get_cmap('Accent', parameters['n_groups'])
    axes.imshow(group_grid, cmap=cmap, origin='upper')
    axes.set_title(f"Paso: { model.t} | Segregación: {model.get_segregation()}")   
    axes.axis('off')

ani = animation.FuncAnimation(figure, update_frame, frames=parameters['steps'] - 1, interval=200, repeat=False)

plt.show()





