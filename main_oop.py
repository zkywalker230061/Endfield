"""
File to analyse Endfield.

Chengyun Zhu
2026-6-11
"""

from itertools import combinations

# 是否显示 无刻写最优策略 和 有刻写局部最优策略
detail = False
# 是否显示 无刻写最优策略 和 有刻写局部最优策略 的具体武器列表
weapon_detail = False
# # 是否查询所有武器的全局最优策略
# all_weapons = False

# 想要查询的武器
query_weapon = "负山"
# 不需要考虑的武器，比如已填充合适基质的武器
drop_weapons = [
    "不知归", "沧溟星梦", "宏愿", "大雷斑", "赫拉芬格", "艺术暴君", "落草", "孤舟", "狼之绯",
    "熔铸火焰", "使命必达",
    "仰止", "迷失荒野", "布道自由", "向心之引",
    "O.B.J.迅极", "O.B.J.轻芒", "O.B.J.尖峰",
    "典范", "黯色火炬", "扶摇", "J.E.T.", "热熔切割器", "作品：蚀迹", "望乡",
    "作品：众生", "探骊", "悼亡诗", "嵌合正义",
    "浪潮", "淬火者", "工业零点一", "荧光雷羽", "长路", "呼啸守卫", "显锋",
]
# 查询符合基质组合的武器
query_attributes = [
    "力量",  # 基础属性
    "生命",  # 附加属性
    "残暴",  # 技能属性
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
    "技能": ["强攻", "压制", "追袭", "粉碎", "巧技", "迸发", "流转", "效益"],
    "name": "枢纽区"
}
field_2 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "物理", "电磁", "寒冷", "自然", "暴击", "终结技", "法术"],
    "技能": ["压制", "追袭", "昂扬", "巧技", "附术", "医疗", "切骨", "效益"],
    "name": "源石研究园"
}
field_3 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["生命", "物理", "灼热", "寒冷", "自然", "暴击", "终结技", "治疗"],
    "技能": ["强攻", "压制", "巧技", "残暴", "附术", "迸发", "夜幕", "效益"],
    "name": "矿脉源区"
}
field_4 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "生命", "物理", "灼热", "自然", "暴击", "源石技艺", "治疗"],
    "技能": ["追袭", "粉碎", "昂扬", "残暴", "附术", "医疗", "切骨", "流转"],
    "name": "供能高地"
}
field_5 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "生命", "电磁", "寒冷", "暴击", "终结技", "法术", "治疗"],
    "技能": ["强攻", "粉碎", "残暴", "医疗", "切骨", "迸发", "夜幕", "流转"],
    "name": "武陵城"
}
field_6 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["生命", "物理", "电磁", "寒冷", "源石技艺", "终结技", "法术", "治疗"],
    "技能": ["压制", "粉碎", "昂扬", "巧技", "医疗", "切骨", "迸发", "夜幕"],
    "name": "清波寨"
}
field_7 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "物理", "灼热", "电磁", "自然", "暴击", "终结技", "法术"],
    "技能": ["强攻", "追袭", "昂扬", "残暴", "附术", "夜幕", "流转", "效益"],
    "name": "首墩"
}
field_8 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["生命", "灼热", "电磁", "寒冷", "自然", "源石技艺", "终结技", "治疗"],
    "技能": ["压制", "粉碎", "巧技", "残暴", "附术", "切骨", "夜幕", "流转"],
    "name": "试验园区"
}
field_9 = {
    "基础": ["敏捷", "力量", "意志", "智识", "主能力"],
    "附加": ["攻击", "生命", "物理", "灼热", "寒冷", "自然", "源石技艺", "治疗"],
    "技能": ["强攻", "追袭", "昂扬", "巧技", "医疗", "切骨", "迸发", "效益"],
    "name": "藏剑谷"
}
field_map = {
    1: field_1,
    2: field_2,
    3: field_3,
    4: field_4,
    5: field_5,
    6: field_6,
    7: field_7,
    8: field_8,
    9: field_9,
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
    "落草": {
        "干员": "汤汤",
        "星级": 6,
        "基础": "敏捷",
        "附加": "攻击",
        "技能": "迸发"
    },
    "狼之绯": {
        "干员": "洛茜",
        "星级": 6,
        "基础": "敏捷",
        "附加": "暴击",
        "技能": "切骨"
    },
    "孤舟": {
        "干员": "庄方宜",
        "星级": 6,
        "基础": "意志",
        "附加": "攻击",
        "技能": "压制"
    },
    "赤缨": {
        "干员": "弭弗",
        "星级": 6,
        "基础": "力量",
        "附加": "攻击",
        "技能": "巧技"
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
    "光荣记忆": {
        "干员": None,
        "星级": 6,
        "基础": "敏捷",
        "附加": "暴击",
        "技能": "夜幕"
    },
    "望乡": {
        "干员": None,
        "星级": 6,
        "基础": "敏捷",
        "附加": "寒冷",
        "技能": "压制"
    },
    "雾中微光": {
        "干员": None,
        "星级": 6,
        "基础": "意志",
        "附加": "电磁",
        "技能": "效益"
    },
    "灯火使命": {
        "干员": None,
        "星级": 6,
        "基础": "敏捷",
        "附加": "终结技",
        "技能": "效益"
    },
    "幻想苦痛": {
        "干员": None,
        "星级": 6,
        "基础": "力量",
        "附加": "源石技艺",
        "技能": "压制"
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
    "显锋": {
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

for drop_weapon in drop_weapons:
    weapons.pop(drop_weapon)

# if not all_weapons:
#     for drop_weapon in drop_weapons:
#         weapons.pop(drop_weapon)


class EndfieldOptimizer:
    """
    Query Endfield matrix strategies.

    Parameters
    ----------
    fields : dict
        Field data.
        The key is the field ID, and
        the value contains basic, additional, skill, and name information.
    weapons_data : dict
        Weapon data.
        The key is the weapon name, and
        the value contains the weapon attributes.

    Attributes
    ----------
    fields : dict
        Field data used by the optimizer.
    weapons : dict
        Weapon data used by the optimizer.
    weapons_in_fields : dict
        Weapons covered by each field.
    strategies : dict
        Available engraving strategies for each field.
    max_counters : dict
        Maximum number of weapons covered by local optimal strategies in each field.
    max_strategies : dict
        Local optimal strategy names for each field.
    """

    def __init__(self, fields, weapons_data):
        """
        Initialize the strategy optimizer.

        Parameters
        ----------
        fields : dict
            Field data.
            The key is the field ID, and
            the value contains field attribute settings.
        weapons_data : dict
            Weapon data.
            The key is the weapon name, and
            the value contains weapon attribute settings.
        """
        self.fields = fields
        self.weapons = weapons_data
        self.weapons_in_fields = {}
        self.strategies = {}
        self.max_counters = {}
        self.max_strategies = {}

    def get_weapons(self, field):
        """
        Get weapons covered by one field.

        Parameters
        ----------
        field : dict
            Attribute settings of one field.

        Returns
        -------
        dict
            Weapons whose additional and skill attributes both match the field.
        """
        weapons_in_field = []
        for weapon in self.weapons.items():
            if (weapon[1]["技能"] in field["技能"] and weapon[1]["附加"] in field["附加"]):
                weapons_in_field.append(weapon)
        return dict(weapons_in_field)

    def get_weapons_in_fields(self):
        """
        Calculate weapons covered by all fields.

        Result is stored in ``self.weapons_in_fields``.
        """
        for field_id, field in self.fields.items():
            self.weapons_in_fields[field_id] = self.get_weapons(field)

    def print_weapons_in_fields(self):
        """
        Print weapon counts covered by each field without engraving.

        Returns
        -------
        None
            Results are printed only when the global variable ``detail`` is ``True``.
        """
        if not detail:
            return
        print("无刻写 最优策略：")
        print("-------------------------")
        for field_id, field in self.fields.items():
            weapons_in_field = self.weapons_in_fields[field_id]
            print(f"{field_id}. {field['name']}: 包含武器数量 {len(weapons_in_field)}")
            if weapon_detail:
                print(list(weapons_in_field.keys()))

    def get_strategies(self, field_id):
        """
        Calculate all available engraving strategies for one field.

        Parameters
        ----------
        field_id : int
            Field ID.

        Returns
        -------
        tuple
            A tuple of ``(strategies, max_counter, max_strategies)``.
            ``strategies`` is the strategy dictionary,
            ``max_counter`` is the maximum covered weapon count, and
            ``max_strategies`` is the list of strategy names that reach the maximum count.
        """
        field = self.fields[field_id]
        strategies = {}
        max_counter = 0
        max_strategies = []
        weapons_in_field = self.weapons_in_fields[field_id]
        for basic_1, basic_2, basic_3 in list(combinations(field["基础"], 3)):
            for add_or_skill in (field["附加"] + field["技能"]):
                counter = 0
                weapon_list = []
                for weapon in weapons_in_field.items():
                    if (weapon[1]["基础"] in [basic_1, basic_2, basic_3]
                            and (weapon[1]["附加"] in add_or_skill
                                 or weapon[1]["技能"] in add_or_skill)):
                        counter += 1
                        weapon_list.append(weapon)
                if counter > 0:
                    strategy_name = f"{basic_1}, {basic_2}, {basic_3}, {add_or_skill}"
                    strategies[strategy_name] = dict(weapon_list)
                max_counter = max(max_counter, counter)
        for item in strategies.items():
            if len(item[1].keys()) == max_counter:
                max_strategies.append(item[0])
        return strategies, max_counter, max_strategies

    def get_strategies_in_fields(self):
        """
        Calculate available engraving strategies for all fields.

        Results are stored in
        ``self.strategies``, ``self.max_counters``, and ``self.max_strategies``.
        """
        for field_id in self.fields:
            strategies, max_counter, max_strategies = self.get_strategies(field_id)
            self.strategies[field_id] = strategies
            self.max_counters[field_id] = max_counter
            self.max_strategies[field_id] = max_strategies

    def print_strategies_in_fields(self):
        """
        Print local optimal engraving strategies for each field.

        Returns
        -------
        None
            Results are printed only when the global variable ``detail`` is ``True``.
        """
        if not detail:
            return
        print("\n有刻写 局部最优策略: ")
        print("-------------------------")
        for field_id, field in self.fields.items():
            print(f"{field_id}. {field['name']}: ")
            for max_strategy in self.max_strategies[field_id]:
                print(f"{max_strategy}，包含武器数量 {self.max_counters[field_id]}")
                if weapon_detail:
                    print(list(self.strategies[field_id][max_strategy].keys()))

    def check_query_weapon(self):
        """
        Check whether the queried weapon exists.

        Raises
        ------
        ValueError
            Raised when the global variable ``query_weapon`` is not in the weapon dictionary.
        """
        if query_weapon not in self.weapons:
            raise ValueError("查询武器输入错误")

    def get_query_weapon_max_counter(self):
        """
        Get the global maximum covered count for the queried weapon.

        Returns
        -------
        int
            The maximum number of covered weapons among strategies that contain the queried weapon.
        """
        max_counter = 0
        for field_id in self.fields:
            for item in self.strategies[field_id].items():
                if query_weapon in item[1].keys():
                    max_counter = max(max_counter, len(item[1].keys()))
        return max_counter

    def get_query_weapon_max_strategy(self, max_counter):
        """
        Get global optimal strategies for the queried weapon.

        Parameters
        ----------
        max_counter : int
            Global maximum covered count for the queried weapon.

        Returns
        -------
        list
            A list of two-item tuples. Each tuple contains the field ID and the strategy name.
        """
        max_strategy = []
        for field_id in self.fields:
            for item in self.strategies[field_id].items():
                if (query_weapon in item[1].keys()
                        and len(item[1].keys()) == max_counter):
                    max_strategy.append((field_id, item[0]))
        return max_strategy

    def print_query_weapon_strategy(self):
        """
        Print global optimal strategies for the queried weapon.

        Results are printed to standard output.
        """
        self.check_query_weapon()
        max_counter = self.get_query_weapon_max_counter()
        max_strategy = self.get_query_weapon_max_strategy(max_counter)
        print(f"\n查询武器 {query_weapon} 全局最优策略: ")
        print("-------------------------")
        for strategy in max_strategy:
            field_id = strategy[0]
            strategy_name = strategy[1]
            print(
                f"{field_id}. {self.fields[field_id]['name']}, {strategy_name}，"
                f"包含武器数量: {max_counter}"
            )
            print(list(self.strategies[field_id][strategy_name].keys()))

    def check_query_attributes(self):
        """
        Check whether the queried matrix attributes are valid.

        Raises
        ------
        ValueError
            Raised when the basic, additional, or skill attribute is not in
            the corresponding attribute list.
        """
        if query_attributes[0] not in attributes_basic:
            raise ValueError("基础属性输入错误")
        if query_attributes[1] not in attributes_add:
            raise ValueError("附加属性输入错误")
        if query_attributes[2] not in attributes_skill:
            raise ValueError("技能属性输入错误")

    def get_weapons_with_query_attributes(self):
        """
        Get weapons matching the queried matrix attribute combination.

        Returns
        -------
        list
            Weapon names that exactly match the global variable ``query_attributes``.
        """
        list_of_weapons_with_query_attributes = []
        for weapon in self.weapons.items():
            if (
                weapon[1]["基础"] == query_attributes[0]
                and weapon[1]["附加"] == query_attributes[1]
                and weapon[1]["技能"] == query_attributes[2]
            ):
                list_of_weapons_with_query_attributes.append(weapon[0])
        return list_of_weapons_with_query_attributes

    def print_weapons_with_query_attributes(self):
        """
        Print weapons matching the queried matrix attribute combination.

        Results are printed to standard output.
        """
        self.check_query_attributes()
        list_of_weapons = self.get_weapons_with_query_attributes()
        print(f"\n查询基质 {query_attributes}: ")
        print("-------------------------")
        if len(list_of_weapons) != 0:
            print(list_of_weapons)
        else:
            print("无符合的武器")

    def run(self):
        """
        Run the complete query workflow.
        """
        self.get_weapons_in_fields()
        self.print_weapons_in_fields()

        self.get_strategies_in_fields()
        self.print_strategies_in_fields()

        self.print_query_weapon_strategy()

        self.print_weapons_with_query_attributes()

        # if all_weapons:
        #     for weapon in weapons:
        #         global query_weapon
        #         query_weapon = weapon
        #         self.print_query_weapon_strategy()


if __name__ == "__main__":
    optimizer = EndfieldOptimizer(field_map, weapons)
    optimizer.run()
