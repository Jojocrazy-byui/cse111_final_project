class Budget:
    """
    An object which keeps track of what one needs for a budget
        Budget: What you can spend in this month
        Budget goals: How close you are to flowing over said budget
        Current trajectory: How soon will your spending go over the budget for this month
    """
    def __init__(self, budget = 0, account_name = 'null')
        self.budget= budget
        self.account = account_name
        self.month = 'Febuary'

    def set_budget(self, budget)
        self.budget = budget

    def reset_account(self, account_name)
        self.account = account_name

    def trajectory(self, account_name, month)
        