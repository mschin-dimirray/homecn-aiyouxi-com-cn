import json
import sys
from datetime import datetime


def build_site_entry(url: str, title: str, tags: list, description: str) -> dict:
    return {
        "url": url,
        "title": title,
        "tags": sorted(tags),
        "description": description,
        "added": datetime.now().strftime("%Y-%m-%d")
    }


def load_default_sites() -> list:
    return [
        build_site_entry(
            url="https://homecn-aiyouxi.com.cn",
            title="爱游戏主页",
            tags=["爱游戏", "首页", "游戏资讯"],
            description="提供最新游戏资讯、攻略和社区交流的综合平台"
        ),
        build_site_entry(
            url="https://homecn-aiyouxi.com.cn/news",
            title="爱游戏新闻",
            tags=["爱游戏", "新闻", "更新"],
            description="游戏行业动态与版本更新公告"
        ),
        build_site_entry(
            url="https://homecn-aiyouxi.com.cn/community",
            title="爱游戏社区",
            tags=["爱游戏", "论坛", "玩家交流"],
            description="玩家讨论区，分享心得与组队信息"
        ),
        build_site_entry(
            url="https://homecn-aiyouxi.com.cn/guide",
            title="爱游戏攻略",
            tags=["爱游戏", "攻略", "教程"],
            description="新手入门指南与高级技巧汇总"
        ),
    ]


def format_summary(sites: list) -> str:
    lines = []
    lines.append("=" * 58)
    lines.append("  站点资料汇总摘要")
    lines.append("=" * 58)
    lines.append("")
    for idx, site in enumerate(sites, start=1):
        lines.append(f"  [{idx}] {site['title']}")
        lines.append(f"       URL: {site['url']}")
        lines.append(f"       标签: {'、'.join(site['tags'])}")
        lines.append(f"       说明: {site['description']}")
        lines.append("")
    lines.append("-" * 58)
    lines.append(f"  共收录 {len(sites)} 个站点")
    lines.append(f"  生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 58)
    return "\n".join(lines)


def main():
    sites = load_default_sites()
    output = format_summary(sites)
    print(output)

    # 可选：写入文件
    with open("site_summary_output.txt", "w", encoding="utf-8") as f:
        f.write(output)
    print("\n摘要已保存至 site_summary_output.txt")


if __name__ == "__main__":
    main()