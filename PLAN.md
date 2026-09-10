# 方案：工具创建器 + 代码型工具的圆桌演示

面向 Fan et al. *Calling the Tools* (ES&T Viewpoint) 的 SI 演示。
本文件是实现前的方案，不是文档；实现完成后并入 README。

---

## 0. 范围与原则

**这一轮做两件事：**

1. 一个**独立的工具创建器页面**，把"造方法"和"用方法"分开
2. 圆桌侧的最小改动，让 ¶29 描述的 code-based 交互真的能发生

**不做：** 向量库 / RAG、跨代理直接调用对方的工具、圆桌界面重构、测试框架。

**架构：一个后端，两个页面，靠 `tools/` 文件夹交接。**

```
/            index.html       圆桌 —— 用方法
/toolcreator  toolcreator.html  工具创建器 —— 造方法
tools/       <name>.py + <name>.json    两者唯一的接口
```

两个页面之间不共享任何运行时状态。工具注册表是**文件系统里的实物**，
可以进 git、可以直接汇总成 SI 的 `tools.json`。

---

## 1. 工具包的格式

一件工具 = 一个脚本 + 一份规格，同名成对放在 `tools/`。

### 1.1 执行契约（不变）

脚本从 stdin 读一个 JSON 对象，往 stdout 写一个 JSON 对象。
以 `tools/` 为工作目录运行，数据文件放同一目录用相对路径读。

### 1.2 规格 `<name>.json`

```json
{
  "name": "sec_ro",
  "title": "Specific energy consumption, single-stage RO",
  "description": "Closed-form SEC for a single-stage reverse osmosis process.",
  "runtime": "python",
  "parameters": [
    {"key": "pi_feed_bar", "type": "number", "unit": "bar", "required": true,
     "resolution": "design point, one feed composition",
     "description": "Feed osmotic pressure"},
    {"key": "recovery", "type": "number", "unit": "-", "required": true,
     "range": [0.05, 0.85], "description": "Permeate recovery ratio"},
    {"key": "pump_eff", "type": "number", "unit": "-", "required": false,
     "default": 0.8, "range": [0.3, 0.95], "description": "High-pressure pump efficiency"}
  ],
  "returns": {
    "sec_kWh_per_m3": {"type": "number", "unit": "kWh/m3"}
  },
  "conditions": "必填。方法成立的条件与边界，界面上永不折叠、永不截断。",
  "provenance": {
    "class": "published",
    "citation": "Fan et al., Nature Water 2026, Box 1",
    "note": ""
  },
  "examples": [
    {"args": {"pi_feed_bar": 2.1, "recovery": 0.75, "pump_eff": 0.8},
     "result": {"sec_kWh_per_m3": 0.42},
     "note": "typical brackish design point"}
  ]
}
```

**三个字段是这个方案的重点：**

- **`conditions` 必填。** 为空 → 该工具标记为**未就绪**，不进圆桌的提示词。
  这是文章的立场：没写清成立条件的方法不算方法。
- **`provenance.class` 二选一**：`published`（有出处，代码只是胶水）
  或 `model_drafted`（模型起草，未经验证）。后者在界面和导出里带醒目标记。
- **`parameters[].resolution`** —— 没有分辨率声明，就暴露不出 Fan↔Qiu 那类缺口：
  它们不是"缺一个数"，是"缺一个在正确尺度上的数"。

**`examples` 一次服务三件事**：教模型怎么调（首次调用成功率）、
一键回归测试、SI 里方法条目自带的验证算例。

---

## 2. 工具创建器页面 `/toolcreator`

**独立页面，在新标签页打开。** 圆桌页面上一个链接 `Tool creator ↗`，
每件工具有自己的 URL（`/toolcreator?tool=damage`），可以同时开几个标签页：
圆桌在跑，装配在另一个标签里进行，互不干扰。

### 2.1 核心：装配是一场对话，不是一个表单

一次性输入说不清一个真方法——干旱损害模型不是一段话能定义的：哪个区域？
哪些排放物种？估值取什么？分辨率是什么？必须来回问。

**对话的另一端是这一席自己的 agent**，用它自己的 api 配置、带着它自己的知识库。
不是通用代码助手：Agent-Q 读 Qiu 的论文，为 Qiu 的方法造工具。
它可以在装配途中 `@lookup` 自己的语料确认某个系数的定义，而不是凭我们打的字。

