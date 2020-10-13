# TimeSheet

- để note lại thời gian dành ra để làm hết một job trong môt project/task/sub-task
- Track thời gian còn lại để làm project/task/sub-task
- Có thể tạo timesheet trực tiếp trong app timesheet mà không cần vào trong project/task
- manager validate timesheet
- trong phần báo cáo có thể so sánh planned vs effective hours (chia theo từng task hoặc từng employee)
- HR analysis là xem lại số giờ làm, ca làm của nvien

## Workflow:

Có một loại product (dưới dạng service) tính tiền dựa trên số lượng giờ làm (timesheet on tasks) (unit = hour), khi ngta mua cái produc (service) đó thì nó có thể trở thành project hoặc task in a project (edit trong product). Timesheet giúp theo dõi công việc trong task và project dễ dàng hơn

mua cái service đấy chính là tạo quotation với product là tên service đấy. Quotation tạo xong thì odoo tự tạo task/project cho mình

tạo task xong thì gán task cho người thực hiện, người này có timesheet cost của riêng ngta. Chênh lệch giữa timesheet cost của service với của employee là lợi nhuận

track cost and revenue:
- enable timesheet: xuất hiện overview trong thẻ project
- enable analytic accounting (trong manage user -> access rights -> technical settings): xuất hiện profitablity trong thẻ project


