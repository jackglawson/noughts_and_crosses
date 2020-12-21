from dataclasses import dataclass


@dataclass()
class Params:
    num_epochs: int
    explain: bool
    learning: bool


@dataclass
class StrategyParams:
    """
    Parameters for Strategy.

    Parameters
    ----------
    start_q: float
      Each action has an associated q-value. The q-values will be initialised at start_q.

    random_action_rate: float
      Even if the number of hits is over min_hits_before_using_stats, this parameter forces some exploration.

    discount_rate: float
      A reward now is better than future rewards.
      The larger the factor, more weight will be given to future rewards.
      Set discount_rate = 1 to give equal weight to immediate and future rewards.

    next_state_is_predictable: bool
      Is the next state purely dependent on the action now?
      Should be false if there is randomness in the game, or there is more than one player.

    predictive: bool
      if True, strategy will use max q of next state. Should be True if the reward is not given immediately.
    """

    start_q: float
    random_action_rate: float
    discount_rate: float
    next_state_is_predictable: bool
    predictive: bool