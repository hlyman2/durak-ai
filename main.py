import rlcard
import rlcard_durak
from rlcard_durak import envs
from rlcard.agents.dmc_agent import model as DMCAgent
from rlcard.utils.utils import print_card
import rlcard_durak

num_players = 4
env = rlcard_durak.make(
    'durak_env', 
    config = {'game_num_players': num_players,},
)

agent1 = DMCAgent(env.num_actions)
agent2 = DMCAgent(env.num_actions)
agent3 = DMCAgent(env.num_actions)
agent4 = DMCAgent(env.num_actions)

env.set_agents([
    agent1, 
    agent2, 
    agent3, 
    agent4,
])