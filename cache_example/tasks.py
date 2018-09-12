from django_misc.celery import app


@app.task(name='test_task', bind=True)
def test_task(self):
    # Return value will be shown in celery server console
    # It is returned here to show that task actually ran
    return 'task completed'
