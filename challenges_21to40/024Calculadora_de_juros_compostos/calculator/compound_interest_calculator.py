class CompoundInterestCalculator:
    def __init__(self, principal=0.0, interest_rate=0.0, time=0):
        self.principal = principal
        self.interest_rate = interest_rate
        self.time = time

    def calculate_final_amount(self) -> float:
        """
        Calcula o montante final com base no principal, taxa de juros e tempo.
        """
        return self.principal * (1 + self.interest_rate) ** self.time
