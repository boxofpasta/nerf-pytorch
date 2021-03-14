import os
import sys
import shutil
import argparse
import subprocess


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, help='Experiment config json folder.')
    parser.add_argument('-p', '--prefix', type=str, help='Command prefix.', default='')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    """
    Opens a subprocess to start a separate training session for each configuration in the folder.
    """
    args = get_args()
    configs = os.listdir(args.config)
    for config in configs:
        path = os.path.join(args.config, config)
        command = args.prefix + "python run_nerf.py --config " + path
        print('Running:', command)
        subprocess.Popen(command, shell=True)
