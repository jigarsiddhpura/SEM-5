class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

def total_order_planning(actions, goal):
    plan = []
    current_state = set()

    while not goal <= current_state:
        added = False

        for action in actions:
            if action not in plan and action.preconditions <= current_state:
                plan.append(action)
                current_state |= action.effects
                added = True
                break

        if not added:
            print("Goal cannot be achieved.")
            return None

    return plan

# Define actions with their preconditions and effects for making pizza
actions = [
    Action("Buy Pizza Dough", set(), {"Pizza Dough"}),
    Action("Preheat Oven", set(), {"Oven Preheated"}),
    Action("Roll Out Dough", {"Pizza Dough"}, {"Rolled Out Dough"}),
    Action("Spread Pizza Sauce", {"Rolled Out Dough"}, {"Dough with Sauce"}),
    Action("Grate Cheese", set(), {"Grated Cheese"}),
    Action("Add Cheese to Dough", {"Dough with Sauce", "Grated Cheese"}, {"Pizza with Cheese"}),
    Action("Chop Vegetables", set(), {"Chopped Vegetables"}),
    Action("Add Vegetables to Pizza", {"Pizza with Cheese", "Chopped Vegetables"}, {"Homemade Pizza"}),
    Action("Bake Pizza", {"Homemade Pizza", "Oven Preheated"}, {"Baked Pizza"})
]

pizza_goal = {"Baked Pizza"}

pizza_plan = total_order_planning(actions, pizza_goal)

if pizza_plan:
    print("\nTotal Order Plan for Homemade Pizza:")
    for action in pizza_plan:
        print(action.name)
print('\n')