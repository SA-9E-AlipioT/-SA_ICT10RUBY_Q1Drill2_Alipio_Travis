
from pyscript import document

# Predefined sets for each grade level
grade_7 = {"Alex Cruz", "Brian Santos", "Carla Reyes"}
grade_8 = {"Daniel Flores", "Ella Garcia", "Faith Mendoza"}
grade_9 = {"Gabriel Torres", "Hannah Lopez", "Ivan Ramos"}
grade_10 = {"Julia Castillo", "Kevin Bautista", "Alex Cruz"}

# Combine all grade-level sets using the union operator
master_members = grade_7 | grade_8 | grade_9 | grade_10


# Function to display the members and their total
def display_members():
    # Sort the names and format them as HTML
    member_names = "<br>".join(sorted(master_members))

    # Display the full list using an f-string
    document.querySelector("#member_list").innerHTML = (
        f"{member_names}"
    )

    # Display the number of unique members
    document.querySelector("#member_count").innerHTML = (
        f"{len(master_members)}"
    )


# Function triggered by the Add Member button
def add_member(event=None):
    # Get the names from the input boxes
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()

    # Combine the first and last names
    new_member = f"{first_name} {last_name}".strip()

    # Add the new member using set union
    master_members.update({new_member} - {""})

    # Show a message and refresh the results
    document.querySelector("#message").innerHTML = (
        f"Member added: {new_member}"
    )

    display_members()

    # Clear the input boxes
    document.querySelector("#first_name").value = ""
    document.querySelector("#last_name").value = ""


# Display the original members when the page loads
display_members()
