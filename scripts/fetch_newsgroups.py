import argparse
import pickle
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import HashingVectorizer

parser = argparse.ArgumentParser("download 20 newsgroups dataset")
parser.add_argument("--out_dir", type=str, help="output data dir")

args = parser.parse_args()

categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]

remove = ('headers', 'footers', 'quotes')

data_train = fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42,
                                remove=remove)

data_test = fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42,
                               remove=remove)

obj = {}
obj["data_train"] = data_train
obj["data_test"] = data_test

os.makedirs(args.out_dir)

with open(os.path.join(args.out_dir, "20news.pkl"), "wb") as fp:
    pickle.dump(obj, fp)