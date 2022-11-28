import prefect, os, csv

FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/covid.csv"
   
@prefect.task()
def write_to_csv(csv_data: dict):
    mode = "a" if os.path.exists(FILE_PATH) else "x"
    with open(FILE_PATH, mode) as buffer:
        writer = csv.DictWriter(buffer, fieldnames=csv_data.keys())
        if mode=="x":
           writer.writeheader()
        writer.writerow(csv_data)

@prefect.flow()
def main():
  return

if __name__ == "__main__":
   main()

