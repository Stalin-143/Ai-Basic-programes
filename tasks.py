from celery import Celery

# Initialize Celery
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def run_backup():
    import subprocess
    result = subprocess.run(['python', 'backup.py'], capture_output=True, text=True)
    return result.stdout