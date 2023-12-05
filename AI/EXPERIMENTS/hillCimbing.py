import copy

visited_states: list = []

def generate_child_state(current_state :list, prev_heuristic :int, goal_state :list) -> list|int :
    """Generates a child state by moving an element from one peg to another."""

    global visited_states
    state_copy = copy.deepcopy(current_state)

    for i in range(len(state_copy)):
        temp_state = copy.deepcopy(state_copy)

        if len(temp_state[i]) > 0:
            # print(f"temp sta = {temp_state}, i = {i}")  

            # .pop remove last element from the list and returns it ⭐
            element = temp_state[i].pop()
            # print(f"element = {element}")

            for j in range(len(temp_state)):
                new_state = copy.deepcopy(temp_state)

                if j != i:
                    new_state[j] = new_state[j] + [element]
                    # print(f"new state = {new_state}")
                    current_heuristic = calculate_heuristic(
                        new_state, goal_state)
                    # print(j,i,"->",current_heuristic,prev_heuristic)

                    if current_heuristic > prev_heuristic:
                        child_state = copy.deepcopy(new_state)
                        return child_state

    return 0


def calculate_heuristic(current_state :list, goal_state :list) -> int:
    """Calculates the heuristic value for the given state compared to the goal state."""

    goal_positions = goal_state[3]
    heuristic_value = 0

    for i in range(len(current_state)):
        check_values :list = current_state[i]

        if len(check_values) > 0:
            for j in range(len(check_values)):
                if check_values[j] != goal_positions[j]:
                    heuristic_value -= j
                else:
                    heuristic_value += j

    print(f"Heuristic value for {current_state} is {heuristic_value}")
    return heuristic_value


def solve_puzzle(initial_state, goal_state):
    global visited_states

    if initial_state == goal_state:
        print(f"Solution found! {goal_state}\n")
        return

    # create deepcopy to prevent changes in the NESTED structure of the ORIGINAL list
    current_state = copy.deepcopy(initial_state)

    while True:
        visited_states.append(copy.deepcopy(current_state))
        print(f"Current State: {current_state}")

        prev_heuristic = calculate_heuristic(current_state, goal_state)
        child = generate_child_state(current_state, prev_heuristic, goal_state)

        if child == 0:
            print(
                f"No better heuristic value is obtained, declaring this as the goal state - {current_state}\n"
            )
            return

        print(f"Child chosen for exploration: {child}\n")
        current_state = copy.deepcopy(child)
        

def main():
    global visited_states
    initial_state = [[], [], [], ['B', 'C', 'D', 'A']]
    goal_state = [[], [], [], ['A', 'B', 'C', 'D']]
    solve_puzzle(initial_state, goal_state)


if __name__ == "__main__":
    main()
