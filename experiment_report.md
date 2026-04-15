# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** 2A202600027
**Name:** Đặng Văn Minh
**Date:** 15/04/2026

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Based on my data, the best choice is Laptop at $1200. | 9 | Dữ liệu sạch, không lỗi. |
| Garbage Data (`garbage_data.csv`) | Based on my data, the best choice is Nuclear Reactor at $999999. | 2 | Dữ liệu lỗi: giá sai ($999999 vô lý), thiếu ids, trùng lặp, sai định dạng, outliers. |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?

Dữ liệu Garbage chứa nhiều vấn đề nghiêm trọng:

- **Duplicate IDs:** ID trùng lặp gây khó khăn trong việc xác định sản phẩm duy nhất.
- **Sai định dạng dữ liệu:** Ví dụ, "ten dollars" không phải giá trị số hợp lệ, gây lỗi khi so sánh giá.
- **Outliers:** Giá trị bất thường như $999999 làm sai lệch quyết định của Agent.
- **Null Values:** Giá trị thiếu (ví dụ: ID hoặc tên sản phẩm trống) làm giảm độ tin cậy của dữ liệu.

Những vấn đề này làm gián đoạn khả năng xử lý và phân tích dữ liệu của Agent, dẫn đến câu trả lời sai lệch.

---

## 3. Ket luan

**Quality Data > Quality Prompt?**

Đồng ý. Dữ liệu chất lượng cao quyết định trực tiếp đến độ chính xác và tin cậy của câu trả lời từ Agent. Prompt tốt chỉ hiệu quả khi dữ liệu đầu vào đáng tin cậy.
