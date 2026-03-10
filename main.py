"""
File to analyse Endfield.

Chengyun Zhu
2026-2-9
"""

from itertools import combinations

# 是否显示 无刻写最优策略 和 有刻写局部最优策略
detail = False
# 是否显示 无刻写最优策略 和 有刻写局部最优策略 的具体武器列表
weapon_detail = False

# 想要查询的武器
query_weapon = "艺术暴君"
# 不需要考虑的武器，比如已填充合适基质的武器
drop_weapons = [
    "不知归", "沧溟星梦", "宏愿", "大雷斑", "赫拉芬格",
    "熔铸火焰", "使命必达",
    "仰止", "迷失荒野", "布道自由",
    "O.B.J.迅极", "O.B.J.轻芒",
    "典范",
    "作品：众生",
    "浪潮", "淬火者", "工业零点一", "荧光雷羽", "长路",
]
# 查询符合基质组合的武器
query_attributes = [
    "智识",  # 基础属性
    "暴击",  # 附加属性
    "流转",  # 技能属性
]


attributes_basic = [
    "敏捷", "力量", "意志", "智识", "主能力"
]
attributes_add = [
    "攻击", "生命",
    "物理", "灼热", "电磁", "寒冷", "自然",
    "暴击", "源石技艺", "终结技",
    "法术", "治疗"
]
attributes_skill = [
    "强攻", "压制", "追袭", "昂扬",
    "粉碎", "巧技", "附术", "残暴",
    "医疗", "切骨", "迸发", "夜幕",
    "流转", "效益"
]

field_1 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "灼热", "电磁", "寒冷", "自然", "源石技艺", "终结技", "法术"],
    "技能": ["强攻", "压制", "追袭", "粉碎", "巧技", "迸发", "流转", "效益"]
}
field_2 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "物理", "电磁", "寒冷", "自然", "暴击", "终结技", "法术"],
    "技能": ["压制", "追袭", "昂扬", "巧技", "附术", "医疗", "切骨", "效益"]
}
field_3 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["生命", "物理", "灼热", "寒冷", "自然", "暴击", "终结技", "治疗"],
    "技能": ["强攻", "压制", "巧技", "残暴", "附术", "迸发", "夜幕", "效益"]
}
field_4 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "生命", "物理", "灼热", "自然", "暴击", "源石技艺", "治疗"],
    "技能": ["追袭", "粉碎", "昂扬", "残暴", "附术", "医疗", "切骨", "流转"]
}
field_5 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "生命", "电磁", "寒冷", "暴击", "终结技", "法术", "治疗"],
    "技能": ["强攻", "粉碎", "残暴", "医疗", "切骨", "迸发", "夜幕", "流转"]
}

