import click # import the click library to create a CLI
import json # import "Json" to save and load tasks from a file
import os # import "os" to check if the file exists

TODO_FILE = "todo.json" # Define the filename whare tasks are stored

# Function to load tasks from the Json file
def load_tasks():
    if not os.path.exists(TODO_FILE): #Check if file exists
        return [] # if not, return an empty list
    with open(TODO_FILE, "r") as file: # open the file in read mode
        return json.load(file) # load and return the Json data as a Python list
        

# function to save tasks to the Json file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file: # open the file in write mode
        json.dump(tasks, file, indent=4) # save the tasks as formatted Json 
        
        

@click.group() # define a click command group (main CLI)
def cli():
    """"Simple To-Do List Manager""" # docstring for the CLI
    pass # no action , acts as a container for commands

@click.command() # define a command called "add"
@click.argument("task") # Accepts a required argument (task name)
def add(task):
    """Add a new task to the to-do list"""
    tasks = load_tasks() #load existing tasks
    tasks.append({"task" : task , "done" : False}) #append a new task (default: not done)
    save_tasks(tasks) # save the updated tasks
    click.echo(f"Task added: {task}") # Print a susccess message
    
    
@click.command() # define a command called "List"
def list():
    """List all tasks"""
    tasks = load_tasks() # load existing tasks
    if not tasks: # if thare are no tasks
        click.echo("No tasks found") # print a message
        return # Stop execution
    for index, task in enumerate(tasks, 1): # Loop through tasks with numbering
        status = "✓" if task["done"] else "✗" # Show '✓' for completed, '✗' for not
        click.echo(f"{index}. {task["task"]} [{status}]") # Print task with status
        
        
@click.command() # define a command called "comlete"
@click.argument("task_number", type=int) #Accepts a task number as an integer
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks() # load existing tasks
    if 0 < task_number <=len(tasks): # Ensure task number is valid
        tasks[task_number - 1]["done"] = True # Mark as done
        save_tasks(tasks) # Save Updated tasks
        click.echo(f"Task {task_number} marked as completed") # Print success message
    else:
        click.echo("Invalid task number")
        
        
@click.command() # define a command called "delete"
@click.argument("task_number" ,type=int) # Accepts a task number as an integer
def delete(task_number):
    """ Delete a task from the list"""
    tasks = load_tasks() # load existing tasks
    if 0 < task_number <= len(tasks): # Ensure task number is valid
        deleted_task = tasks.pop(task_number - 1) # Remove the task
        save_tasks(tasks) # Save updated tasks
        click.echo(f"Removed task: {deleted_task["task"]}") # Print deleted task
    else:
        click.echo("Invalid task number.") #Handle invalid task number
        
        
# Add commands to the main CLI group
cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

# If the script is run directly, start the CLI
if __name__ == "__main__":
    cli()