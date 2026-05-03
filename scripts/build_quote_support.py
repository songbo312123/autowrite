#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
from textwrap import dedent

BASE_DIR = Path(__file__).resolve().parent.parent
LIBRARY_PATH = BASE_DIR / "assets" / "引用库.json"


def load_library():
    return json.loads(LIBRARY_PATH.read_text(encoding="utf-8"))


def suggest(topic: str, content_type: str | None = None):
    library = load_library()
    hits = []
    for item in library:
        topic_hit = any(key in topic for key in item.get("topic", []))
        type_hit = True if not content_type else content_type in item.get("fit_types", [])
        if topic_hit and type_hit:
            hits.append(item)
    if hits:
        return hits

    if content_type:
        typed = [item for item in library if content_type in item.get("fit_types", [])]
        if typed:
            return typed[:3]
    return library[:3]


def markdown(topic: str, content_type: str | None = None):
    items = suggest(topic, content_type)
    blocks = []
    for item in items:
        blocks.append(dedent(f"""
        ### 引用建议
        - 适配主题：{' / '.join(item['topic'])}
        - 来源：{item['source']}
        - 作者 / 作品：{item['author_or_work']}
        - 可用内容：{item['quote']}
        - 适合论证：{item['use_for']}
        - 适合类型：{' / '.join(item['fit_types'])}
        - 可靠性：{item['reliability']}
        - 使用提醒：{item['warning']}
        """).strip())
    return "\n\n".join(blocks)


def main():
    parser = argparse.ArgumentParser(description="Suggest quote support for article argument")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--content-type")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = parser.parse_args()
    items = suggest(args.topic, args.content_type)
    if args.format == "json":
        print(json.dumps(items, ensure_ascii=False, indent=2))
    else:
        print(markdown(args.topic, args.content_type))


if __name__ == "__main__":
    main()
