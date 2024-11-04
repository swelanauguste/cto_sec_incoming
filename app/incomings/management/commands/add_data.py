import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Incoming
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = "Import incoming data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="The path to the CSV file to be imported",
        )

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]
        with open(csv_file, newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                ref = row["id"]

                # Check if entry already exists based on 'ref'
                if Incoming.objects.filter(ref=ref).exists():
                    self.stdout.write(self.style.WARNING(f"Entry with ref {ref} already exists. Skipping..."))
                    continue

                # Parse boolean fields
                conf = row["confidential"].strip().lower() == "true"
                urgent = row["urgent"].strip().lower() == "true"

                # Handle date parsing
                received_on_str = row["received_on_str"].strip()
                if received_on_str:  # Check if the string is not empty
                    try:
                        received_on = datetime.strptime(received_on_str, "%Y-%m-%d").date()
                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Invalid date format for ref {ref}. Using today's date."))
                        received_on = timezone.now().date()  # Use today's date if parsing fails
                else:
                    received_on = timezone.now().date()  # Default to today's date if the date string is empty

                # Create a new Incoming instance
                incoming = Incoming(
                    ref=get_random_string(length=10),
                    received_on=received_on,
                    conf=conf,
                    urgent=urgent,
                    received_from=row["from"],
                    note=row["note"],
                    originally_from=row["originally_from"],
                    contact=row["contact"],
                    email=row["email"],
                    subject=row["subject"],
                    # You may add additional fields here if needed
                )

                # Save the instance to the database
                try:
                    incoming.save()
                    self.stdout.write(self.style.SUCCESS(f"Successfully added entry with ref {ref}."))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error saving entry with ref {ref}: {e}"))
