# Usecase Description



# [Add Users and Manage Access Rights](https://www.odoo.com/documentation/user/14.0/general/odoo_basics/add_user.html)

- **Group** are created to define rules to models within an application.
- **Inherited** means that users added to this application group are automatically added to the following ones.
- The **Menus** tab is where you define which menus (models) the user can have access to.
- **Access Rights** rules are the first level of rights.
- As a second layer of editing and visibility rules, **Record Rules** can be formed. They overwrite, or refine, the **Access Rights**.
- A record rule is written using a **Domain**. **Domains** are conditions used to filter or searching data.

# [Security In Odoo](https://www.odoo.com/documentation/14.0/reference/security.html)

- A user belongs to any number of groups, and security mechanisms are associated to groups, thus applying security mechamisms to users.

## Access Control

- `ir.model.access`
- Each access control has a model to which it grants permissions, the permissions it grants and optionally a group.
- Access controls are additive, for a given model a user has access all permissions granted to any of its groups: if the user belongs to one group which allows writing and another which allows deleting, they can both write and delete.
- If no group is specified, the access control applies to all users, otherwise it only applies to the members of the given group.

## Record Rules

- Record rules are conditions that records must satisfy for an operation to be allowed. It is applied record-by-record **after access control has been applied**.
- A record rule has:
  - A model on which it applies
  - A set of permissions to which it applies (read, write, create, unlink)
  - A set of user groups to which the rule applies, if no group is specified the rule is **global**
  - A domain used to check whether a given record matches the rule (and is accessible) or does not (and is not accessible)
  - The domain is evaluated with two variables in context: `user` is the current user’s record and `time` is the time module

- **Global rules** are **subtractive**, they must all be matched for a record to be accessible
- **Group rules** are additive, if any of them matches (and all global rules match) then the record is accessible

# Default config from Odoo

## Sale Team

- member của 1 sale team không thể nhìn thấy tài liệu của nhau (thuộc group Sales / User: Own Documents Only)
- Leader của một sale team có thể nhìn thấy toàn bộ documents liên quan đến sale của team cũng như của các team khác nhưng lại không nhìn được report (thuộc group Sales / User: All Documents)
- Thằng duy nhất trong default config của Saless mà có thể nhìn được report là Sales / Administration (thằng này đồng thời có quyền config sales team và activity types - thêm, sửa, xóa)

## Invoice

- Trong module invoice đang có hai group
- Invoice / Billing : xem được hết invoice (ko quan trọng của ai)
- Invoice / Administrator: Xem được hết invoice và có quyền config

# Những cái đã customize được

## Giới hạn quyền của Team leader

- [x] Saleperson can only access their own documents
- [x] Sale team leader can access all documents of his/her team (including team member's documents)
- [x] Sale team leader cannot access document from other sale team
- [x] Sale team leader can access documents of other sale team if the owner add he/she to the follower list

- Documents ở đây bao gồm :
  - Lead/Opp (crm.lead)
  - Order (sale.order)
  - Order Line (sale.order.line)
  - Invoice (Journal Entry) (account.move)
  - Invoice Line (Journal Item) (account.move.line)
  - Sale Analysis Report (sale.report)
  - Invoice Statistics (account.invoice.report)

**Solution**

- Bỏ sales team leader ra khỏi group Sales / All Documents và thêm vào group tự tạo là Sales / All Team's Documents. Group này chỉ cho phép nhìn thấy documents của team
- Thêm toàn bộ user vào group mới là Sales / User: Following Document. Group này cho phép user nhìn thấy các documents được link đến cái opportunity mà người đó được mời follow

- Thay thế group Invoice / Billing bằng group Invoince / Own Billing để users chỉ xem được invoice của mình

- Thêm trường mới để link với Order cho Invoice Lines và Invoices. Thêm Automated action cho invoice và invoice lines để tự động cập nhập trường mới kia
- Dùng trường mới thêm để tạo record rules.

## Mở rộng thêm một level PMO. Một PMO quản lý nhiều Team Leader. Có nhiều PMO và nằm dưới quyền CEO

[x] PMO Manager can access all documents of members in that PMO
[x] Can share documents between PMO, other members in different teams

**Solution**

For every PMO, create a group and add user belong to that PMO (including PMO Manager) to that group (e.g. groups PMO1, PMO2). Set the category of those groups is PMO

Create a new group named PMO Manager and add all PMO managers to that group

Create a new field PMO in model Users


# Các giải pháp khác có thể cân nhắc

- Thay vì share bằng việc thêm follower trong opportunity, thì có thể thay field Saleperson: Many2one trong model Lead/Opp thành Salepersons: Many2many để có thể assign nhiều saleperson cho một Lead/Opp
- Tạo một Automated Action để nó tự động add follower cho sale order hoặc invoice nếu như nó được link tới cái Lead/Opp mà người đó đang được mời follow (cái này đã thử mà chưa thành công)


# Những điều còn băn khoăn
