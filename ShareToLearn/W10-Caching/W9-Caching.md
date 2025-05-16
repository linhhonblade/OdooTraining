---
theme: "Singapore"
colortheme: "seahorse"
title: Asynchronous in Python and Odoo
author: 'Mailovemisa'
institute: 'A1 Consulting'
date: May 9th, 2025
toc: true
slide_level: 2
mainfont: "merriweather"
fontsize: 10pt
linkstyle: bold
urlcolor: red
lang: en-US
aspectratio: 169
header-include: |
    \metroset{progressbar=frametitle,sectionpage=progressbar}

# pandoc report.md -t beamer -o slide.pdf
---

# What?

**Cache** là lớp đệm trung gian giữa client và nguồn dữ liệu gốc nhằm phục vụ dữ liệu nhanh hơn khi có yêu cầu lặp lại.

# Why?

| Lợi ích               | Giải thích                                                        |
| --------------------- | ----------------------------------------------------------------- |
| Giảm độ trễ (latency) | Trả kết quả nhanh hơn                                             |
| Giảm tải cho backend  | Ít truy vấn DB/API                                                |
| Tăng throughput       | Nhiều request hơn trên cùng tài nguyên                            |
| Tiết kiệm chi phí     | Giảm số lần truy vấn dịch vụ tốn tiền (vd: GPT, Redis, API cloud) |

# Các loại cache phổ biến

| Loại Cache       | Vị trí              | Ví dụ                                    |
| ---------------- | ------------------- | ---------------------------------------- |
| In-memory        | RAM (local process) | Python `@lru_cache`, Odoo `ormcache`     |
| Distributed      | Redis, Memcached    | Redis + Flask/Django                     |
| CDN              | Gần client          | Cloudflare, Akamai cache tài nguyên tĩnh |
| Browser cache    | Trình duyệt         | Cache ảnh, CSS, JS                       |
| Persistent cache | Lưu ra file         | `diskcache`, `joblib`, `pickle`          |


# Caching Strategies

## 1, Cache-aside (Lazy caching)

- App kiểm tra cache trước → nếu không có → truy DB → lưu vào cache.
- Dữ liệu cập nhật cần tự invalidate cache.

✅ Phổ biến, dễ triển khai

❌ Dễ stale nếu không invalidate kỹ

## 2. Write-through

Khi ghi dữ liệu → ghi cả cache và DB đồng thời.

✅ Đảm bảo cache luôn nhất quán

❌ Có độ trễ khi write

## 3. Write-back / Write-behind

Ghi vào cache trước, rồi ghi DB sau (asynchronously).

✅ Nhanh khi write
❌ Rủi ro mất dữ liệu nếu crash

## 4. Read-through

App không truy cập DB trực tiếp mà luôn đọc qua cache layer.

✅ Centralized logic
❌ Tăng độ phức tạp hệ thống

# Eviction Policies (Chính sách loại bỏ cache)

Cache sẽ phình to (gần bằng DB gốc) nếu không có chiến lược loại bỏ phù hộp

| Chính sách                      | Ý nghĩa                        |
| ------------------------------- | ------------------------------ |
| **LRU** (Least Recently Used)   | Xoá item ít dùng gần đây nhất  |
| **LFU** (Least Frequently Used) | Xoá item ít được truy cập nhất |
| **FIFO**                        | Xoá theo thứ tự thêm vào       |
| **TTL Expiry**                  | Hết hạn tự xoá                 |
| **Manual**                      | Dev tự tay xóa                 |


# Khi nào KHÔNG nên dùng cache?

- Dữ liệu thay đổi liên tục và cần độ nhất quán cao (e.g., số dư tài khoản)
- Khi logic rất nhẹ → không cần optimize thêm
- Khi hệ thống chưa gặp bottleneck → premature optimization là waste

# Cache in Python

## `functools.lru_cache` - built-in, đơn giản, RAM

LRU Cache luôn giữ lại các mục được sử dụng gần đây nhất, và xóa mục ít được truy cập nhất trong thời gian gần đây khi cache đầy.

Nói cách khác:

- Mỗi lần truy cập vào một mục → nó được "đánh dấu là mới sử dụng"
- Khi cần xóa để lấy chỗ → cache xóa mục lâu không đụng tới nhất

```python
@lru_cache()
        def search_journal_ids(company_id):
            """Search all the journal of a certain type for a company.

            This method is cached, only one search is done per company_id.
            :param company_id (int): the company to search journals for.
            :return (list<int>): the ids of the bank and cash journals of a company
            """
            return self.env['account.journal'].search([
                *self.env['account.journal']._check_company_domain(company_id),
                ('type', 'in', ('cash', 'bank')),
            ]).ids
```

## `cachetools`

...


# Cache in Odoo

## 1. Mục tiêu của cache trong Odoo

- Tăng hiệu năng khi truy xuất dữ liệu từ PostgreSQL
- Giảm load lên DB trong môi trường multi-worker
- Tối ưu truy cập field, model, view, params, v.v.
- Giảm RPC latency khi phục vụ frontend (JS + XML)

## 2. Cache trong Odoo

| Tên Cache                          | Mục tiêu                                     | Dạng lưu trữ      | Invalidation                        |
| ---------------------------------- | -------------------------------------------- | ----------------- | ----------------------------------- |
| `@tools.ormcache()`                | Cache hàm/method dùng model context          | RAM (per-process) | Thủ công (via `invalidate_cache()`) |
| `@tools.ormcache_context()`        | Cache có phân biệt context như lang, company | RAM               | Thủ công                            |
| `ir.config_parameter`              | Config toàn hệ thống                         | RAM (per-process) | Tự invalidate khi `set_param()`     |
| `@lru_cache`                       | Python function caching                      | RAM               | Không tự invalidate                 |
| View cache                         | Cache XML view parsed                        | RAM               | Xóa khi update module/view          |
| Record rules / Access rights       | Cache rule evaluation per model/user         | RAM               | Invalidate khi thay đổi ACL         |
| Translation cache                  | Cache chuỗi dịch                             | RAM               | Invalidate khi update lang          |
| Model metadata (fields, relations) | Cache cấu trúc model, field                  | RAM               | Invalidate khi restart/update model |

## 3. ORM Cache (@tools.ormcache)

```python
from odoo.tools import ormcache, ormcache_context
```

- Decorator cache kết quả hàm dựa trên *args
- Lưu kết quả trong process memory
- Không phân biệt worker → mỗi worker có cache riêng
- Phải invalidate thủ công nếu dữ liệu thay đổi


```python
    @api.model
    @ormcache('key')
    def _get_param(self, key):
        # we bypass the ORM because get_param() is used in some field's depends,
        # and must therefore work even when the ORM is not ready to work
        self.flush_model(['key', 'value'])
        self.env.cr.execute("SELECT value FROM ir_config_parameter WHERE key = %s", [key])
        result = self.env.cr.fetchone()
        return result and result[0]
```

## ⚠️ 4. Multi-worker = cache per-process

Odoo không chia sẻ RAM cache giữa workers:
- Mỗi worker (process) có RAM riêng
- Cache (ormcache, ir.config) nằm trong RAM → không share
- Khi 1 worker update cache (set_param, update model), các worker khác vẫn dùng cache cũ

Giải pháp:
- Odoo không có cache bus mặc định
- Muốn sync → phải dùng:
  - clear_caches() trong ir.config_parameter
  - Hoặc module custom dùng Redis/pubsub để sync invalidate

