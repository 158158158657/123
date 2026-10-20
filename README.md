# 课程作业提交仓库

- **学号：** 20244080120
- **姓名：** 雷永胜

## 提交内容

| 文件 | 说明 |
| --- | --- |
| `20244080120_雷永胜_hw01.ipynb` | 作业1：Data Types, Functions and Conditionals |
| `20244080120_雷永胜_exp01.ipynb` | 实验报告01：Python基础与数据处理入门 |
| `student_utils.py` | 实验4 要求的解析模块（与 Notebook 同级，供 `import student_utils` 使用） |
| `exp01_data/` | 实验4 生成的数据目录：`students.txt`、`report.txt`、`students.pkl` |

## 运行环境

- Python 3.13 + Jupyter Notebook
- 独立 conda 环境 `exp01`（未使用 base 环境）
- 全部 Notebook 均在重启内核后按从上到下的顺序完整运行，输出已保存在文件中

## 复现方式

```bash
conda activate exp01
jupyter notebook
```

打开对应 `.ipynb`，`Kernel → Restart & Run All` 即可复现全部输出。
`exp01_data/` 与 `student_utils.py` 由 `exp01.ipynb` 运行时自动生成。
