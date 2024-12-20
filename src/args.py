import argparse

def str2bool(value):
    """Convert str to bool for argparse"""
    if value.lower() in ['true', 't', 'yes', '1']:
        return True
    elif value.lower() in ['false', 'f', 'no', '0']:
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected")

def getargs():
    parser = argparse.ArgumentParser(description="Game of Life simulation")
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=10,
        help="Size of the matrix (by default : 10)"
    )
    parser.add_argument(
        "-i", "--iterations",
        type=int,
        default=5,
        help="Number of iterations to render (by default : 5)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Custom seed to use for random"
    )
    parser.add_argument(
        "--activateGui",
        type=str2bool,
        default=True,
        help="Use Pygame has a gui of the program or not"
    )
    
    return parser.parse_args()