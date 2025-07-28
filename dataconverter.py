import json
import os

identities = {
  "pedestrian": 0,
  "rider+bicycle": 1,
  "rider+scooter": 2,
  "rider+wheelchair": 3,
  "rider+tricycle": 4,
  "rider+buggy": 5,
  "rider+motorbike": 6,
  "person-group-far-away": 7,
  "rider+vehicle-group-far-away": 8,
  "bicycle-group": 9,
  "buggy-group": 10,
  "motorbike-group": 11,
  "scootergroup": 12,
  "tricycle-group": 13,
  "wheelchair-group": 14,
  "scooter-group": 15,
  "rider+co-rider": 16,
  "skateboarder": 17,
  "rider": 18,
  "bicycle": 19,
  "motorbike": 20
}

def read_data(train_val, file_name, city):
    file = f'./datasets/ECP/old_labels/{train_val}/{city}/{file_name}'
    with open(file, 'r') as f:
        data = json.load(f)
    txt_version = file_name.replace('json', 'txt')
    final = f'./datasets/ECP/labels/{train_val}/{txt_version}'
    return data, final

def process_data(data):
    image_height = data['imageheight']
    image_width = data['imagewidth']
    to_return = ''
    for item in data['children']:
        if ("occluded>40" not in item['tags']) and ("occluded>10" not in item['tags']):
            identity = item['identity']
            if "far-away" not in identity:
                children = item['children']
                x0, y0, x1, y1 = item['x0'], item['y0'], item['x1'], item['y1']
                if 'skating' in item['tags']:
                    identity = 'skateboarder'
                elif identity == 'rider' and len(children) > 0:
                    vehicle = children[0]['identity']
                    identity = identity + "+" + vehicle
                try:
                    identity = identities[identity]
                except KeyError:
                    print("changing dictionary: adding " + identity)
                    identities[identity] = len(identities)
                    identity = identities[identity]
                # CORRECT width/height calculation
                x0 = x0 / image_width
                y0 = y0 / image_height
                x1 = x1 / image_width
                y1 = y1 / image_height
                x_center = (x0 + x1) / 2
                y_center = (y0 + y1) / 2
                x_dif = x1 - x0
                y_dif = y1 - y0
                to_return += f"{identity} {x_center} {y_center} {x_dif} {y_dif}\n"
    return to_return

def write_data(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    for train_val in ["train", "val"]:
        cities = os.listdir(f'./datasets/ECP/old_labels/{train_val}')
        for city in cities:
            files = os.listdir(f'./datasets/ECP/old_labels/{train_val}/{city}')
            for file in files:
                print("processing file", file)
                ecp_data, new_file = read_data(train_val, file, city)
                print("new file =", new_file)
                write_data(new_file, process_data(ecp_data))

