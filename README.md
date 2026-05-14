# building-artivocab-workout

> Article + Vocabulary + Workout: 把一篇英语文章变成可直接上课使用的词汇完形训练。

`building-artivocab-workout` 是一个 Codex skill，用来从新闻、短文或 Day_test 模板中生成结构化的中英双语阅读练习。它不只是挖空单词，而是围绕理解、语法敏感度、搭配、词形变化和输出迁移，生成一套完整的课堂训练材料。

## 安装方法

推荐使用 `npx skills` CLI 安装。它会自动识别你正在使用的 Agent（Claude Code、Codex 等），并把 skill 放到对应目录。

```bash
npx skills add CaoYuhaoCarl/building-artivocab-workout
```

常用管理指令：

```bash
npx skills list                 # 查看已安装的 skills
npx skills find web-design      # 在仓库内搜索 skill
npx skills update               # 升级已安装的 skills
npx skills remove kb-retriever  # 卸载指定 skill
```

## 适合什么时候用

- 你有一篇英文文章，想提取核心词汇并做成阅读练习。
- 你想生成完形填空、词汇表、答案高亮和课堂输出任务。
- 你有一个 Day_test 风格的 Markdown 文件，想把任务区补完整。
- 你在做 Chinese EFL 阅读课，需要 B1 左右难度的可讲、可练、可检测材料。

## 它会产出什么

1. **Step 0**: B1 难度改写，或在文本已经合适时保留原文。
2. **Task 1**: 20 个核心词的 Group block。
3. **Task 2**: 对 20 个核心词进行全文标记。
4. **Task 3**: 选出 10 个检测词。
5. **Task 4**: 生成编号完形填空。
6. **Task 5**: 返回原文并只高亮 10 个答案词。
7. **Task 6**: 生成课堂输出激活任务。
8. **Task 7**: 生成写作和阅读高阶训练。

## 使用方式

把文章或 Day_test Markdown 文件交给 Codex，并提出类似请求：

```text
用 building-artivocab-workout 帮我把这篇文章做成词汇完形训练。
```

或：

```text
帮我做阅读练习题，包含词汇表、完形填空和答案高亮。
```

默认输出会保存到 `assets/config.md` 中配置的 `output_dir`，文件名采用：

```text
YYYY_MM_DD_article_name.md
```

## 项目结构

```text
.
├── SKILL.md                         # skill 入口与核心工作流
├── README.md                        # 项目说明
├── assets/
│   ├── config.md                    # 输出路径和命名规则
│   ├── day_test_template_v2.md       # Day_test 空白模板
│   └── group_format_template.md      # Task 1 词汇格式模板
├── references/
│   └── task_specs.md                # Step 0 与 Task 1-7 的详细规则
└── scripts/
    ├── build_output.py              # 组装最终 Markdown
    ├── validate_group_block.py       # 校验 Task 1
    └── validate_final_output.py      # 校验 Task 4 和 Task 5
```

## 设计原则

- **文章先行**: 所有任务都基于同一篇 worksheet article，避免词表、挖空和答案错位。
- **课堂可用**: 输出不仅能做题，还能引导复述、总结、因果表达和角色回应。
- **难度稳定**: 默认控制在 upper-A2/B1 到 B1 左右，保留必要事实和逻辑。
- **可验证**: 关键任务配有脚本检查，减少空数、编号、答案高亮等机械错误。

## 维护提示

- 修改执行逻辑时，优先更新 `SKILL.md`。
- 修改任务规则时，更新 `references/task_specs.md`。
- 修改输出目录或文件命名时，更新 `assets/config.md`。
- 修改 Task 1 格式时，更新 `assets/group_format_template.md`，并运行对应校验脚本。

