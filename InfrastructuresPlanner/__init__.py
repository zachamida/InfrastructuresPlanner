from gym.envs.registration import register

register(
    id='InfraPlanner-v0',
    entry_point='InfrastructuresPlanner.envs:infra_planner',
)