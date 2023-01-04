import pandas as pd
import gensim.models as g


def get_model(self):

    docs = g.doc2vec.TaggedLineDocument(self.abs)
    # doc2vec training -> save_model, models
    
    dm = g.Doc2Vec(docs,
                        vector_size=self.vector_size,
                        window=self.window_size,
                        min_count=self.min_count,
                        sample=self.sample,
                        workers=self.workers,
                        hs=self.hs,
                        dm=1,
                        negative=self.negative,
                        dbow_words=1,
                        dm_concat=1,
                        epochs=self.epochs)
    dm.save(self.args.save_dir+"{}_model.bin".format("dm"))
    
    dbow = g.Doc2Vec(docs,
                        vector_size=self.vector_size,
                        window=self.window_size,
                        min_count=self.min_count,
                        sample=self.sample,
                        workers=self.workers,
                        hs=self.hs,
                        dm=0,
                        negative=self.negative,
                        dbow_words=1,
                        dm_concat=1,
                        epochs=self.epochs)
    dbow.save(self.args.save_dir+"{}_model.bin".format("dbow"))
    
    return dm, dbow

    
    