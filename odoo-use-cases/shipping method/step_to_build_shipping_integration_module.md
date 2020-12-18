# GHN Shipping Integration Solution

**API của GHN chỉ hỗ trợ address dạng code (như khiểu ProvinceID, DistrictID,..) và nó cũng không hỗ trợ hàm để tra ra cái Id đó dựa trên tên của đơn vị hành chính mà chỉ cung cấp api để liệt kê id ứng với tất cả tên của đvi hành chính**

> Túm cái quần lại là muốn gửi api để định giá ship thì phải làm thêm một bước là mần ra cái id của cái địa chỉ gửi và nhận hàng. Cái này liên quan đến module base (giờ mới hiểu tại sao bọn magenest lại có cái depend = [base] trong manifest) tuy nhiên magenest viết hàm gửi api ở trong model sale.order (cái này đi sai với hướng dẫn của odoo và không hiểu sao nó lại làm vậy)

Nói chung là chuyển sang làm cái Ahamove trước, vì api của nó dễ dùng hơn

# Ahamove Shipping Integration Solution (lấy API_KEY qua mail ming@ahamove.vn)

*Ahamove tính phí vận chuyển dựa trên số điểm dừng và quãng đường vận chuyển. Tối đa 80kg kích thước 90x60x90 (dịch vụ giao hàng cồng kềnh)*

## Module structure

`name`: `delivery_ahamove`
`depends`: [`delivery`]

**models**
- `AhamoveProvider`:
  - attributes:
    - `_inherit`: `delivery.carrier`
    - `delivery_type`: thêm lựa chọn `Ahamove`
    - `prod_environment`: Set to True if your credentials are certified for production
      - false: gọi đến api test
      - true: gọi đến api production
  - methods:
    - `ahamove_rate_shipment()`: call api estimate order fee
    - `ahamove_send_shipping()`: call api create order
    - `ahamove_get_tracking_link()`: call api get order tracking link
    - `ahamove_get_return_label()`
    - `ahamove_cancel_shipment()`: call api cancel order

**libraries**
- requests, werkzeugh.url (dùng lúc viết hàm để lấy/refresh token)
- json
- UserError (odoo.exceptions)
- logging (print log in debug mode)
- request (odoo.http) (dùng lúc gọi api)
