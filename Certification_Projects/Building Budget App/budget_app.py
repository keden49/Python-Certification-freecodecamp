
class Category:
    def __init__ (self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description = ''):
        self.ledger.append({'amount': amount, 'description': description})


    def withdraw(self,amount,description = ''):
        if self.check_funds(amount):
            #withdraw can only be possible if the current balance > amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False






    def get_balance(self):
        balance = 0
        for deposit in self.ledger:
            if 'amount' in deposit:
                balance += deposit['amount']
        return balance



    def transfer (self,amount,other):

        if self.check_funds(amount):
            #withdraws from holders @
            self.withdraw(amount,f"Transfer to {other.name}")
            #deposits into receivers @
            other.deposit(amount,f"Transfer from {self.name}")
            return True

        else:
            return False

    def check_funds(self,amount):

        balance = self.get_balance() #returns current balance

        if balance < amount :

            return False
        else:
            return True



    # Display Code
    def __str__(self):
        #centering title with a filler '*'
        title = self.name.center(30,'*')
        formatted_entries = []# empty list to store formatted entries
        for entry in self.ledger:
            #left alignment
            description = f"{entry['description'][:23]:<23}"
            #right alignment
            amount = f"{entry['amount']:7.2f}"
            formatted_entries.append(f"{description}{amount}")
        total_balance = f"Total: {self.get_balance()}"

        output = title + "\n"
        output += "\n".join(formatted_entries)
        output += "\n" + total_balance
        return output
         # formatted items are appended beginning with newline character




# Creating Bar Chart
def create_spend_chart(categories):
    #Calculating Withdrawls
    '''empty dictionary to store all categories sum withdrawls in a key value pair'''
    category_withdrawls = {}
    total_withdrawls = 0 #sum of all category withdrawls

    #import pdb
    for category in categories:
        #Initialize each category withdrawl with a 0
        withdrawls = 0 #each category withdrawl sum

        for transaction in category.ledger:
            #summing only withdrawls
            if transaction['amount'] < 0:
                withdrawls += abs(transaction['amount'])#add absolute value
                #pdb.set_trace()
            #Updating dictionary
            category_withdrawls[category.name] = withdrawls
            total_withdrawls += withdrawls
            #pdb.set_trace()

    category_percentages = {}

    for category_name,withdrawls in category_withdrawls.items():
        if total_withdrawls:
            percentage = (withdrawls/total_withdrawls) * 100
            #rounding down to the nearest 10th
            percentage = (percentage // 10) * 10
            category_percentages[category_name] = percentage
        #Avoiding 0 error
        else:
            category_percentages[category_name] = 0







        #pdb.set_trace()

    #Constructing chart framework

    spend_chart ="Percentage spent by category\n"
    vertical_axis = []

    for line in range(100,-1,-10):
    # creating vertical axis
    # padding with 3 ensures the | is consistent
      axis = f"{str(line).rjust(3)}| "
      vertical_axis.append(axis)
      #pdb.set_trace()

    #Building blocks for chart

    for i, percentage_level in enumerate(range(100,-1,-10)):
      #initialize building block as empty string for every percentage_level
      building_blocks = ""
      for _,percentage in category_percentages.items():
        if percentage >= percentage_level:
          building_blocks += "o  "
        else:
          building_blocks += "   "
        #updating the vertical_axis list

      vertical_axis[i] += building_blocks + "\n"
      #pdb.set_trace()

    spend_chart += "".join(vertical_axis)


     #Create Horizontal line

    num_categories = len(categories)
    '''horizontal space begins with 4 empty spaces to cover the three padded spaces taken by vertical axis intergers and also the space taken by "|"
        a single category takes 3 space characters and an extra space'''

    horizontal_line ="    " + "-" * (num_categories * 3 + 1) + "\n"
    spend_chart += horizontal_line
    #pdb.set_trace()

    #Format Vertical Category Names

    max_name_length = 0
    #pdb.set_trace()
    #getting the category with maximum length name

    for category in categories:
        max_name_length = max(max_name_length, len(category.name))
    #pdb.set_trace()


    category_names_lines = []

    for i in range(max_name_length):
        name_line = "    "  # 4 spaces to align with the chart structure
        for category in categories:
            '''for the first iteration all first letters for all categories will be appended to category_names_lines'''
            if i < len(category.name):
                name_line += ' ' + category.name[i]+' '
                #ensure character occupies
            else:
                name_line += "   " # 3 characters while longer name is printing
        category_names_lines.append(name_line + " \n")
        #pdb.set_trace()

    spend_chart += "".join(category_names_lines)
    #pdb.set_trace()

    #remove trailing new lines
    return spend_chart.rstrip("\n")
    #pdb.set_trace()