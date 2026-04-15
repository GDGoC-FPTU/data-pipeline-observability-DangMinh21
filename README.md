[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23574151&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** 26ai.minhdv@vinuni.edu.vn
**Name:** Đặng Văn Minh

---

## Mo ta

Bài lab này tập trung vào việc xây dựng một ETL pipeline để xử lý dữ liệu và kiểm tra tính quan sát của dữ liệu. Tôi đã thực hiện pipeline để xử lý dữ liệu thô, tạo dữ liệu sạch, và tiến hành thực nghiệm với dữ liệu sạch và dữ liệu lỗi.

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
```bash
# Clean Data
python agent_simulation.py processed_data.csv

# Garbage Data
python agent_simulation.py garbage_data.csv
```

---

## Cau truc thu muc

```
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline
├── garbage_data.csv         # Du lieu loi de kiem tra
├── experiment_report.md     # Bao cao thi nghiem
└── README.md                # File nay
```

---

## Ket qua

- **Dữ liệu đầu vào:** 5 records
- **Dữ liệu sau xử lý:** 3 records (2 bị loại do lỗi hoặc không hợp lệ)
- **Thực nghiệm:**
  - Clean Data: Agent trả lời chính xác với độ chính xác 9/10.
  - Garbage Data: Agent trả lời sai với độ chính xác 2/10.
