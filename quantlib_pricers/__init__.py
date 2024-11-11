from .vanilla_pricer import vanilla_pricer 
from .asian_option_pricer import asian_option_pricer
from .barrier_option_pricer import barrier_option_pricer
vanillas = vanilla_pricer()
barriers = barrier_option_pricer()
asians = asian_option_pricer()