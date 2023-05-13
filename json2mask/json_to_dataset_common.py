'''
该程序仅支持输入是文件夹，
            输出是文件夹。
'''
import argparse
import base64
import json
import os
import os.path as osp

import PIL.Image
import yaml

from labelme_tools.logger import logger
from labelme_tools import  utils


def main():
    logger.warning('This script is aimed to demonstrate how to convert the'
                   'JSON file to a single image dataset, and not to handle'
                   'multiple JSON files to generate a real-use dataset.')

    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json_file', default=r"D:\work\91360\shihezi_shiguan\code\MyUtils\labelme_tools\test_data\json")
    parser.add_argument('-o', '--out', default=r"D:\work\91360\shihezi_shiguan\code\MyUtils\labelme_tools\test_data\json_out")
    args = parser.parse_args()

    json_file = args.json_file
    root_out_dir = args.out
    if not osp.exists(root_out_dir):
        os.mkdir(root_out_dir)

    count = os.listdir(json_file)
    for i in range(0, len(count)):
        path = os.path.join(json_file, count[i])
        if os.path.isfile(path):
            data = json.load(open(path))

            if data['imageData']:
                imageData = data['imageData']
            else:
                imagePath = os.path.join(os.path.dirname(path), data['imagePath'])
                with open(imagePath, 'rb') as f:
                    imageData = f.read()
                    imageData = base64.b64encode(imageData).decode('utf-8')
            img = utils.img_b64_to_arr(imageData)
            label_name_to_value = {'_background_': 0}
            # 标记成cell或者cell1，cell2的转折代码
            data_shapes = data['shapes']
            t_mark = 0
            for shape_i in range(len(data_shapes)):
                label_name = data_shapes[shape_i]['label']
                t_mark = t_mark + 1
                label_name = label_name + str(t_mark)
                data_shapes[shape_i]['label'] = label_name
                if label_name in label_name_to_value:
                    label_value = label_name_to_value[label_name]
                else:
                    label_value = len(label_name_to_value)
                    label_name_to_value[label_name] = label_value

            # label_values must be dense
            label_values, label_names = [], []
            for ln, lv in sorted(label_name_to_value.items(), key=lambda x: x[1]):
                label_values.append(lv)
                label_names.append(ln)
            assert label_values == list(range(len(label_values)))

            lbl = utils.shapes_to_label(img.shape, data_shapes, label_name_to_value)

            captions = ['{}: {}'.format(lv, ln)
                        for ln, lv in label_name_to_value.items()]
            lbl_viz = utils.draw_label(lbl, img, captions)

            out_dir = osp.basename(count[i]).replace('.', '_')
            out_dir = osp.join(root_out_dir, out_dir)
            if not osp.exists(out_dir):
                os.mkdir(out_dir)

            PIL.Image.fromarray(img).save(osp.join(out_dir, 'img.png'))
            # PIL.Image.fromarray(lbl).save(osp.join(out_dir, 'label.png'))
            utils.lblsave(osp.join(out_dir, 'label.png'), lbl)
            PIL.Image.fromarray(lbl_viz).save(osp.join(out_dir, 'label_viz.png'))

            with open(osp.join(out_dir, 'label_names.txt'), 'w') as f:
                for lbl_name in label_names:
                    f.write(lbl_name + '\n')

            logger.warning('info.yaml is being replaced by label_names.txt')
            info = dict(label_names=label_names)
            with open(osp.join(out_dir, 'info.yaml'), 'w') as f:
                yaml.safe_dump(info, f, default_flow_style=False)

            logger.info('Saved to: {}'.format(out_dir))


if __name__ == '__main__':
    main()
