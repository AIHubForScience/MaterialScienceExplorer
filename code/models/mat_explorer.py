import numpy as np
import pickle
from . import emb_layer, clustering


class MatSciExplorer(object):
    def __init__(self, args):

        self.args = args
        self.vector_size = args.vector_size
        self.window_size = args.window_size
        self.min_count = args.min_count
        self.sample = args.sampling_threshold
        self.workers = args.worker_count
        self.hs = args.hs
        self.negative = args.negative_size
        self.epochs = args.train_epoch

        self.abs = args.abs
        self.bib = args.bib

        self.neighbours = args.neighbours
        self.components = args.components
        self.cluster_size = args.cluster_size

    def train(self):
        
        dm, dbow = emb_layer.get_model(self)

        Y = dm.dv.index_to_key[:]
        V = []
        for tag in Y:
            V.append(np.concatenate([dbow.dv[tag], dm.dv[tag]]))

        result = clustering.get_cluster(self, V)
        pickle.dump(result, open(self.args.save_dir+"_result.pkl",'wb'), protocol = pickle.HIGHEST_PROTOCOL)
        
