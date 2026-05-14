# building-artivocab-workout

<p align="center">
  <img src="assets/banner.png" alt="building-artivocab-workout banner">
</p>

<p align="center">
  <a href="#building-artivocab-workout"><img src="https://img.shields.io/badge/Harness-Agent%20Skill-2f855a?style=flat-square" alt="Harness: Agent Skill"></a>
  <a href="SKILL.md"><img src="https://img.shields.io/badge/version-1.0.0-2563eb?style=flat-square" alt="Version 1.0.0"></a>
  <a href="#安装方法"><img src="https://img.shields.io/badge/install-npx%20skills-f97316?style=flat-square" alt="Install with npx skills"></a>
</p>

> Article -> Vocabulary + Reading + Writing: 把一篇英语文章变成可直接上课/练习使用的全面训练。

`building-artivocab-workout` 是一个 skill，用来从新闻、短文或 Day_test 模板中生成结构化的中英双语阅读练习。它不只是挖空单词，而是围绕理解、语法敏感度、搭配、词形变化和输出迁移，生成一套完整的课堂训练材料。

## 安装方法

推荐使用 [`npx skills`](https://www.npmjs.com/package/skills) CLI 一键安装。它会自动识别你正在使用的 Agent（Claude Code、Codex、Gemini、Hermes、Openclaw等agent），并把 skill 放到对应目录。

```bash
npx skills add CaoYuhaoCarl/building-artivocab-workout
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
用 building-artivocab-workout 帮我把这篇文章做成词汇完形训练。<直接粘贴文章到这儿>
```

或：

```text
帮我做阅读练习题，包含词汇表、完形填空和答案高亮。<直接粘贴文章到这儿>
```

或：

```text
/building-artivocab-workout <直接粘贴文章到这儿>
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
├── LICENSE                          # MIT 开源协议
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

## 维护提示

- 修改执行逻辑时，优先更新 `SKILL.md`。
- 修改任务规则时，更新 `references/task_specs.md`。
- 修改输出目录或文件命名时，更新 `assets/config.md`。
- 修改 Task 1 格式时，更新 `assets/group_format_template.md`，并运行对应校验脚本。

## 推荐学习

如果你想把这个 skill 做成可复用的长期工作流，推荐先看这几份资料：

- **学习 skill 是什么**: [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) - Claude Help Center 对 skill 的概念、工作方式和适用场景做了快速解释。
- **学习如何创建标准 skill**: [Introduction to agent skills](https://anthropic.skilljar.com/introduction-to-agent-skills/434525) - Anthropic 课程，覆盖 `SKILL.md` frontmatter、目录组织、触发描述和分发。
- **理解 skill 与 hooks、subagents、MCP 的区别**: [Agent Skills with Anthropic](https://learn.deeplearning.ai/courses/agent-skills-with-anthropic/lesson/ldn5c3/introduction?startTime=0) - DeepLearning.AI 课程，从 tools、MCP、subagents 到组合式 agent workflow 做系统梳理。

## 开源协议

本项目基于 [MIT License](LICENSE) 开源。

Contact: X [@CaoYuhaoCarl](https://x.com/CaoYuhaoCarl) · Telegram [@caoyuhaocarl](https://t.me/caoyuhaocarl) · WeChat `caoyuhaocarl`
