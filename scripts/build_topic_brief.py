#!/usr/bin/env python3
import argparse
import json
from textwrap import dedent

TYPE_MAP = {
    "情感": "情感共鸣型",
    "知识": "知识解释型",
    "热点": "热点评论型",
    "职场": "职场成长型",
    "搞钱": "搞钱/副业型",
    "副业": "搞钱/副业型",
    "复盘": "自媒体复盘型",
    "自媒体": "自媒体复盘型",
}

EMOTION_HINTS = {
    "情感共鸣型": ["委屈", "被忽视", "想被理解"],
    "知识解释型": ["好奇", "想搞懂", "认知升级"],
    "热点评论型": ["困惑", "判断欲", "表达欲"],
    "职场成长型": ["消耗感", "焦虑", "想找出路"],
    "搞钱/副业型": ["收入焦虑", "希望感", "不甘心"],
    "自媒体复盘型": ["想突破", "想复制", "少踩坑"],
}

TITLE_DIRECTIONS = {
    "情感共鸣型": ["人群+共鸣", "关系冲突", "情绪判断"],
    "知识解释型": ["问题式", "反常识式", "讲清楚承诺"],
    "热点评论型": ["热点+观点", "事件背后", "普通人相关性"],
    "职场成长型": ["打工人标签", "痛点判断", "反常识解释"],
    "搞钱/副业型": ["收益感", "误区纠偏", "路径判断"],
    "自媒体复盘型": ["结果先给", "复盘踩坑", "可复制动作"],
}

STRUCTURE_MAP = {
    "情感共鸣型": "场景—感受—判断—收束",
    "知识解释型": "问题—原因—拆解—结论",
    "热点评论型": "事件—解读—影响—观点",
    "职场成长型": "困境—机制—代价—出路",
    "搞钱/副业型": "问题—误区—方法—预期",
    "自媒体复盘型": "背景—动作—结果—经验",
}


def normalize_type(raw: str) -> str:
    if raw in TYPE_MAP.values():
        return raw
    return TYPE_MAP.get(raw, raw)


def build_brief(topic: str, audience: str, content_type: str, goal: str, style: str) -> dict:
    normalized = normalize_type(content_type)
    return {
        "topic": topic,
        "audience": audience,
        "content_type": normalized,
        "goal": goal,
        "style": style,
        "emotion_hints": EMOTION_HINTS.get(normalized, []),
        "title_directions": TITLE_DIRECTIONS.get(normalized, []),
        "recommended_structure": STRUCTURE_MAP.get(normalized, "问题—原因—拆解—结论"),
        "brief_markdown": dedent(f"""
        ## 选题简报
        - 主题：{topic}
        - 目标人群：{audience}
        - 内容类型：{normalized}
        - 主传播目标：{goal}
        - 风格倾向：{style}

        ### 建议触发情绪
        - {' / '.join(EMOTION_HINTS.get(normalized, ['相关性', '表达欲']))}

        ### 推荐标题方向
        - {' / '.join(TITLE_DIRECTIONS.get(normalized, ['情绪共鸣', '干货收益', '悬念反差']))}

        ### 推荐正文结构
        - {STRUCTURE_MAP.get(normalized, '问题—原因—拆解—结论')}
        """).strip()
    }


def main():
    parser = argparse.ArgumentParser(description="Build topic brief for enterprise writing skill")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--audience", required=True)
    parser.add_argument("--content-type", required=True)
    parser.add_argument("--goal", default="高打开 + 高转发")
    parser.add_argument("--style", default="清楚、真实、可传播")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = parser.parse_args()

    result = build_brief(args.topic, args.audience, args.content_type, args.goal, args.style)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["brief_markdown"])


if __name__ == "__main__":
    main()
