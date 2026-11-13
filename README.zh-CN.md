# learning-assistant

以任务 / 题目为驱动的学习指导 Skill。实用优先，不追求广度，适合时间紧的场景，同时保留足够的深度，让知识在任务完成或考试之后仍然留得下来。

[English](README.md) | 简体中文

## 它不是什么

不是把一门学科从头系统讲一遍的导师。它确立一个可验收的目标，找出用户已有知识里夹生的部分，只补目标真正需要的基础，用任务和题目验证是否真的学懂，并留下短小、互相链接的笔记供日后复习。

## 目录结构

```
learning-assistant/
├── SKILL.md                          元数据、核心循环、选择判定表、资源索引
├── references/
│   ├── general-learning.md           通用规则（每次激活都会读）
│   ├── code-learning.md              代码专属规则（仅判定时读）
│   ├── presentation.md               图形化、内联卡片、降级
│   └── knowledge-network.md          长期知识网络笔记与可选的笔记工具增强
├── demo/
│   ├── inline-card-basic.html        领域中性卡片示例
│   └── inline-card-code-quiz.html    代码专属卡片示例
└── evals/
    └── trigger-queries.json          20 条触发评测（含近似负例）
```

`SKILL.md` 是唯一索引。各 reference 自包含、互不引用，因此文件引用始终保持一层。

## 触发方式

用户想学、想被教、想被考、想定学习目标，或想补实"学过但没真懂"的内容时激活——包括泛泛的「我想学 X」和「期末速成」。

不激活的场景：一次性概念问答、单纯的任务代做（改 bug、跑测试、生成文件、查某个 API 用法）、以及用户明确只要答案。

代码专属规则只在用户**明确表达想学会 / 想理解代码**时加载；意图含糊时先问一句再决定。其他学科使用通用层。

## 安装

把本目录复制到你的 agent 的用户级 skills 目录，例如：

```bash
cp -r learning-assistant ~/.workbuddy-ai/skills/
```

然后新开一个会话，Skill 才会出现在可用技能列表里。有些安装器会把技能放到别的目录（例如 `~/.codebuddy/skills/`），要确认副本最终落在当前 agent 真正读取的那个目录中。

## 可选工具

全部都是增强项，都有纯 Markdown 降级路径，不是必需。

- **answer-me-with-html** — 单页 HTML 讲解页。它的 CLI 是技能目录内的脚本，不保证存在全局 `am` 命令。安装指引：https://github.com/QingYunA/answer-me-with-html/blob/main/INSTALL.md
- **Obsidian** — 双链、properties、`.canvas` 关系图。纯 Markdown 加 `[[wikilinks]]` 是必需的最低形态。
- **对话内联卡片** — 需要宿主提供主题变量与消息回传接口；缺失时退化为文字选项或可复制的提示词。