weapons = {
    "大雷斑": {
        "干员": "余烬",
        "星级": 6,
        "基础": "力量",
        "附加": "生命",
        "技能": "医疗"
    },
    "沧溟星梦": {
        "干员": "艾尔黛拉",
        "星级": 6,
        "基础": "智识",
        "附加": "治疗",
        "技能": "附术"
    },
    "使命必达": {
        "干员": "洁尔佩塔",
        "星级": 6,
        "基础": "意志",
        "附加": "终结技",
        "技能": "追袭"
    },
    "熔铸火焰": {
        "干员": "莱万汀",
        "星级": 6,
        "基础": "智识",
        "附加": "攻击",
        "技能": "夜幕"
    },
    "不知归": {
        "干员": "骏卫",
        "星级": 6,
        "基础": "意志",
        "附加": "攻击",
        "技能": "流转"
    },
    "宏愿": {
        "干员": "管理员",
        "星级": 6,
        "基础": "敏捷",
        "附加": "攻击",
        "技能": "附术"
    },
    "赫拉芬格": {
        "干员": "别礼",
        "星级": 6,
        "基础": "力量",
        "附加": "攻击",
        "技能": "迸发"
    },
    "负山": {
        "干员": "黎风",
        "星级": 6,
        "基础": "敏捷",
        "附加": "物理",
        "技能": "效益"
    },
    "艺术暴君": {
        "干员": "伊冯",
        "星级": 6,
        "基础": "智识",
        "附加": "暴击",
        "技能": "切骨"
    },
    "破碎君王": {
        "干员": None,
        "星级": 6,
        "基础": "力量",
        "附加": "暴击",
        "技能": "粉碎"
    },
    "昔日精品": {
        "干员": None,
        "星级": 6,
        "基础": "意志",
        "附加": "生命",
        "技能": "效益"
    },
    "典范": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "攻击",
        "技能": "压制"
    },
    "楔子": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "暴击",
        "技能": "附术"
    },
    "遗忘": {
        "干员": None,
        "星级": 6,
        "基础": "智识",
        "附加": "法术",
        "技能": "夜幕"
    },
    "J.E.T.": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "攻击",
        "技能": "压制"
    },
    "骁勇": {
        "干员": None,
        "星级": 6,
        "基础": "敏捷",
        "附加": "物理",
        "技能": "巧技"
    },
    "领航者": {
        "干员": None,
        "星级": 6,
        "基础": "智识",
        "附加": "寒冷",
        "技能": "附术"
    },
    "作品：蚀迹": {
        "干员": None,
        "星级": 6,
        "基础": "意志",
        "附加": "自然",
        "技能": "压制"
    },
    "黯色火炬": {
        "干员": None,
        "星级": 6,
        "基础": "智识",
        "附加": "灼热",
        "技能": "附术"
    },
    "扶摇": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "暴击",
        "技能": "夜幕"
    },
    "热熔切割器": {
        "干员": None,
        "星级": 6,
        "基础": "意志",
        "附加": "攻击",
        "技能": "流转"
    },
    "显赫声名": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "物理",
        "技能": "残暴"
    },
    "白夜新星": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "源石技艺",
        "技能": "附术"
    },
    "同类相食": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "法术",
        "技能": "附术"
    },
    "爆破单元": {
        "干员": None,
        "星级": 6,
        "基础": "主能力",
        "附加": "源石技艺",
        "技能": "迸发"
    },
    "骑士精神": {
        "干员": None,
        "星级": 6,
        "基础": "意志",
        "附加": "生命",
        "技能": "医疗"
    },
    "迷失荒野": {
        "干员": "佩丽卡",
        "星级": 5,
        "基础": "智识",
        "附加": "电磁",
        "技能": "附术"
    },
    "仰止": {
        "干员": "陈千语",
        "星级": 5,
        "基础": "敏捷",
        "附加": "物理",
        "技能": "夜幕"
    },
    "向心之引": {
        "干员": "艾维文娜",
        "星级": 5,
        "基础": "意志",
        "附加": "电磁",
        "技能": "压制"
    },
    "O.B.J.重荷": {
        "干员": "卡契尔",
        "星级": 5,
        "基础": "力量",
        "附加": "生命",
        "技能": "效益"
    },
    "终点之声": {
        "干员": "昼雪",
        "星级": 5,
        "基础": "力量",
        "附加": "生命",
        "技能": "医疗"
    },
    "古渠": {
        "干员": "大潘",
        "星级": 5,
        "基础": "力量",
        "附加": "源石技艺",
        "技能": "残暴"
    },
    "理性告别": {
        "干员": "狼卫",
        "星级": 5,
        "基础": "力量",
        "附加": "灼热",
        "技能": "追袭"
    },
    "O.B.J.迅极": {
        "干员": "萤石",
        "星级": 5,
        "基础": "敏捷",
        "附加": "终结技",
        "技能": "迸发"
    },
    "O.B.J.术识": {
        "干员": "安塔尔",
        "星级": 5,
        "基础": "智识",
        "附加": "源石技艺",
        "技能": "追袭"
    },
    "布道自由": {
        "干员": "赛希",
        "星级": 5,
        "基础": "意志",
        "附加": "治疗",
        "技能": "医疗"
    },
    "O.B.J.轻芒": {
        "干员": "秋栗",
        "星级": 5,
        "基础": "敏捷",
        "附加": "攻击",
        "技能": "流转"
    },
    "十二问": {
        "干员": "弧光",
        "星级": 5,
        "基础": "敏捷",
        "附加": "攻击",
        "技能": "附术"
    },
    "逐鳞3.0": {
        "干员": "阿列什",
        "星级": 5,
        "基础": "力量",
        "附加": "寒冷",
        "技能": "压制"
    },
    "O.B.J.尖峰": {
        "干员": "埃特拉",
        "星级": 5,
        "基础": "意志",
        "附加": "物理",
        "技能": "附术"
    },
    "探骊": {
        "干员": None,
        "星级": 5,
        "基础": "力量",
        "附加": "终结技",
        "技能": "迸发"
    },
    "作品：众生": {
        "干员": None,
        "星级": 5,
        "基础": "敏捷",
        "附加": "法术",
        "技能": "附术"
    },
    "莫奈何": {
        "干员": None,
        "星级": 5,
        "基础": "意志",
        "附加": "终结技",
        "技能": "昂扬"
    },
    "悼亡诗": {
        "干员": None,
        "星级": 5,
        "基础": "智识",
        "附加": "攻击",
        "技能": "夜幕"
    },
    "坚城铸造者": {
        "干员": None,
        "星级": 5,
        "基础": "智识",
        "附加": "终结技",
        "技能": "昂扬"
    },
    "钢铁余音": {
        "干员": None,
        "星级": 5,
        "基础": "敏捷",
        "附加": "物理",
        "技能": "巧技"
    },
    "嵌合正义": {
        "干员": None,
        "星级": 5,
        "基础": "力量",
        "附加": "终结技",
        "技能": "残暴"
    },
    "淬火者": {
        "干员": None,
        "星级": 4,
        "基础": "意志",
        "附加": "生命",
        "技能": "粉碎"
    },
    "工业零点一": {
        "干员": None,
        "星级": 4,
        "基础": "力量",
        "附加": "攻击",
        "技能": "压制"
    },
    "长路": {
        "干员": None,
        "星级": 4,
        "基础": "力量",
        "附加": "法术",
        "技能": "追袭"
    },
    "呼啸守卫": {
        "干员": None,
        "星级": 4,
        "基础": "智识",
        "附加": "攻击",
        "技能": "压制"
    },
    "荧光雷羽": {
        "干员": None,
        "星级": 4,
        "基础": "意志",
        "附加": "攻击",
        "技能": "压制"
    },
    "全自动骇新星": {
        "干员": None,
        "星级": 4,
        "基础": "智识",
        "附加": "法术",
        "技能": "昂扬"
    },
    "浪潮": {
        "干员": None,
        "星级": 4,
        "基础": "智识",
        "附加": "攻击",
        "技能": "追袭"
    },
    "应急手段": {
        "干员": None,
        "星级": 4,
        "基础": "敏捷",
        "附加": "物理",
        "技能": "压制"
    },
    "天使杀手": {
        "干员": None,
        "星级": 4,
        "基础": "意志",
        "附加": "法术",
        "技能": "压制"
    },
    "寻路者道标": {
        "干员": None,
        "星级": 4,
        "基础": "敏捷",
        "附加": "攻击",
        "技能": "昂扬"
    },
}

