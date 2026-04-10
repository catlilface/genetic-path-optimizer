from typing import Literal, TypedDict


class Action(TypedDict):
    short: str
    name: str


MutationStrategy = Literal["inversion", "random_swap", "neighbor_swap", "random"]
CrossoverStrategy = Literal["repeat", "no_repeat", "best_repeat", "best_no_repeat"]
