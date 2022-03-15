import csv;
from elasticsearch import Elasticsearch

def initElasticsearch():
    es = Elasticsearch()
    body = {
    }

    es.indices.create(index='jifdas-aie-locations', body=body)


def indexAdmData():
    header = rows = []

    with open("adm2_data.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        es = Elasticsearch()
        for row in csvreader:
            rows.append(row)

            adm_data = {
                "adm_level":2,
                "adm_pcode":row[3],
                "adm_name":row[4]
            }

            result = es.index(index='jifdas-aie-locations', id=row[3], document=adm_data)

    print(rows[:3])

indexAdmData()
