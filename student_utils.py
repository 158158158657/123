# 实验4 的解析工具模块（由 Notebook 生成）。
# 把一行 'name,score' 解析成字典，非法记录抛出 ValueError。


def parse_student(line):
    parts = [part.strip() for part in line.split(",")]
    if len(parts) != 2:
        raise ValueError(f"字段数量错误（应为 2 个，实际 {len(parts)} 个）")
    name, score_text = parts
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩不是整数: {score_text!r}") from None
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0~100 范围: {score}")
    return {"name": name, "score": score}
