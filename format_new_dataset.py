"""
Format a new dataset. There might not be parallel supported as it's writing into a single file.
"""
# python format_new_dataset.py      --data_directory "data/processed_data/oa_dataset" --output_file pubmed_oa_all.json --dataset_name covid-event
import argparse
import os
import json

import spacy
from tqdm import tqdm

# covid-event
def format_document(fname, dataset_name, nlp):
    json_fp = open(fname, "r")
    with open(fname, "r") as json_fp:
        json_d = json.load(json_fp)
        # only the first line is abstract
        # lines = open(fname).readlines()
        text = json_d["abstract"] # currently abstract TODO: will be replaced by paragraphs later
        pmid = json_d["pmid"]
        title = json_d["full_title"]
        journal = json_d["journal"]
        # year =json_d["publication_year"]
        date = json_d["publication_date"]



        doc = nlp(text)

        sentences = [[tok.text for tok in sent] for sent in doc.sents if len(sent) >= 2]
        doc_key = os.path.basename(fname).replace(".json", "")
        res = {"doc_key": doc_key,
               "dataset": dataset_name,
               "_title": title,
               "_date":date,
               "_journal":journal,
               "sentences": sentences}
    return res


def format_dataset(data_directory, output_file, dataset_name, use_scispacy):
    nlp_name = "en_core_sci_sm" if use_scispacy else "en_core_web_sm"
    nlp = spacy.load(nlp_name)

    fnames = [f"{data_directory}/{name}" for name in os.listdir(data_directory)]
    res = [format_document(fname, dataset_name, nlp) for fname in fnames]
    with open(output_file, "w") as f:
        for doc in tqdm(res):
            print(json.dumps(doc), file=f)


def get_args():
    description = "Format an unlabled dataset, consisting of a directory of `.txt` files; one file per document."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--data_directory", type=str,
                        help="A directory with input `.txt files, one file per document.")
    parser.add_argument("--output_file", type=str,
                        help="The output file, `.jsonl` extension recommended.")
    parser.add_argument("--dataset_name", type=str,
                        help="The name of the dataset. Should match the name of the model you'll use for prediction.")
    parser.add_argument("--use-scispacy", action="store_true",
                        help="If provided, use scispacy to do the tokenization.")
    return parser.parse_args()


def main():
    args = get_args()
    format_dataset(**vars(args))


if __name__ == "__main__":
    main()
