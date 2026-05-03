#!/usr/bin/env python3
import argparse
from textwrap import dedent

OPENING_MAP = {
    "情感共鸣型": "故事起手 / 场景起手",
    "知识解释型": "问题起手 / 反常识起手",
    "热点评论型": "热点起手 / 观点先给",
    "职场成长型": "高频场景起手 / 朋友一句话起手",
    "搞钱/副业型": "提问起手 / 误区起手",
    "自媒体复盘型": "结果先给 / 踩坑起手",
}

STRUCTURE_PARTS = {
    "情感共鸣型": ["先写具体场景", "再命名情绪与处境", "最后给判断与收束"],
    "知识解释型": ["先把问题说清", "再拆误解和原因", "最后给结论和应用"],
    "热点评论型": ["先交代事件", "再解释机制", "最后落到普通人影响与观点"],
    "职场成长型": ["先写困境", "再写机制与代价", "最后给出路判断"],
    "搞钱/副业型": ["先写焦虑或困惑", "再拆误区", "最后给路径与合理预期"],
    "自媒体复盘型": ["先交代背景目标", "再写动作与结果", "最后抽象经验"],
}

ENDING_MAP = {
    "情感共鸣型": "金句收束 + 提问 / 转发提示",
    "知识解释型": "判断句收束 + 行动提示",
    "热点评论型": "立场判断 + 提问",
    "职场成长型": "判断句收束 + 转发点",
    "搞钱/副业型": "行动提示 + 提问",
    "自媒体复盘型": "经验总结 + 提问",
}


def build_outline(topic: str, content_type: str, audience: str, goal: str) -> str:
    opening = OPENING_MAP.get(content_type, "问题起手")
    parts = STRUCTURE_PARTS.get(content_type, ["先定义问题", "再拆解原因", "最后给结论"])
    ending = ENDING_MAP.get(content_type, "判断句收束")

    return dedent(f"""
    ## 文章骨架
    - 主题：{topic}
    - 内容类型：{content_type}
    - 目标人群：{audience}
    - 主传播目标：{goal}

    ### 开头设计
    - 推荐起手：{opening}
    - 前三句任务：抓注意力 / 确认相关性 / 给阅读理由

    ### 正文结构
    1. {parts[0]}
    2. {parts[1]}
    3. {parts[2]}

    ### 小标题建议
    - 第一部分：把问题拉近到读者身上
    - 第二部分：解释真正关键点或误区
    - 第三部分：给结论、路径或可执行动作

    ### 结尾设计
    - 推荐方式：{ending}
    - 必须完成：回题 / 留下可转述判断 / 给互动或转发理由
    """).strip()


def main():
    parser = argparse.ArgumentParser(description="Assemble article outline")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--content-type", required=True)
    parser.add_argument("--audience", required=True)
    parser.add_argument("--goal", default="高打开 + 高转发")
    args = parser.parse_args()
    print(build_outline(args.topic, args.content_type, args.audience, args.goal))


if __name__ == "__main__":
    main()
