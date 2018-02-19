To launch this utility you have to enter following commands:

$cd ~/path/to/this/directory(This command is used to move into utility's directory. It's needed for correct work of database)
$python main.py

    INTERACTIVE MODE

In order to activate the interactive utility mode, you have to launch it without arguments(execute the commands, which were given above):

1. Automatically displays a menu, that will offer to authorize or register a new user.

    REGISTRATION.  When you register a new user, you must specify the following data:
	               Username, using the symbols of the main ascii table. For example: "John Doe". Registration will be performed if the username is valid and unique
	               Current position: Salesman or Manager.
		
    AUTHORIZATION. In this step, you only need to specify the username, of a user, who was registered earlier.
	
2. After autorization you will see command menu, where manager can see sales report(4) and salesman can sell beverages with additives(1), see cost of drinks(2) or load last bill(3).

                                OPERATIONS
	
	(1) Sell beverages. To sell beverages, you must enter the beverage itself and its additive(if the additive is not needed just enter 'none'). After each sale last bill of current salesman will be automatically overwritten.
	(2) See the beverage cost. Just enter the name of beverage.
	(3) Load last bill
	(4) See sales report
	(5) Exit


    WORKING WITH KEYS IN THE COMMAND LINE
        
To execute any actions in command line just launch utility with key -cmd:

-h, --help		- help window with instructions for using keys

-cmd			- key needed to work with the utility in command line mode

-reg, --registration	- use this key  to register a new user

-u, --username		- enter username of the new user after this key

-p, --position		- enter position of the new user after this key

-action			- after this key you need to enter a number of the operation:
				1:sell a drink(Salesman)
				2:Get the beverage price(Salesman)
				3:Load last bill(Salesman)
				4:Show sales records(Manager)
				5:Exit
				
-b, --beverage		- after this key enter the drink you are interested in

-a, --additionals	- after this key enter the beverage to drink

Examples of working with keys:

Register a new manager:
$python main.py -cmd -reg -u Artem -p Manager

Manager artem view sales report:
$python main.py -cmd -u Artem -action 4

Register a new salesman:
$python main.py -cmd -reg -u Vikentsiy -p Salesman

The seller Vikentiy sells latte with nothing:
$python main.py -cmd -u Vikentsiy -action 1 -b latte -a none

