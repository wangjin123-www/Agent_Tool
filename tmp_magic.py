p = r'd:/wnagjin/Compay_Project/CDC_7255/cdc_7255/tmp_eqc1601_hsi.xlsx'
with open(p, 'rb') as f:
    head = f.read(16)
print(head)
