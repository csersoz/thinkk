from os import link
import urllib.request


for x in range(10):
    sayfa = 110
    current_page = sayfa + x
    urllib.request.urlretrieve("https://f.eba.gov.tr/ing-soru-bankasi/cambridge/Think-Turkiye-Presentation-Plus-Level-B1/TH_UP_L2/" + "69528" + "/resources/paginas/th_be_l2_sb_p"+ str(current_page) +".jpg", "/Users/cihat.s.ersoz/Documents/WEB/B1/" + str(current_page) + ".jpg")
    print(current_page)

#urllib.request.urlretrieve("https://f.eba.gov.tr/ing-soru-bankasi/cambridge/Think-Turkiye-Presentation-Plus-Level-A2/TH_UP_L1/69506/resources/paginas/th_be_l1_sb_p32.jpg", "local-filename2.jpg")

#U2     69529    
#U3     69530
#U4     69531   
#U5     69521
#U6     69522
#U7     69523
#U8     69524
#U9     69525   
#U10    69526
#U11    69527
#U12    69528