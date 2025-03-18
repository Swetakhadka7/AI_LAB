class BackwardChaining:
    def __init__(self):
        self.rules = {
            "can_enter": ["has_security_clearance", "has_access_card"],
            "has_security_clearance": ["is_employee"],  # Removed 'is_vip' for clarity
            "is_employee": ["has_id_card"]
        }
        self.facts = set()  # Stores known facts

    def add_fact(self, fact):
        self.facts.add(fact)

    def backward_chain(self, goal):
        # If the goal is already a fact, return True
        if goal in self.facts:
            return True
        
        # If the goal is not in the rule base, return False
        if goal not in self.rules:
            return False
        
        # Check if all conditions for the goal are satisfied
        for condition in self.rules[goal]:
            if not self.backward_chain(condition):  # Recursive check
                return False

        # If all conditions are met, we can infer the goal
        self.facts.add(goal)
        return True

# Example Usage
bc = BackwardChaining()

# Adding known facts
bc.add_fact("has_id_card")  # This makes the person an employee
bc.add_fact("has_access_card")

# Checking if a person can enter the restricted area
goal = "can_enter"
if bc.backward_chain(goal):
    print("Access Granted!")
else:
    print("Access Denied!")
