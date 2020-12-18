# Shipping in Odoo

Odoo can handle various delivery methods. Delivery methods can be used for sales orders or e-commerce

## Delivery methods

Handled by `Delivery Costs` module.

`eCommerce Delivery` integrates delivery methods to eCommerce

- Calculate price:
  - Fixed price:
  - Based on Rules: weight, volume, weight*volume, price, quantity

- 3rd party shipper in Vietnam
  - Already integrated by an Odoo partner:
    - [Viettel Post (odoo13) by Magenest](https://apps.odoo.com/apps/modules/13.0/magenest_vietelpost_integration/): mà chỉ có api documents của Aftership, Test module trên Odoo 13 CE thì có vẻ như module này chỉ track đơn vận thông qua Aftership, Aftership có liên kết với Viettel nhưng trong api của Aftership không thấy có cách lấy giá ship từ Viettel Post (chưa hiểu bọn này hoạt động kiểu gì, sẽ xem lại sau). Ncl các features của module này cũng không nhiều, và không thấy api docs của Viettelpost
      - Free
      - Aftership: là một platform giúp tracking đơn hàng vận chuyển, hỗ trợ cho các website ecommerce
      - 359 lines
      - Không tìm thấy api documents của ViettelPost nhưng có người làm tích hợp Viettelpost rồi (chắc nó giấu đâu đó chưa tìm ra hoặc mấy ổng tự gửi request thẳng đến website của viettelpost)
      - Chưa biết cách lấy token kiểu gì
    - [GHN (odoo13) by Magenest](https://apps.odoo.com/apps/modules/13.0/magenenst_ghn_integration/): Khá đầy đủ features giống bên Ahamove.
      - Free
      - Chưa test
      - [GHN API Docs](https://api.ghn.vn/home/docs/detail)
      - 856 lines
    - [Ahamove (odoo13) by Magenest](https://apps.odoo.com/apps/modules/13.0/delivery_ahamove_magenest/) :
      - Free
      - Chưa test
      - [Ahamove API Docs](https://developers.ahamove.com/#overview)
      - 113 lines
    - [GHN and Suppership by TopERP (v12,v13)](https://apps.odoo.com/apps/modules/13.0/shipping_station_connector/):
      - $18.19
      - 84133 lines
      - [Supership API Docs](https://docs.developers.supership.vn/guide/)


## Develope a shipping module

According to the notes in `delivery.carrier` model in `Delivery Costs` module:

```
 In order to add your own external provider, follow these steps:
 1. Create your model MyProvider that _inherit 'delivery.carrier'
    2. Extend the selection of the field "delivery_type" with a pair
       ('<my_provider>', 'My Provider')
    3. Add your methods:
       <my_provider>_rate_shipment
       <my_provider>_send_shipping
       <my_provider>_get_tracking_link
       <my_provider>_cancel_shipment
       _<my_provider>_get_default_custom_package_code
       (they are documented hereunder)
```

## Tìm hiểu về module `Delivery Costs của Odoo`

### Overview

- module name: `delivery`
- description: Allows you to add delivery methods in sale orders and picking. You can define your own carrier for prices. When creating invoices from picking, the system is able to add and compute the shipping line.
- depends:
  - `sale_stock`: This module makes the link between the sales and warehouses management applications.
  - `sale_management`: It handles the full sales workflow: **Quotations** &rarr; **Orders** &rarr; **Invoices**. If you also installed the Warehouse Management, you can deal with the following preferences:
    - Shipping
    - Invoicing
    - Incoterms

### `delivery.carrier`

#### attributes

- `name`: delivery method
- `delivery_type`: This field will be overwritten by internal shipping providers by adding their own type
- `company_id`
- `product_id`
- `invoice_policy`:
  - estimated cost
  - real cost
- `country_ids`
- `state_ids`
- `zip_from`
- `zip_to`

#### API for external providers

- `rate_shipment(self, order)`: Compute the price of the order shipment. It calls `<my_provider>_rate_shipment() `
- `send_shipping(self, pickings)`: Send the package to the service provider. It calls `<my_provider>_send_shipping()`
- `get_return_label(self, pickings, tracking_number=None, origin_date=None)`: It calls `<my_provider>_get_return_label()`
- `get_tracking_link(self, picking)`: Ask the tracking link to the service provider. It calls `<my_provider>_get_tracking_link()`
- `cancel_shipment(self, pickings)`: Cancel a shipment. It calls `<my_provider>_cancel_shipment()`
