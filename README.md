The Steps to follow to make this project are:

Import the libraries
Create a game window
Produce a random grid
Inserting the user input
First, we will import the “pygame” module using the import keyboard. If it’s not there in your system then type the particular command “pip install pygame” in your cmd.
With that, we will also import the “requests” module. The work of this module will be discussed later. After importing the next step is to initialize the pygame with the .init() method, this is the most important step to execute.
The basic need to develop this project is to create a game window and with the help of “pygame. the display.set_mode(width, height)” we will do so. Also to make it user-friendly we have set the title for the game window via “pygme. the display.set_caption( )”.
In the next step we declared a font variable and set the font by using “pygame.font.Font(“font name.ttf”, font_size)”. “.ttf” is the extension to be used with the font name.
To create this game, the most basic need is to produce a grid with a set of random numbers from 1-9. To do this, we will use an API so that every time the user will start the game, he/she will find a new randomly generated grid every time. Before knowing how it should be done, let’s discuss something about APIs.
After reading this 3 letter word the first question that came to our mind is WHAT IS API?
Right! 
API(Application programming interface), is a type of software interface that offers services to other interfaces. It is being done by requesting and getting responses as well.
Now, let’s discuss how we implemented this in our project. So here is one website “https://sugoku.herokuapp.com/board?difficulty=easy” which provides sudoku grids. With the help of this website, we will generate random grids for our game.
The basic mechanism to call an API via an URL and that URL will receive your request and the next step is to send the request. In context with this project, we will use the “get” method to retrieve the information in response to the request.
So to do this, firstly we will import the “requests” module, this module allows you to send HTTP requests using python. Now, we will create a variable named response in which with the help of “requests. get(URL)” we have made the request. Then, in s_grid variable will store the returned JSON object of the result by using “response.json()” and inside this the parameter for which we are searching is boards.
Since, we will be manipulating the grid so we will declare another variable “grid_original” containing the same grid which we will not get manipulate.
Before summing up all these things in a game loop, let’s discuss the functions which are needed to be made.
we have created a UDF named “insert(screen, position)”, this function will add functionality to the program such that the user can fill up the values in the grid, which is what a Sudoku game is like!
To update the grid variable we will just make use of the i and j variable.
We will run a while loop, under that we will check the event type. First of all, with the help of “pygame.event.get()” we will run a loop for events. Now, with the help of the if-else ladder, we will check the event type with the help of “event. type”. If the user quits the game then the “pygame. QUIT” will help us to check so and thus we will return, if the user press any key then the “pygame. KEYDOWN” condition will be checked.
Under keydown event, we have to sum up three things:
The user won’t be able to manipulate the originally generated grid
If the user wants to erase something then one can do so
The user can enter the values to get valid input
The first condition under the key-down event is to violate the user to change the original grid, the second condition is checking whether the key pressed is 0 or not(ASCII CODE for 0- 48), if it is 0 then the value at that particular block should get erased. Erasing a value means drawing a rect of the same color in that area, this is done by “pygame.draw.rect(surface, color, value)”. The third condition is checking for the valid input, whether the entered value is between 1 and 9 or not. The value to be get appeared we will first render the font with the help of “.render()” and then blit it with the help of “.blit()”.
Again with the help of the “while” loop will create a game loop under which we will run this loop until we will get an event, to check the event condition. Under this, we will make use of the if-else ladder to get to know the type of event.
Now we have to check for the Mouse down event with the help of “pygame. MOUSEBUTTONUP”  and for the left click we will use “event.button==1” and thus with the help of “pygame.mouse.get_pos()” will get the position of the mouse and then we will call the insert function.
Now in the game loop to draw the sudoku grid will make use of “pygame.draw.line(screen, color, coordinates, width)” under a for loop, and in order to divide the grid boxes we have put the condition for every 3rd line to get bold by increasing the width.
In the next step, we have add a functionality that a user can manipulate the existing entered output if the user wishes to change the value in order to play according to the rules.
By following these steps, you can easily build a Sudoku game!
