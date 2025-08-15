# Model design
import agentpy as ap

# Visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
import seaborn as sns

class Person(ap.Agent):

    def setup(self):
        """ Initiate agent attributes. """
        self.grid = self.model.grid
        self.random = self.model.random
        self.group = self.random.choice(range(self.p.n_groups))
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

parameters = {
    'want_similar': 0.7, # For agents to be happy
    'n_groups': 2, # Number of groups
    'density': 0.8, # Density of population
    'size': 200, # Height and length of the grid
    'steps': 300  # Maximum number of steps
    }

model = SegregationModel(parameters)
model.setup()

fig, ax = plt.subplots(figsize=(8, 8))
sns.set_style("white")

def update_frame(frame):
    ax.clear()
    model.update()
    model.step()

    if len(model.agents.select(model.agents.happy == False)) == 0:
        ani.event_source.stop()  # Detener la animación
        step = frame + 1
    else:
        model.step()
        step = frame + 1

    group_grid = model.grid.attr_grid('group')
    cmap = mcolors.ListedColormap(["blue", "red"])
    ax.imshow(group_grid, cmap=cmap, origin='upper')
    ax.set_title(f"Paso: {step} | Segregación: {model.get_segregation()}")
    ax.axis('off')

ani = animation.FuncAnimation(fig, update_frame, frames=parameters['steps'], interval=200, repeat=False)

plt.show()