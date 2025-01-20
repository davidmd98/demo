import click
from demo.scripts import predict, train

def _main():
    
    @click.group(chain=True)
    def entry_point() -> None:
        '''Entry point'''
        
    for cmd in (train, predict):
        entry_point.add_command(cmd)
        
    entry_point()
    
if __name__=="__main__":
    _main()