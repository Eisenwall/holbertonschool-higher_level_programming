#!/usr/bin/env python3
"""
Task 0: Creating a Simple Templating Program
Generates personalized invitation files from a template and a list of attendees.
"""

import os

def generate_invitations(template, attendees):
    """
    Generates invitation files based on a template and a list of attendees.

    Args:
        template (str): Template string containing placeholders.
        attendees (list): List of dictionaries with attendee data.
    """

    # Validate input types
    if not isinstance(template, str):
        print(f"Error: Template should be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees should be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendee list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        content = template

        # Replace placeholders
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key, "N/A")
            # Handle None values
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{key}}}", str(value))

        # Define output file name
        filename = f"output_{index}.txt"

        # Write to file
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

