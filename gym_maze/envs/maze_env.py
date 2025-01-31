import gym
from cair_maze.maze_game import MazeGame


class MazeEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    id = "maze-v0"

    def __init__(self, width, height, mechanic, mechanic_args):

        self.env = MazeGame((width, height), mechanic=mechanic, mechanic_args=mechanic_args)

        self.observation_space = self.env.get_state().shape
        self.action_space = 4

    def step(self, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def render(self, mode=0, close=False):
        if close:
            self.env.quit()
            return None

        return self.env.render(type=mode)
