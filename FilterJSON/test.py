import json
import pandas as pd
from filterJSONv2 import FilterJSON

json_file_name = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"

json1 = FilterJSON()
json1.getCSV(json_file_name)
