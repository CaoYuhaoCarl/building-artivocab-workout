---
name: group_format_template
description: Must strictly follow the following example markdown format below and ensure all fields are correctly populated when being triggered.
---

在套用下面模板时，优先给“词族明显、迁移价值高、课堂上容易连带讲解”的词补一行简洁的 `派生词:`。
控制在 1–3 个高价值 family members；不是每个词都要有，但这类词不要长期漏掉。

```
## **Group x**
共20词 (简单:X, 中等:X, 难:X, 超难:X)

**word1** /word1_phonetic/ [word_frequncy(COCA rank)]

n.装置；设备；方法；策略；手段
例句: I can't believe I have to wear this device on my arm for the next month.

──────────────────────────────

**word2** /word1_phonetic/ [word_frequncy(COCA rank)]

n.装置；设备；方法；策略；手段
例句: I can't believe I have to wear this device on my arm for the next month.
派生词: word2ed[ARTICLE_FORM]; word2ing adj. 示例派生; word2er n. 示例派生

──────────────────────────────

...

**word20** /word1_phonetic/ [word_frequncy(COCA rank)]

n.装置；设备；方法；策略；手段
例句: I can't believe I have to wear this device on my arm for the next month.

──────────────────────────────
```

> **派生词: 示例说明**（实际输出时删除此注释块）
> 下面是一个包含所有字段的完整真实条目范例，供格式参考：
>
> ```
> **survive** /səˈvaɪv/ [2800]
>
> v. 在……中活下来；幸存；继续存在
> 例句: Very few businesses survived the economic crisis.
> 派生词: survived[ARTICLE_FORM]; survival n. 幸存; survivor n. 幸存者
>
> ──────────────────────────────
> ```
>
> `派生词:` 规则：
> - 仅对词族明显、迁移价值高的词添加，不强制每条都有
> - 控制在 1–3 个高价值 family members
> - 文中使用的屈折/派生形式优先列入，帮助学生建立headword与原文的联系
> - **标记规范**：文中实际出现的形式,在派生词中用 `[ARTICLE_FORM]` 标记(替代旧版的 `（文中形式）`)。`[ARTICLE_FORM]` 是 sentinel,后期可在编辑器中一键查找替换为任意展示文案(如 `（原文形式）`、`*`、删除等)

> **更多条目示例**（不同形态覆盖：含派生词 / 不含派生词 / 搭配为主）
>
> ```
> **scarce** /skers/ [4500]
>
> adj. 稀缺的；不足的
> 例句: Clean water is becoming increasingly scarce in many regions.
> 搭配: scarce resources / scarce supply
>
> ──────────────────────────────
> ```
>
> ```
> **launch** /lɔːntʃ/ [1200]
>
> v. 发起；推出；发射
> 例句: The government launched a new campaign to reduce plastic waste.
> 搭配: launch a campaign / launch a product / launch an investigation
> 派生词: launched[ARTICLE_FORM]; launcher n. 发射器
>
> ──────────────────────────────
> ```
