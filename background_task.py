import os
import sys
import argparse
def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_file", type=str, metavar="FILE", help="path to config file"
    )
    parser.add_argument(
        "-s", "--seed", default=0, type=int, help="seed for initializing training"
    )

    return parser.parse_args()

args = make_parser()
var = args.config_file.split(',')

execute_cmd = ""
for elem in var:
    print(elem)
    name = elem.split('/')[-1]
    execute_cmd = execute_cmd + sys.executable + " run.py "+elem+" >res_"+str(name)+".txt && "

execute_cmd = execute_cmd[:-3]
print(execute_cmd)
os.system("nohup sh -c '" + execute_cmd + "' &")




