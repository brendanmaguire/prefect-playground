import httpx
from prefect import flow, task, get_run_logger


@flow
def test_workflow():
    logger = get_run_logger()
    logger.info('Hello world')

    log_page("https://example.com/")

    answer = sample_task()
    logger.info(f'The answer is {answer}')


@task
def log_page(url: str) -> None:
    logger = get_run_logger()
    logger.info(httpx.get(url).text)


@task
def sample_task():
    return 42


if __name__ == '__main__':
    test_workflow()
