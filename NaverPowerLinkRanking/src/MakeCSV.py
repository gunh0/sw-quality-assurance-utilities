import csv

def MakeDownloadCSV(output_file_name, tableTempData):
    output_file = open(output_file_name, 'w+', newline='')
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(tableTempData)
    rulList = tableTempData['URL']
    keywordList = tableTempData['KEYWORD']
    rankingList = tableTempData['RANKING']
    for i in range(0, len(rulList)):
        tmpRowData = []
        tmpRowData.append(rulList[i])
        tmpRowData.append(keywordList[i])
        tmpRowData.append(rankingList[i])
        csv_writer.writerow(tmpRowData)
    output_file.close()