```
┌──────────────┬───────────────────────────┬────────────────────┐
│ TOOLS        │ 与 Agent-Q 的装配对话      │ DRAFT              │
│              │                            │ ┌────┬────┬────┐  │
│ ● sec_ro     │ [附件] Qiu2023.md          │ │Spec│Code│Test│  │
│ ○ damage ◄   │        2_historical_dam.R  │ └────┴────┴────┘  │
│              │                            │                    │
│ + New        │ Q: 你想让哪一部分可调用？   │ name: damage       │
│              │    我看到三段可以独立成立…  │ params: …          │
│ ─────────    │                            │ conditions: …      │
│ 附件         │ 你: 从能量到损害那一段      │   conditions: …    │
│ ▸ 阅读材料   │                            │                    │
│ ▸ 运行时数据 │ Q: @write_spec {…}         │ [Accept] [Discard] │
│              │    @write_code ```python…   │                    │
│              │    @run {"energy_MWh":…}    │ examples  2 ✓      │
│              │    → 报错，我改一下          │                    │
└──────────────┴───────────────────────────┴────────────────────┘
```

### 2.2 装配对话里的三个动词

复用圆桌里现成的截获循环：

| 动词 | 作用 |
|---|---|
| `@write_spec: {json}` | 提出/更新规格 |
| `@write_code:` ` ```python … ``` ` | 提出/更新脚本 |
| `@run: {args}` | **跑一遍自己刚写的脚本，看到报错自己改** |

第三个是关键：装配 agent 能自测。圆桌里"工具失败 → 原文回喂 → 自己纠正"
那套机制在这里直接复用。（本机执行、限定在 `tools/`、30 秒超时。）

### 2.3 两种附件，性质完全不同

- **阅读材料** —— 进对话上下文，让 agent 理解方法（论文 md、R 脚本、推导）
- **运行时数据** —— 存进 `tools/`，让脚本运行时打开（系数表、训练好的模型）

界面上分两栏，不要混。大 CSV 只送表头 + 前 N 行 + 统计摘要，不要整表进上下文。

### 2.4 草稿 → 落盘

对话改的始终是**草稿**。点 **Accept** 才写进 `tools/`。

**（实现时去掉了具名审阅。）** 原方案要求勾一个"我已审阅"的框并把 `reviewed_by`
写进 spec。实做后判断是：**在自己的工具里敲自己的名字什么也证明不了**，
而验证签名的身份不该由这个系统承担。artifact 里保留的是让读者**自己**做出这个判断
所需要的一切——conditions、每个参数与返回值的分辨率、provenance，以及产出它们的那场
装配记录。`/accept` 把这些全部打印出来再写盘，所以它们同时落在记录里。

### 2.5 怎么知道装配出来的工具是对的

这是整个设计最大的风险：**它会产出一个文档精美、条件写得头头是道、
但实际是错的模型。**

最有力的检验是让 `examples` 不只是用法示例，而是**用论文自己报告的数字做回归测试**：

> Qiu et al. 报告 2001–2021 西部干旱导致的累计损害是 X（在 SCC=Y、贴现率=Z 下）。
> 用这套参数跑装配出来的工具，能不能复现 X？

**复现不出来，这个工具就是错的**，无论条件写得多好看。
一键重跑所有 examples 就是这个检验。

### 2.6 装配记录导出

整场装配对话存成 `tools/<name>.build.md`：附件清单、往来对话、
每次 `@run` 的参数与返回、最终 spec。

**这份记录是 SI 的一部分**——它是"研究者没写代码，但保留了判断"
这句话唯一的证据。手写脚本给不出它。

### 2.7 一个连带简化

有了正式的 `spec.json`，**圆桌的开卷不再需要读脚本生成工具卡**——直接加载 spec。
少一次模型调用，也少一个漂移来源（现在卡片是模型每次重写的，可能和代码不一致）。

### 2.8 后端新增

```
GET    /toolcreator            toolcreator.html
GET    /api/tools            列出 tools/ 下的工具（名称、状态、mtime）
GET    /api/tools/{name}     返回 script + spec + build log
PUT    /api/tools/{name}     保存 script / spec / build log
DELETE /api/tools/{name}
POST   /api/tool             运行（已存在，增加 runtime 字段）
```

`runtime` 支持 `python`（`sys.executable`）与 `rscript`（`Rscript`）。
加 R 是因为 Qiu 的复现材料是 `.R`——**让原作者的代码原样跑起来，
比重写更贴合"把已有方法变成可调用的"这个论点。**

**安全底线：后端只绑 `127.0.0.1`。** 加了"模型写代码 + 自动执行"之后更不能改。

## 3. 圆桌侧的改动

### 3.1 四类标注

| 标签 | 数字来源 | 必须附带 |
|---|---|---|
| `[GROUNDED]` | 从知识库检索到 | 出处 |
| `[COMPUTED]` | 用**真实**参数跑出来 | 调用的函数与参数 |
| `[ASSUMED]` | 用**假设值**跑出来 | 假设了哪个量、取值、理由、敏感性 |
| `[EXTENDED]` | 没有依据的外推 | 可迁移假设及其成立条件 |

`EXTRAPOLATED` → `EXTENDED` 改名；导入同时认新旧两种，旧记录不失效。

### 3.2 三条硬规则（提示词）

- `@lookup` 的结果只能标 `[GROUNDED]`，**绝不能**标 `[COMPUTED]`。
- `[ASSUMED]` 必须在合理范围内**改变该假设值再跑一次**，报告结论是否随之改变。
  没有这一步，`[ASSUMED]` 就只是免责声明。
- `[EXTENDED]` 不被信任，**交回其所有者裁决**：若另一位参与者做出了落在
  你领域内的 `[EXTENDED]` 主张，你下一轮必须先裁决它。

### 3.3 仪器名录（新）

每席的 system prompt 里加一段——**只有名称、用途、输入输出及单位，不含
`conditions` 全文**：

```
# Instruments at this table
Agent-F — sec_ro:  takes pi_feed_bar[bar], recovery[-], pump_eff[-]
                   returns sec_kWh_per_m3[kWh/m3]
