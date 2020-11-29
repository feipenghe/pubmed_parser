if __name__ == '__main__':
    l = []
    for i in range(10):
        l.append(str(i))

    for i in ("a", "b", "c", "d", "e", "f"):
        l.append(i)

    folder_names = [i + j for i in l for j in l]

    url = "ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/"

    folder_urls = [url + fn for fn in folder_names]
    # folder_urls = [url for fn in folder_names]
    # print(folder_url[0])

    cmd = """sleep 0.5 && wget -r --no-parent --reject "index.html*" """
    long_cmd = ""
    for i in range(len(folder_urls)):
        folder_name = folder_names[i]
        folder_url = folder_urls[i]
        cmd = f"""wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" """ + folder_url
        cmd = cmd + " && " + cmd + " && " + cmd
        long_cmd += cmd  + " & \n"
    # print(long_cmd)

    print(folder_urls[35:])
    check_point = 35
    rest_folder_urls = folder_urls[check_point:]
    num_cmd_line = 14
    num_cmd_per_line = len(rest_folder_urls)//num_cmd_line + 1 # 15 cmd


    long_cmd = ""

    for i in range(num_cmd_line):

        for j in range(num_cmd_per_line):
            # print(i*num_cmd_per_line + j, " / ", len(rest_folder_urls))
            if i*num_cmd_per_line + j == len(rest_folder_urls):
                break
            cmd = "echo 2117 | " # intialize cmd for every cmd
            if j < num_cmd_per_line - 1:
                # if j == 0:
                #     cmd = "sudo "
                cmd += """sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" """ + \
                      rest_folder_urls[i*num_cmd_per_line + j] + "  ||  "
            else:
                cmd += """sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" """ + \
                      rest_folder_urls[i * num_cmd_per_line + j] + "  &  \n"
            long_cmd += cmd
    print(long_cmd)


    # """wget - r - -no - parent - -reject "index.html*" ftp: // ftp.ncbi.nlm.nih.gov / pub / pmc / oa_package /"""

#
# wget -r --no-parent --reject "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/25 2> error_25.log &
# wget -r --no-parent --reject "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/52 2> error_52.log &
# wget -r --no-parent --reject "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/76 2> error_76.log &
# wget -r --no-parent --reject "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/9e 2> error_9e.log &
# wget -r --no-parent --reject "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/ff 2> error_ff.log &


# sleep 42000 && wget -r -N --no-parent --reject  --retry-connrefused --waitretry=1 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/ &


# Currently, we run up to folder 14
# about 15 fetching can be running at the same time otherwise it will warns loggin unsuccessful
# so we should have some scripts later to check files
# wget folder 14 && wget folder 24 ; wget folder 34 ; wget folder 44;



#
# 3-14 one run (need another three pass) 03-0b
# 15-1a three pass  (linuxBackyard)
# 1b -22 three pass


# wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/22 && wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/22 && wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/22




# echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f3  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f4  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f5  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f6  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f7  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f8  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/f9  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/fa  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/fb  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/fc  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/fd  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/fe  ||  echo 2117 | sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_package/ff

# sudo -S wget -r -N --no-parent --reject  --retry-connrefused --waitretry=60 --read-timeout=20 --timeout=15 -t 10 "index.html*" -A ".xml.tar.gz" ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/
# 53, b3, 93, a3, c3, e3