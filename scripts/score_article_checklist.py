#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CHECKS = {
    "title": ["# ", "## 标题候选"],
    "summary": ["## 摘要"],
    "body": ["## 正文"],
    "viral_analysis": ["## 为什么它可能成为爆款"],
    "structure_hint": ["### 一、", "### 1.", "### 第一部分"],
    "interaction": ["欢迎留言", "你最", "如果你身边也有", "把这篇", "先别急着"],
}


def score_text(text: str):
    results = {}
    score = 0
    for key, markers in CHECKS.items():
        passed = any(marker in text for marker in markers)
        results[key] = passed
        score += 5 if passed else 0

    length_score = 5 if len(text) >= 2500 else 0
    paragraph_score = 5 if text.count("\n\n") >= 12 else 0
    score += length_score + paragraph_score
    results["length_enough"] = bool(length_score)
    results["mobile_readable"] = bool(paragraph_score)

    return {
        "score": score,
        "max_score": 40,
        "checks": results,
        "summary": judge(score),
    }


def judge(score: int) -> str:
    if score >= 34:
        return "强稿，可直接作为高质量样稿"
    if score >= 28:
        return "可发，还可继续增强传播点"
    if score >= 20:
        return "结构基本完整，但传播力不足"
    return "建议重搭标题或结构"


def main():
    parser = argparse.ArgumentParser(description="Score article by checklist")
    parser.add_argument("file", help="Markdown article path")
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    print(json.dumps(score_text(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
