import os
import argparse

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
print(THIS_DIR)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--abs', default='{}\\dataset\\mat_abstract.txt'.format(THIS_DIR), help='raw abstract dir')
    parser.add_argument(
        '--bib', default='{}\\dataset\\mat_bib.txt'.format(THIS_DIR), help='raw bib dir')
    parser.add_argument(
        '--save_dir', default='{}\\model_ckpt\\'.format(THIS_DIR))

    # specific doc2vec parser
    parser.add_argument('--vector_size', default=300,
                        type=int, help='Embedding vector size')
    parser.add_argument('--window_size', default=15,
                        type=int, help='Window size')
    parser.add_argument('--min_count', default=10,
                        type=int, help='Minimum count')
    parser.add_argument('--sampling_threshold', default=1e-5,
                        type=float, help='Sampling threshold')
    parser.add_argument('--worker_count', default=5,
                        type=int, help='Number of workers')
    parser.add_argument('--hs', default=0, type=int,
                        help='Hierarchical softmax')
    parser.add_argument('--negative_size', default=5,
                        type=int, help='Negative size')
    parser.add_argument('--train_epoch', default=100,
                        type=int, help='Training epoch')
    

    # specific clustering parser
    parser.add_argument('--neighbours', default=85,
                        type=int, help='Number of neighbours')
    parser.add_argument('--components', default=20,
                        type=int, help='Number of components')
    parser.add_argument('--cluster_size', default=30,
                        type=int, help='Cluster size')

    return parser.parse_args()


