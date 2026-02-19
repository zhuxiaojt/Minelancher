# Minelancher

## 概述

Minelancher是一款Minecraft启动器，使用GPLv3协议进行开源。

此项目目前处于编写中，未完成主要功能。

## 技术栈与代码结构

项目采用Python全栈开发，对于UI框架，我们使用了PyQt5，具体结构如下：

```
Minelancher/
├── MLCore/                 //后端核心，目前暂未开发
├── assets/                 //资源文件
│   └── logo/
│       ├── logo128.png
│       ├── logo16.png
│       ├── logo256.png
│       ├── logo32.png
│       └── logo64.png
├── main.py                 //程序入口
└── ui/                     //前端核心
    ├── UIMain.py
    ├── __init__.py
    ├── layout/
    │   ├── AppHeader.py    //标题栏相关代码
    │   ├── AppSidebar.py   //侧边栏相关代码
    │   └── __init__.py
    ├── locales/            //多语言预留，目前暂未真正适配
    │   ├── __init__.py
    │   ├── langs.json
    │   └── zh-CN.json
    └── pages/              //页面相关代码
        ├── __init__.py
        ├── base_page.py    //页面基类
        └── home_page.py    //主页
```

## 代码规范

目前暂无统一的规范，仅要求代码能够运行。

## 贡献

本项目为开源项目，任何人均可在本项目中提出建议、提交PR。

特别的，本项目不反对你使用AI编写代码，也没有像“人类贡献必须比AI多”的要求，但是你必须对代码进行测试，保证代码没有出现问题，不要把AI作为代码出问题的借口。

要参与本项目的开发，你需要以下环境：

- Python 3.x
- PyQt5
- Git

提交前，务必在本地对最新代码进行足够的测试。

## 代码审查

本项目的审查没有特别的规范要求，现阶段审查核心是“代码能够运行且实现功能”。

请在报告审查结果时使用中文或中英文双语报告，而非仅报告英语。

