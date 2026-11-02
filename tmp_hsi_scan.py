import openpyxl, sys, re

path = r'd:/wnagjin/Compay_Project/CDC_7255/cdc_7255/tmp_eqc1601_hsi.xlsx'
wb = openpyxl.load_workbook(path, data_only=True)
print('SHEETS:', wb.sheetnames)

keys = ['GPIO1', 'GPIO2', 'STR', 'WAKEUP_IN', 'SOC2MCU', 'MCU2SOC']

for ws in wb.worksheets:
    for row in ws.iter_rows():
        for c in row:
            v = c.value
            if v is None:
                continue
            s = str(v)
            if any(k in s for k in keys):
                vals = []
                for cc in row:
                    if cc.value is not None:
                        vals.append(str(cc.value).replace('\n', ' ')[:60])
                print(ws.title, '|', c.coordinate, '|', ' ~ '.join(vals)[:400])
