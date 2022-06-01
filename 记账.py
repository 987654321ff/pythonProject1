import csv

import arrow
import regex as regex
import notion





def wechat(filepath):
    with open(filepath, "r", encoding="utf-8-sig", newline="") as f:
        lines = f.readlines()
        striped_lines = []
        start = False
        for line in lines:
            if not start:
                if line.startswith("----------------------"):
                    start = True
                continue
            striped_lines.append(line.strip())

        csvreader = csv.DictReader(striped_lines)
        for row in csvreader:
            # t = arrow.get(row["交易时间"]).replace(tzinfo="+08")
            c = row["商品"] + "，" + row["交易类型"] + "，" + row["交易对方"]
            a = row["金额(元)"]
            d = row["收/支"]
            print("", c, a, d)
            if d == "收入":
                a = "-" + a[1:]
            elif d == "支出":
                a = a[1:]
            else:
                print("[未被计入]")
                continue
                # 在这里，t、c、a 分别代码时间、内容、金额，而 Notion.add_bill 则是在前面一节所编写的
            # Notion.add_bill(t, c, a, "微信")
            notion.DataBase_additem111("e13ff198-10f8-454f-8fef-7917a17b63e8","", c, a)



def alipay(filepath):
    with open(filepath, "r", encoding="gbk", newline="") as f:
        lines = f.readlines()
        striped_lines = []
        start = False
        for line in lines:
            if not start:
                if line.startswith("----------------------------"):
                    start = True
                continue
            if line.startswith("----------------------------"):
                break
            l = regex.sub(r"\s+,", ",", line)
            striped_lines.append(l)

        csvreader = csv.DictReader(striped_lines)
        for row in csvreader:
            t = arrow.get(row["交易创建时间"]).replace(tzinfo="+08").datetime
            c = row["商品名称"] + "，" + row["交易对方"]
            a = row["金额（元）"]
            d = row["资金状态"]
            print(t, c, a, d)
            if a == "0":
                print("[未被计入]")
                continue
            elif d == "已收入" or d == "解冻":
                a = "-" + a
            elif d == "已支出" or d == "冻结":
                pass
            else:
                print("[未被计入]")
                continue
            # Notion.add_bill(t, c, a, "支付宝")
