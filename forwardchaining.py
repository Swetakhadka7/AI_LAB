class ForwardChaining:
    def __init__(self):
        self.knowledge_base = {
            "cough": "flu",
            "fever": "flu",
            "sore throat": "flu",
            "runny nose": "cold",
            "sneezing": "cold",
            "headache": "migraine"
        }
        self.facts = set()  # Stores known facts

    def add_fact(self, fact):
        self.facts.add(fact)

    def infer(self):
        conclusions = set()
        for fact in self.facts:
            if fact in self.knowledge_base:
                conclusions.add(self.knowledge_base[fact])
        return conclusions if conclusions else {"No conclusion inferred"}

# Example Usage
inference_engine = ForwardChaining()
inference_engine.add_fact("cough")
inference_engine.add_fact("fever")

result = inference_engine.infer()
print("Inferred Conclusion:", result)
