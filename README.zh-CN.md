# learning-assistant

一个用来「快速学懂一件具体的事」的 Agent Skill。它先和你商定一个能验收的目标，找出你原有知识里夹生的地方，只补这个目标真正需要的基础，然后用让你动手的方式检验，最后留下两种东西：一份能接着往下讲的状态记录，和一个几天后还能打开复习的交互页面。

[English](README.md) | 简体中文

## 它能做什么

- **先定一个能验收的目标。** 不是「学电力电子」，而是「给定单相桥式全控电路、阻感负载、α=30°，能分区间说出导通器件、画出 u_d 与 i_d、不看资料算出 U_d」。后面所有判断都对着这个目标做。
- **先诊断，再讲。** 用一小套能区分深浅的问题（做成一张卡片）找出你真正薄弱或搞错的那一层，而不是把你会的东西再讲一遍。
- **只补目标需要的前置。** 如果断链在更基础的地方，它会先退回去修那一层，再回到你的目标。它不会从第一章顺着教材走。
- **靠让你动手来检验。** 预测、画图、解释、判断。反馈会指出你推理断在哪一层，而不只是对错。
- **留下两样东西。** 一份简短的状态记录，让下一次会话（或换一个模型）能接上；以及一个给你自己用的交互复习页。

## 和一般「AI 家教」的区别

大多数「AI 家教」类提示词的产物是一大段解释。这个 Skill 建立在相反的假设上：**读懂一段解释不等于学会**，而时间紧的时候，广度是最先该砍掉的东西。

- **一个目标，不是一门课。** 时间不够时，先砍广度，不砍诚实和验证。
- **深度是你选的。** 你选一档（够用 / 扎实 / 深入），它改变的是「覆盖多少」，而不是「要不要检验」。
- **错答是输入。** 笔记里记的是你实际犯的那个错；这个错以后会变成复习页上的一道干扰项。
- **不确定就说不知道。** 易变的结论要么给来源，要么明确标「未核实」。

## 适用场景

| 你的处境 | 可以这样说 |
| --- | --- |
| 几天后考试，内容太多 | 「期末速成，三天，只求过线」 |
| 学过，但一直没真懂 | 「这块我没真懂，一考试就错」 |
| 读别人写的代码 | 「逐行讲讲这段代码在干什么」 |
| 想学但不知道从哪下手 | 「我想学 X，但不知道从哪开始」 |
| 想知道自己忘了多少 | 「帮我复习一下 X，看我忘了多少」 |
| 某个概念反复绊倒你 | 「用你的方式给我讲一下 X」 |

## 不适用的场景

- 一次性的概念问答：「X 是什么」「一句话解释 X」。
- 单纯的任务代做：改这个 bug、跑测试、生成文件、查某个 API 用法。
- 你只想要答案，不关心推理过程。

这些情况它照常回答，不会开一节课。但如果你**明确要求**用它那套方式讲一个概念，它会走一个短版本——讲解、一次检查、反馈——不设目标、不做笔记、不排复习。

## 怎么用

直接说你想学什么、为什么学。它的第一轮回复通常会问四件事：

1. 目标是什么，要能用什么方式验收；
2. 需要多深，什么时候要用；
3. 有没有指定教材或考纲范围；
4. 问一次要不要用 Obsidian 管笔记（可选，默认关）。

然后它开始问你问题。答「不知道」是有用信息，不是失败——空着会被记为证据，它不会替你填。

### 会话中可以用的指令

| 说 | 效果 |
| --- | --- |
| `skip` | 跳过某个知识点，记为跳过，**永不**记为掌握 |
| `just tell me` | 只这一个问题不问你了，直接说答案 |
| `explain fully` | 暂停提问，系统讲一遍 |
| `deeper` / `lighter` | 调整深度档位 |
| `show progress` | 打印当前进度块 |
| `save state` / `resume from:` | 把进度带到新会话 |

## 你实际会看到什么

### 对话里的题目卡片

宿主支持交互卡片时，题目会以卡片形式出现，而不是一屏文字：单选、多选、填空、一题多空、一次多题的诊断题组。

每张卡片的流程一致：**判定在卡片内完成**（不会发出任何消息），随时可以写理由；点确认只发一条消息，含题干、你的作答、本地判定和你的解释；另外两个固定选项单独放在下面——

- `难度太高，需要大幅降低难度`
- `难度太低，可以快速提升难度`

这两个点了立刻发出，且从不参与判分。

### 讲解页，以及什么时候必须有图

内容里有分情况、有分支、有波形、有电路，或者需要同时抓住三个以上概念时，它会生成单页 HTML 讲解页，一种情况一个面板，并在回复正文里也给出结论。

图按内容选路线：波形和函数曲线用绘图库（matplotlib），复杂电路先找有依据的资料图，简单示意图手写 SVG。**一张属性表格不算图**——列表里写「电阻负载 u_d = 0 / 电感负载 u_d 变负」并没有把负值区间画在时间轴上。

### 两种笔记

- **`notes/N01-<知识点>.md`** —— 给助手读的状态记录：结论、你实际犯的错、关系、上次结果。它的读者是下一次接手的会话。
- **`review/R01-<知识点>.html`** —— 给你自己反复打开的页面：一页速记、关键图、错题重刷（点选项立即本地判定，连续两次答对才移出错题池）、知识关系图、跳转到相邻笔记的链接。离线可用，会记住你已经掌握了哪些。

两者同号、放在 `<CODE>-<科目>/{notes,review,explain,figures}` 下，三十个文件也不会乱。

复习页不上传任何东西：判定在页面里完成，进度存在你浏览器的本地存储里，「复制复习指令」只是复制一段文字。

