import sys
from connect4 import run

if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) == 2 else 8765
    run(port)
