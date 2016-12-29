####Functions defined 
##show all quotes +
##add quote +
##update quote
##delete quote
##search quote
##ask question
##print menu 
##main

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def show_all_quotes(wks):
    quotes = wks.get_all_values()
    for entry in quotes:
        print entry[0]

def add_quote(wks, quote):
	wks.append_row([quote])
	show_all_quotes(wks)
	print("Quote added <3")

def update_quote(wks, update):
	print("")

def update_email(email_cell, email):
    print("")

def ask_question(question, legal_input):
    "ask the user a question and return the result"
    while 1:
        response = int(input(question))
        if response in legal_input:
            return response
        print("We don't have that option, try one from within", legal_input, "\n")


def print_menu():
    "print the manage menu"
    print("""
    *********************<3***********************
    Manage Your Program:
        1. show all quotes 
        2. insert new quote
        3. update a quote
        4. delete quote
        5. search quotes
        6. update e-mail roster
        7. send a quote
        8. print quote
        9. exit
    *********************<3***********************
    """)

def main():
    "main function"
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('access.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("Quotes").sheet1

    legal_input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    question = "What would you like to do? "

    while 1: 
        print_menu()
        response = ask_question(question,legal_input)

        #show all quotes
        if response == 1:
            show_all_quotes(wks)
        #add quote
        elif response == 2:
            quote = raw_input("Quote: ")
            add_quote(wks, quote)

        #update quote
        elif response == 3:
            print ("Write the code for this")
            wks.update_acell('A1', "lol")

        #delete quote
        elif response == 4: 
        	print("What quote would you like to delete? ")

        #search spreadsheet 
        elif response == 5:
        	search_Query = input("Search for what quote?: ")
            #cell = worksheet.find(search_Query)
            #print("Found at R%sC%s" % (cell.row, cell.col))

        #update e-mail roster
        elif response == 6:
        	email = input("What e-mail would you liked to add?: ")
        	update_email(email_cell, email)

        #send quote
        elif response == 7:
            print("Sending a random quote to all on list.")

        #print quote
        elif response == 8:
            print("Show quote")
            val = wks.acell('A1').value
            print val

        #exit
        elif response == 9:
            break

        else:
            pass

        input("\n\nThanks for using <3\n")


if __name__ == "__main__":
    main()



# list = ['A1', "A2", "A3", "A4"]

# for each in list:
#     val = wks.acell(each).value
#     print val