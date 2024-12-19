import argparse
# Configuration de argparse pour récupérer les paramètres
def getargs():
    parser = argparse.ArgumentParser(description="Game of Life simulation")
    parser.add_argument(
        "-s", "--size", type=int, default=10, help="Size of the matrix (by default : 10)"
    )
    parser.add_argument(
        "-i", "--iterations", type=int, default=5, help="Number of iterations to render (by default : 5)",
    )
    parser.add_argument(
        "--seed", type=int, default=None, help="Custom seed to use for random"
    )
    
    return parser.parse_args()