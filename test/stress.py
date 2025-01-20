import click

from .demo.scripts.predict import predict
from .demo.scripts.train import train

def _execute_in_parallel(workers: int):
    
    processes = [None] * workers
    
    for i in workers:
        p = multiprocessing.Process(target=train)
        p.start()
        processes[i] = p
    
    for p in processes:
        p.join()

@click.command("stress-test")
@click.options("--num-exec", type=int, default=10, help="Number of executions")
@click.options("--workers", type=int, default=1, help="Number of workers available")
def main(executions: int, workers: int = 1) -> None:

    cpu_count = multiprocessing.cpu_count()
    
    if workers > cpu_count: workers = cpu_count

    count = 0

    while count < executions:
        _execute_in_parallel(workers)
        count += workers
        
    _execute_in_parallel(executions - workers)
    
if __name__=="__main__":
    main()