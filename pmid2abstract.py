import pubmed_parser as pp
import os
from tqdm import tqdm
if __name__ == '__main__':
    """ Reading pmid files and output to """
    # TODO: add query argument and download and process pmid automatically
    # TODO: embed this package in dyide package

    # read pmid
    fname = "pmid-ergothione-set.txt" # pmid is from https://pubmed.ncbi.nlm.nih.gov/?term=%22ergothioneine%22%5BMeSH+Terms%5D+OR+ergothioneine%5BText+Word%5D
    data_path = "data"
    fin_loc = os.path.join(data_path, fname)

    dir_out = "pmid-ergothione-set" # TODO: make a folder automatocally if folder not exists
    fout_path = os.path.join(data_path, dir_out)


    # 450 out of 610 abstractions are available
    with open(fin_loc, "r") as in_f:
        count = 0
        for line in tqdm(in_f.readlines()):
            pub_dict = pp.parse_xml_web(line.strip(), save_xml=False)
            abstract = pub_dict["abstract"]
            if len(pub_dict["abstract"]) >= 5:# some publication don't have abstract, here we filter out abstraction by string length
                with open(os.path.join(fout_path, f"{pub_dict['pmid']}.txt" ), "w") as out_f:
                    out_f.write(abstract)
            else:
                count += 1
                print("missing abstract: ", count)


