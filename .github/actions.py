import json
import os

def metadata():
     pass

def main():
    action = os.environ['PKG_ACTION']

    if action == 'METADATA':
        metadata()
    
   
if __name__ == '__main__':
    main()
