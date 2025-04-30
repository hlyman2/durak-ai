''' Register new environments
'''

from .env import Env
from rlcard_durak.envs.registration import register, make

register(
    env_id='durak',
    entry_point='rlcard_durak.envs.durak_env:DurakEnv',
)