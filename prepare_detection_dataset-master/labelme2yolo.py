import glob
import json
import os 
import yaml
import io


json_file = glob.glob("./data/annot_16/*.json")
txt_file = "./data/annot_16/labels/"
if not os.path.exists(txt_file):
   os.makedirs(txt_file) 
# print(json_file)
labels_list = []

###########json2txt##########
for file in json_file:
    basename_without_ext = os.path.splitext(os.path.basename(file))[0]
    # print(basename_without_ext)
    f = open(txt_file + basename_without_ext + ".txt", "a") ####
    json_open = open(file, 'r')
    json_load = json.load(json_open)

    # print(len(json_load["shapes"]))


    for i in range (len(json_load["shapes"])):
        label = json_load["shapes"][i]["label"]
        if label not in labels_list:
            labels_list.append(label)
        print(labels_list)
        # print(json_load["shapes"][i]["points"])

flag = False

# print(json_load["shapes"][1]["points"])
for file in json_file:
    basename_without_ext = os.path.splitext(os.path.basename(file))[0]
    # print(basename_without_ext)
    f = open(txt_file + basename_without_ext + ".txt", "a")
    json_open = open(file, 'r')
    json_load = json.load(json_open)
    for i in range (len(json_load["shapes"])):
        for j in range (len(labels_list)):
            if json_load["shapes"][i]["label"] == labels_list[j]:
                num = labels_list.index(labels_list[j])
                # print(num)
                
                   
            
                f.write(str(num))
                for k in range(len(json_load["shapes"][i]["points"])):
                    for l in range(len(json_load["shapes"][i]["points"][k])):
                        normlized_num = round(json_load["shapes"][i]["points"][k][l]/480, 6)
                        f.write(" " + str(normlized_num))
                f.write(" \n")
                f.close
                        

#############################
                    

yaml_file = "./data"
if not os.path.exists(yaml_file):
   os.makedirs(yaml_file)

yaml_file_name = "liver_tumor_16.yaml"

with open(os.path.join(yaml_file, yaml_file_name), "w") as f:
    data = {
        "path":"../data",
        "train":"./trainimg",
        # "train":"./data/trainimg",
        "val":"./valimg",
        # "val":"./data/valimg",
        "test":" ",

        
        "names":{
            0:str(labels_list[0]) ,
            1:str(labels_list[1]) ,
            2:str(labels_list[2]) ,
            3:str(labels_list[3]) ,
            4:str(labels_list[4]) ,

        }
    }
    yaml.safe_dump(data, f)