for weapon in drop_weapons:
    weapons.pop(weapon)

if __name__ == "__main__":
    weapons_in_1 = []
    weapons_in_2 = []
    weapons_in_3 = []
    weapons_in_4 = []
    weapons_in_5 = []
    for weapon in weapons.items():
        if (weapon[1]["技能"] in field_1["技能"]
                and weapon[1]["附加"] in field_1["附加"]):
            weapons_in_1.append(weapon)
        if (weapon[1]["技能"] in field_2["技能"]
                and weapon[1]["附加"] in field_2["附加"]):
            weapons_in_2.append(weapon)
        if (weapon[1]["技能"] in field_3["技能"]
                and weapon[1]["附加"] in field_3["附加"]):
            weapons_in_3.append(weapon)
        if (weapon[1]["技能"] in field_4["技能"]
                and weapon[1]["附加"] in field_4["附加"]):
            weapons_in_4.append(weapon)
        if (weapon[1]["技能"] in field_5["技能"]
                and weapon[1]["附加"] in field_5["附加"]):
            weapons_in_5.append(weapon)
    weapons_in_1 = dict(weapons_in_1)
    weapons_in_2 = dict(weapons_in_2)
    weapons_in_3 = dict(weapons_in_3)
    weapons_in_4 = dict(weapons_in_4)
    weapons_in_5 = dict(weapons_in_5)
    if detail:
        print("无刻写 最优策略：")
        print("-------------------------")
        print(f"能量淤积点1: 包含武器数量 {len(weapons_in_1)}")
        if weapon_detail:
            print(list(weapons_in_1.keys()))
        print(f"能量淤积点2: 包含武器数量 {len(weapons_in_2)}")
        if weapon_detail:
            print(list(weapons_in_2.keys()))
        print(f"能量淤积点3: 包含武器数量 {len(weapons_in_3)}")
        if weapon_detail:
            print(list(weapons_in_3.keys()))
        print(f"能量淤积点4: 包含武器数量 {len(weapons_in_4)}")
        if weapon_detail:
            print(list(weapons_in_4.keys()))
        print(f"能量淤积点5: 包含武器数量 {len(weapons_in_5)}")
        if weapon_detail:
            print(list(weapons_in_5.keys()))

    strategies_1 = {}
    max_counter_1 = 0
    max_strategies_1 = []
    for basic_1, basic_2, basic_3 in list(combinations(field_1["基础"], 3)):
        for add_or_skill in (field_1["附加"] + field_1["技能"]):
            counter = 0
            weapon_list = []
            for weapon in weapons_in_1.items():
                if (weapon[1]["基础"] in [basic_1, basic_2, basic_3]
                        and (weapon[1]["附加"] in add_or_skill or weapon[1]["技能"] in add_or_skill)):
                    counter += 1
                    weapon_list.append(weapon)
            if counter > 0:
                strategies_1[f"{basic_1}, {basic_2}, {basic_3}, {add_or_skill}"] = dict(weapon_list)
            if counter > max_counter_1:
                max_counter_1 = counter
    for item in strategies_1.items():
        if len(item[1].keys()) == max_counter_1:
            max_strategies_1.append(item[0])

    strategies_2 = {}
    max_counter_2 = 0
    max_strategies_2 = []
    for basic_1, basic_2, basic_3 in list(combinations(field_2["基础"], 3)):
        for add_or_skill in (field_2["附加"] + field_2["技能"]):
            counter = 0
            weapon_list = []
            for weapon in weapons_in_2.items():
                if (weapon[1]["基础"] in [basic_1, basic_2, basic_3]
                        and (weapon[1]["附加"] in add_or_skill or weapon[1]["技能"] in add_or_skill)):
                    counter += 1
                    weapon_list.append(weapon)
            if counter > 0:
                strategies_2[f"{basic_1}, {basic_2}, {basic_3}, {add_or_skill}"] = dict(weapon_list)
            if counter > max_counter_2:
                max_counter_2 = counter
    for item in strategies_2.items():
        if len(item[1].keys()) == max_counter_2:
            max_strategies_2.append(item[0])

    strategies_3 = {}
    max_counter_3 = 0
    max_strategies_3 = []
    for basic_1, basic_2, basic_3 in list(combinations(field_3["基础"], 3)):
        for add_or_skill in (field_3["附加"] + field_3["技能"]):
            counter = 0
            weapon_list = []
            for weapon in weapons_in_3.items():
                if (weapon[1]["基础"] in [basic_1, basic_2, basic_3]
                        and (weapon[1]["附加"] in add_or_skill or weapon[1]["技能"] in add_or_skill)):
                    counter += 1
                    weapon_list.append(weapon)
            if counter > 0:
                strategies_3[f"{basic_1}, {basic_2}, {basic_3}, {add_or_skill}"] = dict(weapon_list)
            if counter > max_counter_3:
                max_counter_3 = counter
    for item in strategies_3.items():
        if len(item[1].keys()) == max_counter_3:
            max_strategies_3.append(item[0])

    strategies_4 = {}
    max_counter_4 = 0
    max_strategies_4 = []
    for basic_1, basic_2, basic_3 in list(combinations(field_4["基础"], 3)):
        for add_or_skill in (field_4["附加"] + field_4["技能"]):
            counter = 0
            weapon_list = []
            for weapon in weapons_in_4.items():
                if (weapon[1]["基础"] in [basic_1, basic_2, basic_3]
                        and (weapon[1]["附加"] in add_or_skill or weapon[1]["技能"] in add_or_skill)):
                    counter += 1
                    weapon_list.append(weapon)
            if counter > 0:
                strategies_4[f"{basic_1}, {basic_2}, {basic_3}, {add_or_skill}"] = dict(weapon_list)
            if counter > max_counter_4:
                max_counter_4 = counter
    for item in strategies_4.items():
        if len(item[1].keys()) == max_counter_4:
            max_strategies_4.append(item[0])

    strategies_5 = {}
    max_counter_5 = 0
    max_strategies_5 = []
    for basic_1, basic_2, basic_3 in list(combinations(field_5["基础"], 3)):
        for add_or_skill in (field_5["附加"] + field_5["技能"]):
            counter = 0
            weapon_list = []
            for weapon in weapons_in_5.items():
                if (weapon[1]["基础"] in [basic_1, basic_2, basic_3]
                        and (weapon[1]["附加"] in add_or_skill or weapon[1]["技能"] in add_or_skill)):
                    counter += 1
                    weapon_list.append(weapon)
            if counter > 0:
                strategies_5[f"{basic_1}, {basic_2}, {basic_3}, {add_or_skill}"] = dict(weapon_list)
            if counter > max_counter_5:
                max_counter_5 = counter
    for item in strategies_5.items():
        if len(item[1].keys()) == max_counter_5:
            max_strategies_5.append(item[0])

    if detail:
        print("\n有刻写 局部最优策略: ")
        print("-------------------------")
        print("能量淤积点1: ")
        for max_strategy_1 in max_strategies_1:
            print(f"{max_strategy_1}，包含武器数量 {max_counter_1}")
            if weapon_detail:
                print(list(strategies_1[max_strategy_1].keys()))

        print("能量淤积点2: ")
        for max_strategy_2 in max_strategies_2:
            print(f"{max_strategy_2}，包含武器数量 {max_counter_2}")
            if weapon_detail:
                print(list(strategies_2[max_strategy_2].keys()))

        print("能量淤积点3: ")
        for max_strategy_3 in max_strategies_3:
            print(f"{max_strategy_3}，包含武器数量 {max_counter_3}")
            if weapon_detail:
                print(list(strategies_3[max_strategy_3].keys()))

        print("能量淤积点4: ")
        for max_strategy_4 in max_strategies_4:
            print(f"{max_strategy_4}，包含武器数量 {max_counter_4}")
            if weapon_detail:
                print(list(strategies_4[max_strategy_4].keys()))

        print("能量淤积点5: ")
        for max_strategy_5 in max_strategies_5:
            print(f"{max_strategy_5}，包含武器数量 {max_counter_5}")
            if weapon_detail:
                print(list(strategies_5[max_strategy_5].keys()))

    if query_weapon not in weapons:
        raise ValueError("查询武器输入错误")
    max_counter = 0
    max_strategy = []
    for item in strategies_1.items():
        if query_weapon in item[1].keys():
            max_counter = max(max_counter, len(item[1].keys()))
    for item in strategies_2.items():
        if query_weapon in item[1].keys():
            max_counter = max(max_counter, len(item[1].keys()))
    for item in strategies_3.items():
        if query_weapon in item[1].keys():
            max_counter = max(max_counter, len(item[1].keys()))
    for item in strategies_4.items():
        if query_weapon in item[1].keys():
            max_counter = max(max_counter, len(item[1].keys()))
    for item in strategies_5.items():
        if query_weapon in item[1].keys():
            max_counter = max(max_counter, len(item[1].keys()))
    for item in strategies_1.items():
        if query_weapon in item[1].keys() and len(item[1].keys()) == max_counter:
            max_strategy.append((1, item[0]))
    for item in strategies_2.items():
        if query_weapon in item[1].keys() and len(item[1].keys()) == max_counter:
            max_strategy.append((2, item[0]))
    for item in strategies_3.items():
        if query_weapon in item[1].keys() and len(item[1].keys()) == max_counter:
            max_strategy.append((3, item[0]))
    for item in strategies_4.items():
        if query_weapon in item[1].keys() and len(item[1].keys()) == max_counter:
            max_strategy.append((4, item[0]))
    for item in strategies_5.items():
        if query_weapon in item[1].keys() and len(item[1].keys()) == max_counter:
            max_strategy.append((5, item[0]))

    print(f"\n查询武器 {query_weapon} 全局最优策略: ")
    print("-------------------------")
    for strategy in max_strategy:
        print(f"能量淤积点{strategy[0]}, {strategy[1]}，包含武器数量: {max_counter}")
        if strategy[0] == 1:
            print(list(strategies_1[strategy[1]].keys()))
        elif strategy[0] == 2:
            print(list(strategies_2[strategy[1]].keys()))
        elif strategy[0] == 3:
            print(list(strategies_3[strategy[1]].keys()))
        elif strategy[0] == 4:
            print(list(strategies_4[strategy[1]].keys()))
        elif strategy[0] == 5:
            print(list(strategies_5[strategy[1]].keys()))

    if query_attributes[0] not in attributes_basic:
        raise ValueError("基础属性输入错误")
    if query_attributes[1] not in attributes_add:
        raise ValueError("附加属性输入错误")
    if query_attributes[2] not in attributes_skill:
        raise ValueError("技能属性输入错误")
    list_of_weapons_with_query_attributes = []
    for weapon in weapons.items():
        if (
            weapon[1]["基础"] == query_attributes[0]
            and weapon[1]["附加"] == query_attributes[1]
            and weapon[1]["技能"] == query_attributes[2]
        ):
            list_of_weapons_with_query_attributes.append(weapon[0])

    print(f"\n查询基质 {query_attributes}: ")
    print("-------------------------")
    if len(list_of_weapons_with_query_attributes) != 0:
        print(list_of_weapons_with_query_attributes)
    else:
        print("无符合的武器")
