import os, sys
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
sys.path.insert(0, src_path)
import Fega


if __name__ == '__main__':
    Fega.main()