Agent-Q — damage:  takes energy_MWh[MWh], emission_factor[kgCO2/MWh],
                   ch4_leakage[-], scc[$/tCO2], discount_rate[-], ...
                   returns co2_t, ch4_t, mortality, total_usd
```

**这是最可能决定演示成败的一条。** 现在工具卡只进自己那席的提示词，
对方看不见——Agent-F 不会知道要去供给 kWh，Agent-Q 不会知道去要。
"参数开放"在文章里是名词，在代码里就是这段名录。

### 3.4 机械检查（新）

每轮结束后自动检查，不合格**在记录里打醒目旗标**，同时写进导出：

| 检查 | 触发条件 |
|---|---|
| C1 | 出现 `[COMPUTED]` 但本轮零次工具调用 |
| C2 | 出现 `[ASSUMED]` 但本轮工具调用 < 2（没做敏感性） |
| C3 | 整条发言一个标签都没有 |

**模型不照做的时候，你不会以为它照做了。** 这些旗标本身对文章有用——
它是"约束是否真的生效"的证据，无论结论朝哪边。

### 3.5 其他

- 每轮工具调用上限 **2 → 6**（第三步要扫贴现率 × 排放因子 = 4 次）
- 导出补上**工具返回值**（现在只存了调用参数）
- 导出末尾加**人工判读表**，一条主张一行：

```
| # | Speaker | Tag | Claim | Basis shown | Tag correct? | Note |
|---|---------|-----|-------|-------------|--------------|------|
| 1 | Agent-F | GROUNDED | SEC 0.42 kWh/m3 | Fan 2026 §5 |  |  |
```

- 知识库仍走**开卷档案 + `@lookup` 按需查阅**（无向量库）。
  理由不是省钱：**"代理在什么时候决定去查证据"本身就是演示素材**，
  而且记录里那条 🔍 展开能看到取回的原文原样，正好满足
  "`[GROUNDED]` 必须附出处"。

---

## 4. 演示的两件工具

### 4.1 `sec_ro`（Agent-F）

```
sec_ro(pi_feed_bar, recovery, pump_eff=0.8) → {sec_kWh_per_m3}
```

域守卫：`recovery ∈ [0.05, 0.85]`、`pump_eff ∈ [0.3, 0.95]`，
越界 `sys.exit(msg)` 非零退出。

### 4.2 `damage`（Agent-Q）

```
damage(energy_MWh, emission_factor_kgCO2_per_MWh, ch4_leakage,
       scc_usd_per_tCO2, sc_ch4_usd_per_tCH4, vsl_usd,
       discount_rate, year, scenario)
    → {co2_t, ch4_t, mortality, climate_usd, health_usd, total_usd}
