from os import link
import urllib.request
import requests

dict = {
    "A2U1" : 69496,
    "A2U2" : 69494,
    "A2U3" : 69490,
    "A2U4" : 69492,
    "A2U5" : 69491,
    "A2U6" : 69497,
    "A2U7" : 69493,
    "A2U8" : 69510,
    "A2U9" : 69511,
    "A2U10" : 69512,
    "A2U11" : 69513,
    "A2U12" : 69514}

thislist = ["69496", "69494", "69490", "69492", "69491", "69497", "69493", "69510", "69511", "69512", "69513", "69514"]

#urllib.request.urlretrieve("https://f.eba.gov.tr/ing-soru-bankasi/cambridge/Think-Turkiye-Presentation-Plus-Level-A1/TH_UP_L0/69497/resources/paginas/th_be_l0_sb_p10.jpg", "local-filename2.jpg")


def get_url_status(urls):  # checks status for each url in list urls
    
    for url in urls:
        try:
            r = requests.get(url)
            #print(url + "\tStatus: " + str(r.status_code))
        except Exception as e:
            print(url + "\tNA FAILED TO CONNECT\t" + str(e))
    return str(r.status_code)

def main():
    
    urls = ["https://f.eba.gov.tr/ing-soru-bankasi/cambridge/Think-Turkiye-Presentation-Plus-Level-A2/TH_UP_L1/"+ "69513" + "/resources/paginas/th_be_l1_sb_p102.jpg"]
    if (get_url_status(urls) == "400"):
        print("400 ERROR")
    else:
        print(get_url_status(urls))

if __name__ == "__main__":
    main()
