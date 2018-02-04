import csv

import pygal
import pygal_maps_world
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code  #获取国家的两位代码

filename = 'API_AG.LND.FRST.ZS_DS2_en_csv_v2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # header_row = next(reader)     这条语句返回了文件的第一行，这里没用

    country_forest = {}
    # 以下代码的作用：
    # 原文件中，每一行都用\t分割列，是个只有一个元素的大列表，join()方法将该列表转化为字符串
    # 然后用split()方法隔开列，形成一个列表，再读取国家和森林覆盖率信息
    for row in reader:
        row = ''.join(row)
        row = row.split('\t')
        cn = row[0]
        try:
            fo = float(row[59])
        except ValueError:  #避免空字符串的出现
            fo = 0
        else:
            code = get_country_code(cn)
            if code:
                country_forest[code] = fo
    

    # 将森林覆盖率分为三个组，区分更明显
    country_forest_high, country_forest_mid, country_forest_low = {}, {}, {}
    for cc, forest in country_forest.items():
        if forest >= 50:
            country_forest_high[cc] = forest
        elif forest < 50 and forest >= 30:
            country_forest_mid[cc] = forest
        else:
            country_forest_low[cc] = forest

    wm_style = RotateStyle('#32CD32', base_style=LightColorizedStyle)
    wm = pygal_maps_world.maps.World(style=wm_style)
    wm.title = 'World Forest Percent in 2015, by Country'
    wm.add('0-30%', country_forest_low)
    wm.add('30%-50%', country_forest_mid)
    wm.add('>=50%', country_forest_high)

    wm.render_to_file('land_forest.svg')