## 安装

### 方式一：让你的 Agent 帮你装

把下面这段整个复制给你的 agent（Claude Code、WorkBuddy、Codex、Cursor、Gemini CLI 等）。它会在动手前先问你，装完自己检查结果。

```
请帮我安装一个 Agent Skill。

来源：https://github.com/DGTSAlight/learning-assistant
（如果这个地址打不开，先问我正确的地址，不要自己猜。）

1. 先确认我用的是哪个 agent，再找到它的用户级 skills 目录：
   WorkBuddy       ~/.workbuddy/skills/  或  ~/.workbuddy-ai/skills/
   Claude Code     ~/.claude/skills/
   Codex           ~/.codex/skills/
   OpenCode        ~/.config/opencode/skills/
   Cursor          ~/.cursor/skills/
   Gemini CLI      ~/.gemini/skills/
   GitHub Copilot  ~/.copilot/skills/
   CodeBuddy       ~/.codebuddy/skills/
   其他 agent：放在它发现 SKILL.md 文件的位置。
   如果你不确定是哪一个，先问我，不要直接写。

2. 下载这个仓库（git clone；没有 git 就下载 zip 解压），把里面的 learning-assistant
   文件夹整个复制进那个目录。最终必须是：
   <skills 目录>/learning-assistant/SKILL.md

3. 装完检查并告诉我结果：
   - SKILL.md 在正确位置、能打开
   - references/、assets/、scripts/、evals/ 都在
   - 没有多套一层目录（不要出现 learning-assistant/learning-assistant/）

4. 不要修改 SKILL.md 的内容，也不要装到我的 skills 目录以外的地方。

5. 告诉我接下来要做什么它才会生效——一般是新开一个会话。
```

### 方式二：手动安装

把本目录复制到你的 agent 的用户级 skills 目录；如果只想在单个仓库里使用，就放到该仓库的项目级目录。

| Agent | 用户级 | 项目级 |
| --- | --- | --- |
| WorkBuddy | `~/.workbuddy/skills/`（部分版本为 `~/.workbuddy-ai/skills/`） | `.workbuddy/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.codex/skills/`（同时读取 `~/.agents/skills/`） | `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.agents/skills/` |
| Pi | `~/.agents/skills/` | `.agents/skills/` |
| DSH（DeepSeek Harness） | `~/.dsh/skills/` | `.dsh/skills/` |
| Cursor | `~/.cursor/skills/` | `.agents/skills/` |
| Gemini CLI | `~/.gemini/skills/` | `.agents/skills/` |
| GitHub Copilot | `~/.copilot/skills/` | `.agents/skills/` |
| CodeBuddy | `~/.codebuddy/skills/` | `.codebuddy/skills/` |

```bash
git clone https://github.com/DGTSAlight/learning-assistant
cp -r learning-assistant ~/.workbuddy/skills/
```

如果你的 agent 不在表里，把目录放到该 agent 发现 `SKILL.md` 的位置即可。DSH 也可以用 `dsh plugin add` 作为插件安装。

然后新开一个会话，Skill 才会出现在可用技能列表里。

## 可选工具

全部都是增强项，都有纯 Markdown 降级路径，不是必需。

- **answer-me-with-html** —— 单页 HTML 讲解页。它的 CLI 是那个技能目录内的脚本，不保证存在全局 `am` 命令。安装指引：https://github.com/QingYunA/answer-me-with-html/blob/main/INSTALL.md
- **带 matplotlib 的 Python** —— 只有画波形和函数曲线时才需要。默认解释器没有的话，它会去你的 conda 环境和其他安装位置找，找到后可以帮你把它设成本项目的默认解释器。一个都没有时，退化为 SVG 示意图。
- **Obsidian** —— 双链、properties、`.canvas` 关系图。纯 Markdown 加 `[[wikilinks]]` 是必需的最低形态。
- **对话内联卡片** —— 需要宿主提供主题变量与消息回传接口；缺失时退化为文字选项或可复制的提示词。

## 目录结构

```
learning-assistant/
├── SKILL.md                          元数据、核心循环、选择判定表、资源索引
├── references/
│   ├── general-learning.md           通用规则（每次激活都会读）
│   ├── code-learning.md              代码领域（仅判定时读）
│   ├── mathematics.md                数学领域
│   ├── power-electronics.md          电力电子技术领域
│   ├── sensors.md                    传感器与检测领域
│   ├── presentation.md               讲解页、内联卡片、公式写法
│   ├── technical-figures.md          何时必须有图，以及怎么出图
│   ├── knowledge-network.md          笔记、复习页、可选的笔记工具
│   └── gates.md                      可选的硬门禁
├── assets/                           示例：题目卡片、复习页、波形图
├── scripts/                          可运行的波形脚本与可选门禁检查
└── evals/                            25 个触发用例 / 50 条查询，中英双语
```

`SKILL.md` 是唯一索引；各 reference 自包含、互不引用，文件引用始终只有一层。领域文件是可选的——只有通用层也能跑完一次会话，领域文件只是补上范围、顺序和判断标准。

## 适用范围与限制

- **它不替代你的教材。** 有考纲的课，它会先问用哪本教材、考到第几章，然后才引用。
- **效果取决于你说实话。** 没有经过检验的「我会了」只是一句声明，它会去测。
- **笔记是你的。** 写在你的项目目录里，不会写进 Skill 目录；Skill 自身不保存任何状态。
- **不上传任何东西。** 复习页是本地文件；除了你能看到的检索，Skill 本身没有额外的网络行为。

## 许可证

MIT，详见 [LICENSE](LICENSE)。
