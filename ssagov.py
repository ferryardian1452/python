import csv
from zipfile import ZipFile
import requests

def download():

    url = "https://www.ssa.gov/oact/babynames/names.zip"

    with requests.get(url) as response:

        with open("names.zip", "wb") as temp_file:
            temp_file.write(response.content)

def parse_zip():


    data_list = [["year", "name", "gender", "count"]]

    with ZipFile("names.zip") as temp_zip:

        for file_name in temp_zip.namelist():

            if ".txt" in file_name:

                with temp_zip.open(file_name) as temp_file:

                    for line in temp_file.read().decode("utf-8").splitlines():

                        line_chunks = line.split(",")
                        year = file_name[3:7]
                        name = line_chunks[0]
                        gender = line_chunks[1]
                        count = line_chunks[2]

                        data_list.append([name])

    csv.writer(open("data.csv", "w", newline="",
                    encoding="utf-8")).writerows(data_list)

if __name__ == "__main__":

    download()
    parse_zip()
