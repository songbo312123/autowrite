# Scripts

第二阶段把重复动作脚本化，目的是让企业版 skill 不只是知识库，还能稳定生成中间资产。

## 当前脚本

### build_topic_brief.py
输入主题、人群、内容类型、目标，输出标准选题简报。

示例：
```bash
python scripts/build_topic_brief.py \
  --topic "为什么很多人越努力越焦虑" \
  --audience "上班族" \
  --content-type "职场" \
  --goal "高打开 + 高转发"
```

### assemble_article_outline.py
根据内容类型拼装文章骨架。

示例：
```bash
python scripts/assemble_article_outline.py \
  --topic "普通人为什么总觉得自己执行力差" \
  --content-type "知识解释型" \
  --audience "成长型读者"
```

### score_article_checklist.py
对已有文章做基础 checklist 打分。

示例：
```bash
python scripts/score_article_checklist.py \
  "/path/to/article.md"
```

### build_quote_support.py
为主题生成可选的经典引用辅助建议，默认读取 `assets/引用库.json`。

示例：
```bash
python scripts/build_quote_support.py \
  --topic "判断力与方向感" \
  --content-type "知识解释型"
```

可维护资产：
- `assets/引用库.json`
- `assets/引用卡模板.md`
- `references/12-经典引用与文学论证规则.md`

### build_scene_support.py
为主题生成可选的桥段转述辅助建议，默认读取 `assets/桥段转述库.json`。

示例：
```bash
python scripts/build_scene_support.py \
  --topic "稳定和不甘之间的拉扯" \
  --content-type "职场成长型"
```

可维护资产：
- `assets/桥段转述库.json`
- `assets/桥段转述卡模板.md`
- `references/13-桥段转述规则.md`

## 热点专项资产

### AI 热点
- `references/15-AI热点写作规则.md`
- `assets/AI热点角度库.json`
- `assets/AI热点角度卡模板.md`

用途：
- 优先为 AI 热点提供可写角度
- 把 AI 话题从工具新闻翻译成普通人的工作、能力、收入和焦虑问题
- 服务知识解释型、职场成长型、搞钱/副业型和热点评论型内容

## 设计原则

- 脚本只做稳定、重复、格式化动作
- 标题、正文、爆款判断仍由模型完成
- 能脚本化的先做中间层，不急着把整篇文章自动化
- 所有引用建议都应二次核验，避免伪名言和错引
