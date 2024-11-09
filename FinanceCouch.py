import Tracking
from yahoo_fin import get_data
class FinanceCrewAI:
    def __init__(self):
        self.tracking = Tracking.Tracking()

    def analyze_finances(self):
        # Analyze the user's financial information
        transactions = self.tracking.get_transactions()
        expenses = {}

        for transaction in transactions:
            source = transaction['source']
            money = transaction['money']
            if source in expenses:
                expenses[source] += money
            else:
                expenses[source] = money

        # Find the source with the most expenses
        most_expenses = max(expenses, key=expenses.get)
        return most_expenses, expenses[most_expenses]

    def provide_recommendations(self):
        # Provide personalized financial recommendations
        most_expenses, amount = self.analyze_finances()
        print(f"The source with the most expenses is {most_expenses} with an amount of {amount}.")

    def run(self):
        # Main execution loop of the finance coach
        self.provide_recommendations()
        self.tracking.close()

# Instantiate and run the finance crew AI
crew_ai = FinanceCrewAI()
crew_ai.run()