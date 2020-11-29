"""
parse nxml from open access data and use multiple process to outputs individual json file for each nxml
"""
import pubmed_parser as pp
from tqdm import tqdm
if __name__ == '__main__':
    """ Reading pmid files and output to """
    # TODO: add query argument and download and process pmid automatically
    # TODO: embed this package in dyide package
    import os


    #data_path = "data/test_dataset"
    data_path = "/mnt/afcea3e5-090a-47c6-a97a-b169c1f59543/ftp.ncbi.nlm.nih.gov/pub/pmc/oa_xnml_bulk/"
    filelist = os.listdir(data_path)
    fin_locs = [os.path.join(data_path, fname) for fname in filelist]



    # output file path
    out_data_path = "data/processed_data"
    dir_out = "oa_dataset" # TODO: make a folder automatocally if folder not exists
    #dir_out = "temp_dataset"
    fout_path = os.path.join(out_data_path, dir_out)
    if not os.path.isdir(fout_path):
        os.mkdir(fout_path)

    import json
    import sys

    from multiprocessing import Pool


    ## dict_keys(['full_title', 'abstract', 'journal', 'pmid', 'pmc', 'doi', 'publisher_id', 'author_list', 'affiliation_list', 'publication_year', 'publication_date', 'subjects', 'coi_statement'])


    ## TODO: take a list of nxml files and pool them
    def query_data(fin_loc):
        # 450 out of 610 abstractions are available
        dict_out = pp.parse_pubmed_xml(fin_loc)
        # abstract = pub_dict["abstract"]
        # pmid = pub_dict["pmid"]
        # title = pub_dict["full_title"]
        # journal = pub_dict["journal"]
        # year = pub_dict["publication_year"]
        # date = dict_out["publication_date"]
        # # url = pub_dict["url"]
        # data_to_write = (abstract, pmid, title, journal, year, date)
        count = 0

        dump_count = 0
        if len(dict_out["abstract"]) >= 5:  # some publication don't have abstract, here we filter out abstraction by string length
            with open(os.path.join(fout_path, f"{dict_out['pmid']}.json" ), "w") as out_f:
                json.dump(dict_out, out_f)
            # with open(os.path.join(fout_path, f"{pub_dict['pmid']}.txt"), "w") as out_f:
            #     for data in data_to_write:
            #         out_f.write(data + "\n")
            dump_count += 1
        else:
            count += 1

            with open(f"{fout_path}/missing_abstract", "a+") as f:
                f.write(dict_out["pmid"] + ":     " + dict_out["abstract"])
    with Pool(64) as p:
        print(tqdm(p.map(query_data, fin_locs)))




    # p.map(query_data, fin_loc)
