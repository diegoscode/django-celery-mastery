from celery import shared_task

@shared_task
def process_data(name):
    # Lógica pesada ou demorada aqui
    return f"Processed data for {name}"
