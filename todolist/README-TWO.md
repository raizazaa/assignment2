# PBP Assignment 6 : Javascript and AJAX

[Heroku Application](https://raaassignment2.herokuapp.com/todolist/login)

## Describe the difference between asynchronous programming with synchronous programming.
Asyncronus programming means that program can run at the same time parallelly. While synchronus program can only run one at a time.

## When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.
Event-driven programming is a paradigm where entities (objects, services, and so on) communicate indirectly by sending messages to one another through an intermediary. The flow of the program is determined by events such as user actions (mouse clicks, key presses), sensor outputs, or message passing from other programs or threads. JavaScript web applications can perform this type of programming. One such examples are social media app where every users has different set of pages.

## Describe the implementation of asynchronous programming in AJAX.
Once the HTML page loads, data is read from a web server. Without the need to reload the webpage, the data can be updated. Data transfer happens to the web server in the background. Typically it uses callbacks, functions that are called when the actions complete.

## Way to implement things
First, I made the views function to convert the database into json typefile, along with the pathing so that we can check the json file itself. Then, on the HTML file, I add the script tag to initialize the jquery function. I then made the AJAX GET to display the cards todolist by converting from HTML for loop function to jquery loop function. That be made into a string that can be put in tags. I did similar for the POST function where first, I made the view function for add and also the pathing for it. For the form on the HTML file, I convert the link that redirects to create-task to a modal. For some reason I can't use {{form.as_table}} on the modal, therfore I try to make the form table manually by using the input tag for the task title and also the textarea tag for the description. And have a button to submit it that auto closes after submission. Then, I add the AJAX POST function to grap the data from form. After success, I call the AJAX GET function to display the task data. With this method, it have to refresh the page because of a bug from my noodle coding. To fix this, a possible solution is probably to initialize the data cards from the HTML tags itself rather than to have it empty, then append the added data to the HTML tag. But, I ran out of time, thus I haven't try to implement this.