# myproject/streamlit_app/management/commands/run_streamlit.py
from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    help = 'Run the Streamlit app'

    def handle(self, *args, **kwargs):
        subprocess.run(['streamlit', 'run', 'run.py'])
