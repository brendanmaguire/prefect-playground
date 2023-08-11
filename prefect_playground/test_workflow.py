from prefect import flow, task, get_run_logger


@flow
def test_workflow():
    logger = get_run_logger()
    logger.info('Hello world')
    answer = sample_task()
    logger.info(f'The answer is {answer}')


@task
def sample_task():
    return 42


if __name__ == '__main__':
    test_workflow()
