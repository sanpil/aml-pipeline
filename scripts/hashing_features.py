import argparse
import pickle
from sklearn.feature_extraction.text import HashingVectorizer

parser = argparse.ArgumentParser("generate feature hashing features for 20 newsgroups")
parser.add_argument("--input_dir", type=str, help="data directory")
parser.add_argument("--out_dir", type=str, help="output feature hashing features directory")

args = parser.parse_args()

vectorizer = HashingVectorizer(stop_words='english', alternate_sign=False)

with open(os.path.join(args.input_dir, "20news.pkl"), "rb") as fp:
    obj = pickle.load(fp)
    
data_train = obj["data_train"]
    
X_train = vectorizer.fit_transform(data_train.data)

obj = {}
obj["X_train"] = X_train
obj["vectorizer"] = vectorizer

os.makedirs(args.out_dir)

with open(os.path.join(args.out_dir, "feats.pkl"), "wb") as fp:
    pickle.dump(obj, fp)