```

**必须加 `energy_MWh`。** 你原来的签名里没有能量输入，那么从 kWh 到 tCO₂
那一步只能在代理脑子里乘——**那就不是 `[COMPUTED]` 了，是心算。**

域守卫：`discount_rate ≥ 0`、`emission_factor` 无默认值必填。

`conditions` 里必须写明：**这是 Qiu et al. 2023 (PNAS) 的简化估值代理，
不是原模型。** 原模型是月 × 平衡区 × 机组的回归加 PM₂.₅ 浓度—反应函数；
此处压成闭式估值是大幅简化。

### 4.3 缺口是怎么冒出来的

`emission_factor_kgCO2_per_MWh` **必填、无默认值**，且 `resolution` 声明为
「平衡区 × 月 × **增量负荷**边际」。

于是：Agent-F 给出年耗电 → Agent-Q 要跑模型 → 发现缺这个参数 →
知识库里没有、对方也给不了 → 只能报告缺口 + 给条件性估计。

**缺口不需要额外机制，它是参数表的自然产物。** 要做的只是禁止它编一个数。

而且这个缺口是真的：Qiu 的模型估的是**干旱替代边际**（填补水电缺口的机组），
Fan 需要的是**增量负荷边际**（服务一度新增用电的机组）。两者在同一区域同一
季节可能接近，但**识别策略不同**——那个回归不是为了回答这个问题估的。
叠加分辨率错位（年 vs 月、厂级 vs 平衡区），就是 ¶29 那句话。

---

## 5. 四步交互，以及每步靠什么保证

| 步 | 内容 | 靠什么 |
|---|---|---|
| 1 | 一侧提供真实工况 | `@lookup` → `[GROUNDED]` + 出处 |
| 2 | 另一侧在这些条件下运行 | 仪器名录 + `@tool` → `[COMPUTED]` |
| 3 | 改参数检验稳健性 | 调用上限提到 6 + C2 检查 |
| 4 | 暴露缺口，给条件性估计 | 必填无默认参数 + `[ASSUMED]` + 敏感性 |

**第三步是整份规格里最有力的一条**——它给出了 code-based 相对 text-based
不可替代的理由（"结论在假设变化时是否成立"，任何陈述都答不了），
而这个理由在 Viewpoint ¶29 里还只是隐含的。

---

## 6. 施工顺序

| 序 | 内容 | 规模 | 状态 |
|---|---|---|---|
| A | 后端：工具注册表端点 + `rscript` 运行时 | 小—中 | ✅ 已完成 |
| B | `toolcreator.html`：装配对话 + 草稿区 + 测试台 | 中—大 | ✅ 已完成 |
| C | **用 B 的装配对话生成那两件工具**（附件：论文 + 复现代码） | 中（内容） |
| D | 圆桌：四标签、名录、结果账本、上限、机械检查 | 中 | ✅ 已完成 |
| E | 导出：账本 + 机械检查 + 人工判读表 | 小—中 | ✅ 已完成 |

**C 放在 B 之后是有意的**：让工具由装配产生而不是手写，
演示与论点才自洽，而且装配过程本身是 SI 材料。

### 参数出处：ASSUMED 不再由代理自选

账本上线后测出一个洞：代理编一个排放因子、跑真工具、拿到真数、报 `[COMPUTED from R1]`，
**四条检查全绿**——它们查的都是记账（跑没跑、引没引、标没标），没有一条能问
「你填进那个参数的 0.5 是哪来的」。选标签的自由度还在代理手里。

修法是让**调用本身带出处**：

```
@tool: {"ef_co2_t_per_MWh": {"v": 0.5, "src": "assumed"}}
```

`src` 三选一：`R7`（精确可验：值必须出现在 R7 的返回里）、`source`（弱验：档案 /
本轮 lookup / 记录）、`assumed`（不验，它是招供）。**裸值一律记 assumed**，
`source` 找不到也降级为 assumed。

于是 ASSUMED 是**推导的**，不是选的；标签也拆成两个正交的问题
（`[ASSUMED][COMPUTED from R7]`），比三选一好写也好查。C5 因此是精确的：
引用的那次运行是 ASSUMED，而发言里没有 `[ASSUMED]` → 打旗标，零启发式。

附带得到污染传播：R9 用了 ASSUMED 的 R7 → R9 也是 ASSUMED（via R7）。

仍然抓不到：`src: "R3"` 值确实在 R3 里、**但那是错误种类的量**。
出处解决「这个数哪来的」，不解决「这个数是不是正确种类的东西」。后者留给人。

### D/E 实施记录：数据移交用「结果账本 + 强制引用」

原方案只说了名录，没说一方算出的数怎么交到另一方手里。最后定的是**结果账本**：

- 任何人跑一次工具，自动登记 `[R1] Agent-F · sec_ro  args {...} → {...}  (returns: … [kWh/m3])`，
  账本注入**所有人**的提示词
- 别人要用这个数，必须写 `[COMPUTED from R1]`；工具返回时系统当场告诉模型
  「已登记为 R4，请以 [COMPUTED from R4] 报告」，所以引用永远做得到
- 机械检查 C4 抓没有 `[R…]` 的 `[COMPUTED]`

三个好处：单位跟着数字走；**抄来的数变得可检测**；导出里直接得到一张可人工核对的表。
散文移交做不到后两条。

另外，名录里的参数行**逐字保留 unit 与 resolution**——只有单位时两个 marginal 看起来可乘，
写了 resolution 才看得出「BA × month, drought-displacement」不是对方要的
「plant-level annual, incremental-load」。**缺口从参数表里长出来，没有额外机制。**

工具创建器一侧同步：装配对话的提示词里带上 `tools/` 里**其他工具的完整 spec + build.md 开头**，
`@peer: <name>` 可取全文。接口对不上，在造工具的时候就该发现，而不是等两个代理吵起来。

### B 的最终形态：终端，不是表单

方案里画的三栏（工具列表 / 装配对话 / 草稿区）实做后被砍成两栏。草稿仍然是状态，但**不再有面板**：
用 `/spec`、`/code` 读它，用一句话让 agent 改它，或者自己贴一个 `@write_spec` 块直接改。
`/` 是人，`@` 是 agent，两边共用同一个解析器。留下的唯一"面板"是输入框上方一行状态：

    damage · ✓ spec · ✓ code · ✓ conditions · ✓ units                       python

`/accept` 把该看的东西全打印出来再写盘：每个参数与返回值的单位和分辨率、
conditions 全文、provenance、软警告。判断仍然是人的事，但它不是 JSON 里的一个字段。

### B 实施时相对本方案的两处简化

1. **工具创建器里没有 `@lookup`。** 原方案让 agent 在装配时检索自己的知识库；实际做法是把论文、
   复现代码直接作为"阅读材料"附件送进对话。装配是一次性的、材料是你选定的，检索这层间接
   反而增加了失败面。圆桌里的 `@lookup` 不受影响。
2. **运行时数据文件不经工具创建器上传**，由你自己放进 `tools/`。脚本以该目录为工作目录，相对
   路径即可打开。理由：脚本读到的文件应当就是你放在磁盘上的那一份。
3. 附带修的一个坑：测试草稿要落盘才能执行，如果用真名写就会**用未审阅的草稿覆盖已 Accept
   的脚本**。现在草稿一律以 `_draft_<name>` 运行，Accept 时清除，注册表里也不显示。

---

## 7. 待定（我先按括号里的默认值写，随时可改）

1. `damage()` 加 `energy_MWh`（**加**）
2. 知识库走档案+查阅，还是整篇进上下文（**档案+查阅**）
3. 两个脚本由我起草还是你有现成的（**我起草占位版，你替换**）
4. 人工判读表粒度：一条主张一行 / 一次发言一行（**一条主张一行**）
5. `conditions` 为空即不可用——真的强制（**强制**）
6. 工具创建器的模型配置：单独填 / 默认借用圆桌第一席（**默认借用，可覆盖**）
7. 是否支持 R 运行时（**支持**）

已确认：装配记录导出为 `tools/<name>.build.md`（**要**）；
`@run` 允许 agent 执行自己刚写的代码（**允许**）；装配在独立页面（**新标签页**）。
