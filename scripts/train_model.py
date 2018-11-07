import argparse
import os
import pickle
from scipy import sparse
import sklearn
from sklearn.linear_model import LogisticRegression
import sklearn.pipeline
from sklearn.metrics import roc_auc_score
from azureml.core.run import Run

parser = argparse.ArgumentParser("train model for 20 newsgroups")
parser.add_argument("--hashing_dir", type=str, help="feature hashing directory")
parser.add_argument("--tfidf_dir", type=str, help="tfidf features directory")
parser.add_argument("--input_dir", type=str, help="data directory")
parser.add_argument("--output_dir", type=str, help="output model dir")
args = parser.parse_args()

vectorizers = []
X_train = []

with open(os.path.join(args.hashing_dir, "feats.pkl"), "rb") as fp:
    obj = pickle.load(fp)
    vectorizers.append(("feature_hashing", obj["vectorizer"]))
    X_train.append(obj["X_train"])
    
with open(os.path.join(args.tfidf_dir, "feats.pkl"), "rb") as fp:
    obj = pickle.load(fp)
    vectorizers.append(("tfidf_features", obj["vectorizer"]))
    X_train.append(obj["X_train"])
    
with open(os.path.join(args.input_dir, "20news.pkl"), "rb") as fp:
    obj = pickle.load(fp)
    y_train = obj["data_train"].target
    y_test = obj["data_test"].target
    raw_X_test = obj["data_test"].data
    
X_train = sparse.hstack(X_train)
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

final_model = sklearn.pipeline.Pipeline([("transformer", 
                                          sklearn.pipeline.FeatureUnion(vectorizers)), 
                                         ("model", lr_model)])

# check performance of final model
pred_probs = final_model.predict_proba(raw_X_test)

# binarize labels to compute average auc
binarizer = sklearn.preprocessing.LabelBinarizer()
binarizer.fit(y_train)
y_test_bin = binarizer.transform(y_test)
auc = roc_auc_score(y_test_bin, pred_probs)
print(f"Current AUC: {auc}")

run = Run.get_context()
run.log("auc", auc)

os.makedirs(args.output_dir, exist_ok=True)
out_file = os.path.join(args.output_dir, "model.pkl")
with open(out_file, "wb") as fp:
    pickle.dump(final_model, fp)