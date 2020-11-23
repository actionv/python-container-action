<p align="center">
  <a href="https://github.com/actionv/python-container-action">
    <img src="./images/logo.png">
  </a>
</p>
<h1 align="center">基于 Python 容器的 GitHub Actions 模板</h1>

<div align="center">

[![actions status](https://github.com/actionv/python-container-action/workflows/Lint/badge.svg)](https://github.com/actionv/python-container-action/actions) [![release](https://img.shields.io/github/v/release/actionv/python-container-action.svg)](../../releases) [![license](https://badgen.net/github/license/actionv/python-container-action)](./LICENSE) [![PRs Welcome](https://badgen.net/badge/PRs/welcome/green)](../../pulls)

</div>

这是一个用于快速创建 GitHub Actions 的模板，里面包含一段 Python 小程序，该应用程序内置到了 Container Action 中。

在 [`main.py`](main.py) 文件中有一个小示例，展示了如何获取 Action 输入参数并返回 Action 输出。

如果你想基于 Python 容器开发 GitHub Actions，可以在[当前仓库](https://github.com/actionv/python-container-action)上点击 <kbd>[Use this template](https://github.com/actionv/python-container-action/generate)</kbd>，基于当前模板创建一个新的存储库。

## 使用

在此处描述如何使用你的 Action。

### Workflow 示例

```yml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run action

        # 放置你的 Action 仓库
        uses: username/myaction@main

        # Action 的输入参数
        with:
          username: yanglbme
```

### 入参

| 参数     | 描述   | 是否必传 | 默认值 |
| -------- | ------ | -------- | ------ |
| username | 用户名 | 是       | -      |
| age      | 年龄   | 否       | 18     |

### 出参

| 参数 | 描述 |
| ---- | ---- | ------------ |
| res  |      | 一个输出参数 |

## 实例

### 输入

```yml
with:
  username: yanglbme
  age: 99
```

### 输出

```yml
steps:
- uses: actions/checkout@v2
- name: Run action
  id: myaction

  # 放置你的 Action 仓库
  uses: me/myaction@main

  # Action 的输入参数
  with:
    username: yanglbme

# 演示如何使用 Action 的输出
- name: Check outputs
    run: |
    echo "Outputs - ${{ steps.myaction.outputs.res }}"
```

## License

MIT
