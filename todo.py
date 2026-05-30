"""
命令行待办事项管理器
一个简单的记事工具，支持新增、查看、完成、删除任务。
数据保存在 JSON 文件中，关掉程序也不会丢失。
"""

import json
import os
from datetime import datetime

# 数据文件名
数据文件 = "todos.json"


def 加载数据():
    """从 JSON 文件读取待办事项"""
    if os.path.exists(数据文件):
        with open(数据文件, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def 保存数据(数据):
    """将待办事项写入 JSON 文件"""
    with open(数据文件, "w", encoding="utf-8") as f:
        json.dump(数据, f, ensure_ascii=False, indent=2)


def 新增任务(任务列表):
    """添加一条新任务"""
    内容 = input("请输入任务内容：").strip()
    if not 内容:
        print("任务内容不能为空！")
        return

    任务 = {
        "id": len(任务列表) + 1,
        "内容": 内容,
        "已完成": False,
        "创建时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    任务列表.append(任务)
    保存数据(任务列表)
    print(f"✅ 已添加：{内容}")


def 查看任务(任务列表):
    """显示所有任务"""
    if not 任务列表:
        print("📭 当前没有待办事项，轻松！")
        return

    print(f"\n{'=' * 50}")
    print(f"{'序号':<6}{'状态':<10}{'内容':<20}{'创建时间':<20}")
    print("=" * 50)

    未完成 = 0
    for 任务 in 任务列表:
        状态 = "✅ 已完成" if 任务["已完成"] else "⬜ 待办"
        if not 任务["已完成"]:
            未完成 += 1
        print(f"{任务['id']:<6}{状态:<10}{任务['内容']:<20}{任务['创建时间']:<20}")
    
    print("=" * 50)
    已完成 = len(任务列表) - 未完成
    print(f"总计 {len(任务列表)} 条 | 待办 {未完成} 条 | 已完成 {已完成} 条")


def 标记完成(任务列表):
    """将任务标记为已完成"""
    查看任务(任务列表)
    if not 任务列表:
        return

    try:
        序号 = int(input("\n请输入要标记完成的任务序号："))
        任务 = 任务列表[序号 - 1]
        任务["已完成"] = True
        保存数据(任务列表)
        print(f"🎉 已完成：{任务['内容']}")
    except (ValueError, IndexError):
        print("无效的序号！")


def 删除任务(任务列表):
    """删除一条任务"""
    查看任务(任务列表)
    if not 任务列表:
        return

    try:
        序号 = int(input("\n请输入要删除的任务序号："))
        任务 = 任务列表[序号 - 1]
        确认 = input(f"确认删除「{任务['内容']}」？(y/n)：").strip().lower()
        if 确认 == "y":
            任务列表.pop(序号 - 1)
            # 更新序号
            for i, t in enumerate(任务列表):
                t["id"] = i + 1
            保存数据(任务列表)
            print("🗑️ 已删除")
        else:
            print("已取消")
    except (ValueError, IndexError):
        print("无效的序号！")


def 显示菜单():
    """打印操作菜单"""
    print("""
┌──────────────────────────┐
│      📋 待办事项管理器     │
├──────────────────────────┤
│  1. 查看所有任务          │
│  2. 新增任务              │
│  3. 标记完成              │
│  4. 删除任务              │
│  5. 退出                  │
└──────────────────────────┘""")


def 主程序():
    """主循环"""
    任务列表 = 加载数据()

    while True:
        显示菜单()
        选择 = input("请选择操作 (1-5)：").strip()

        if 选择 == "1":
            查看任务(任务列表)
        elif 选择 == "2":
            新增任务(任务列表)
        elif 选择 == "3":
            标记完成(任务列表)
        elif 选择 == "4":
            删除任务(任务列表)
        elif 选择 == "5":
            print("再见！👋")
            break
        else:
            print("无效选择，请重试！")


if __name__ == "__main__":
    主程序()
