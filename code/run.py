import config
import models.mat_explorer as matexp
import os

if __name__ == '__main__':
    args = config.get_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    mat_explorer = matexp.MatSciExplorer(args)
    mat_explorer.train()
