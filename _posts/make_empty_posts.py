"""
Usage: python make_empty_posts.py YYYY-MM-DD YYYY-MM-DD
To create empty files from -> to (inclusive)
"""

import os
import sys
from datetime import datetime, timedelta


def generate_markdown_files(start_date_str, end_date_str):
    # Define the template
    template = """---
date: {date}
permalink: /posts/{permalink}/
tags:
  - daily blog
---

### Yesterday
- NOTHING!

### TODO
- FILL IN BLOG POST! 
- BEN DIDN'T FILL IN HIS BLOG POST TODAY BECAUSE HE'S LAZY AND HE SUCKS!

"""
    # Convert the string arguments to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    # Iterate over each day between the start and end date
    current_date = start_date
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday=0, ..., Friday=4)
        if current_date.weekday() < 5:
            # Format the date strings for the file and content
            formatted_date = current_date.strftime("%Y-%m-%d")
            permalink = current_date.strftime("%Y/%m/%d")
            filename = current_date.strftime("%Y-%m-%d") + "-.md"

            # Check if the file already exists
            if not os.path.exists(filename):
                # Create the content by filling in the template
                content = template.format(date=formatted_date, permalink=permalink)

                # Write the content to the corresponding file
                with open(filename, "w") as f:
                    f.write(content)

                print(f"Generated: {filename}")
            else:
                print(f"Skipped (already exists): {filename}")

        # Move to the next day
        current_date += timedelta(days=1)


if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script_name.py YYYY-MM-DD YYYY-MM-DD")
        sys.exit(1)

    # Get the start and end dates from the command line arguments
    start_date_str = sys.argv[1]
    end_date_str = sys.argv[2]

    # Generate markdown files for weekdays between the given dates
    generate_markdown_files(start_date_str, end_date_str)
