## Hanson的个人Blog

本项目兼容SAE环境, 直接push到自己的sae app中即可实现快速搭建.

### 快速开始:

强烈建议使用virtualenv, pyenv或docker等虚拟环境进行开发.

1.使用virtualenv搭建环境(Linux):

```shell
$bash: virtualenv .venv
$bash: source .venv/bin/activate
(.venv)$bash:
```

2.安装依赖组件:

```shell
(.venv)$bash: make develop
```

3.运行测试用例

```shell
(.venv)$bash: make test
```

> 你也可以手动执行py.test对某模块进行测试并查看测试覆盖情况, 如对`manage`模块的测试 :
> `py.test tests --cov=manage`
> 或生成html版本的覆盖结果 :
> `py.test tests --cov=manage --cov-report=html`

### 自动化:

使用`make [command]`快速搭建开发环境, 详见Makefile, **仅限于Unix平台**.

* `initdb`: 初始化数据库
* `test`: 使用pytest进行单元测试.
* `develop`: 安装工程的依赖组件.

### PS:
SAE上并没有预装SqlAlchemy, 为了能顺利运行项目, 我把SQLAlchemy 0.9.3整个模块放进了工程的代码库中, 比较脏, 但是谁让SAE这么傲娇呢.