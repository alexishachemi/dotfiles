from shutil import copyfile
import os
import os.path as osp
from sys import argv as args
from sys import exit as sexit
import file_manager as fm

args.pop(0)

config = fm.read_config()

def export():
    for file in config["tracked_files"]:
        copyfile(osp.abspath(osp.expanduser(file)), osp.join(fm.TRACKED_DIR, osp.basename(file)))
    fm.write_tracked(config["tracked_files"])


def install():
    for file in config["tracked_files"]:
        copyfile(osp.join(fm.TRACKED_DIR, osp.basename(file)), osp.abspath(osp.expanduser(file)))
    
    #TODO: install packages


def purge():
    try:
        for file in os.listdir(fm.TRACKED_DIR):
            os.remove(osp.join(fm.TRACKED_DIR, file))
        os.rmdir(fm.TRACKED_DIR)
    except FileNotFoundError:
        pass
    try:
        os.remove(fm.TRACKED_PATH)
    except FileNotFoundError:
        pass


def print_usage():
    print('''USAGE: installer CMD
            CMD:
                install     install tracked files and packages
                export      copy tracked files to the repository
                purge       delete currently saved tracked files
          ''')


def args_are_valid() -> bool:
    if len(args) != 1 or any([h in args for h in ["-h", "-help", "--help"]]):
        return False
    if not args[0] in ["install", "export", "purge"]:
        return False
    return True


def main():
    if not args_are_valid():
        print_usage()
        sexit(1)
    os.makedirs(fm.TRACKED_DIR, exist_ok=True)
    match args[0]:
        case "install":
            install()
        case "export":
            export()
        case "purge":
            purge()

if __name__ == "__main__":
    main()
