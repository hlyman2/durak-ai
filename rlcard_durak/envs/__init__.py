''' Register new environments
'''

from .env import Env
from rlcard.envs.registration import register, make

register(
    env_id='durak_env',
    entry_point='rlcard_durak.envs.durak_env:DurakEnv',
)