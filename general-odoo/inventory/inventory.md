# Overview

- The default setting is the immediate transfer where you do not need to “Mark as to do” and “Check availability” when delivering a product.
- Can create `Immediate Transfer` or `Planned Transfer` directly

# Warehouse Management

## Products

### Set initial stock

- Once you have created all your storable products, you can create an `Inventory Adjustment` to determine their current stock level in Odoo
- For a first `Inventory Adjustment`, I suggest you to keep the Products field empty. You can then Start Inventory.
- Odoo will highlight in red the lines for which there is a difference between the theoretical quantity on hand, which is automatically computed by the system, and the counted quantity you manually entered.

> If you work with product variants, the quantity on hand will show you the total quantity in stock for the product template, taking the different variants into account.

### UOM
- In the General Information tab of product template, you can select the Unit of Measure in which the product will be sold
- In the Purchase application, Create a new request for quotation in which you include the product with the different Units of Measure and Confirm it.
- When you enter the Receipt which is linked to the purchase order, odoo conver purchase uom to sale uom
- When doing a replenishment via the Replenish button on the product form, you have the possibility to use a different unit of measure.
- Depending on your product configuration, replenishment may trigger a request for quotation, a manufacturing order or a transfer
- The only condition is that all the units have to be in the same category (Unit, Weight, Volume, Length,…)

### Packages
- To separate a delivery into different packages you will have to set the done quantity to the desired package quantity then click on “PUT IN PACK”, do this for each package.

### Packaging

- In Odoo, packagings are used for indicative purposes on sale orders. They can be specified on the product form, in the inventory tab.

> Another useful use of the packaging is for product reception. By scanning the barcode of the packaging, Odoo adds the number of units contained in the packing on the picking.

## Inventory Adjustment

### Minimum stock rule:
- When the stock level of a product reaches its minimum the system will automatically generate a procurement order with the quantity needed to reach the maximum stock level.
- Config: Create a `Reordering Rule` and specify the `Product`, min/max qty
- The Quantity Multiple is used to round the procurement quantity up to this multiple.
- The Lead time is the number of days after the order point is triggered to receive the products or to order them to the vendor.
- In case you work with multi-warehouses and/or multi-locations, you will be able to specify different reordering rules for the same product in each location.

> For the reordering rules to be triggered, on the corresponding product, a route should be specified. In case you manufacture your products, make sure to select the route Manufacture and create a Bill of Material for the product. In case you purchase your products, make sure to select the route Buy and add a Vendor Pricelist.

> Don’t forget to select the product type storable in the product form. A consumable can not be stocked and won’t trigger reordering rules.


### Make to Order:
- The Make to Order function will trigger a Purchase Order of the amount of the Sales Order related to the product.
- The system will not check the current stock.
- This means that a draft purchase order will be generated regardless of the quantity on hand of the product.
- Config in product form, inventory tab, route: make to order

### Resupply from another Warehouse
- Actiate Multi-Warehouses + Multi-Step Routes
- Enter the warehouse which should be resupplied by another one, in warehouse form
- By activating this option, a new route will now be available on your products *Supply Product from Second warehouse*. It can now be selected, along with either a *reordering rule* or a *make to order*.
- Run Scheduler:
  - The system automatically creates two pickings, one *delivery order* from my Second Warehouse which contains the necessary products, and a receipt in my main warehouse WH/Stock for the same products.
  - The source document is the *reordering rule* which triggered the route *Supply Product from Second warehouse*.

## Warehouses

### Create Warehouses
- Enable Multi-Warehouse in Inventory settings: Multi-Locations will be automatically enabled
- new operation types automatically created by Odoo due to the creation of a new warehouse.

### Create Locations
- In case you want the location to be suggested when creating a Return or when Scrapping a product, you should check Is a Scrap Location? and Is a Return Location?.
- If you have the Barcode application installed, you can specify the barcode which will correspond to this location.

> A warehouse also corresponds to a location. As the locations are hierarchical, Odoo will create the parent location of the warehouse, containing all the sublocations in it.
> A consumable can not be stocked and will thus not be accounted for in the stock valuation.

## Delivery Orders

### Pick (default)

### Pick + Ship
- Once Multi-Step Routes has been activated, you can go to Inventory ‣ Configuration ‣ Warehouse and enter the warehouse which will use delivery in 2 steps.
- Activating this option will lead to the creation of a new Output location. If you want to rename it go to Inventory ‣ Configuration ‣ Locations
- Once you confirm the quotation, two pickings will be created and automatically linked to your sale order.
- If you click on the 2 Delivery button, you should now see two different pickings, one with a reference PICK to designate the picking process and another one with a reference OUT to designate the shipping process.
- The picking operation is the first one to be processed and has a Ready status while the delivery operation will only become Ready once the picking operation has been marked as done.
- the products which have been previously picked are automatically reserved on the delivery order.

### Pick + Pack + Ship
- Activating this option will lead to the creation of two new locations, Output and Packing Zone.
- Once you confirm the quotation, three pickings will be created and automatically linked to your sale order.
  - The first one with a reference PICK to designate the picking process,
  - The second one with the reference PACK that is the packing process,
  - The last one with a reference OUT to designate the shipping process.

### Dropshipping

### Deliver in Packages
- Activate in Settings
- create new packages and assign them to the stock move lines.
- Put in Pack button:
  - automatically assign a pack to the number of products which is set as Done and duplicate the stock move line if necessary.

### Limit delivery method to specific countries
- Config in Delivery Method form, destination tab
> This process doesn’t work in backend. We assume that when you create a Sale Order, you know which delivery method you can use since you created them.

### Cancel DO
- DO > Additional info tab

#### Points to be considered
- Use drop-shipping only for the products you can’t or don’t want to keep in stock.
- Drop-shipping is best for niche products.
- To protect your customers from bad experiences.
- Make sure time is not against you.
- Items have to be available from your supplier.

## Incoming Shipments

- Receive directly (default)
- Input + Stock (Receipt > Internal Transfer)
- Input + Quality Check + Stock (Receipt > Internal Transfer > Internal Transfer)

## Miscellaneous Operations

### Scrap
- You have to check Is a Scrap Location? on the location form. In fact, scrap locations cannot be used as normal storage locations and then, a virtual location will be created for scrapped products.
- Different ways to scrap products
  - scrap from receipt
  - scrap from delivery order
  - scrap from internal transfer
### Manage stock that you dont own
- enable the Consignment feature in the setting > Traceability section.
- If you are the owner, you can leave the field blank.
- Once the receipt is validated, the products enter your stock but still belong to the owner. They don’t impact your inventory valuation.

## Planning

### Lead Time
- Customer Lead Time: the time needed for your product to go from your warehouse to the customer place. Set in product form > inventory tab

> For example, product B is ordered on the 2nd of April but the Customer Lead Time is two days. In that case, the expected delivery date is the 4th of April.

- Sales Security Lead Time corresponds to backup days to ensure you are able to deliver the products in time. The purpose is to be ready shipping earlier in order to arrive on time. The number of security days is subtracted from the calculation to compute a scheduled date earlier than the one promised to the customer. Activate in Inventory

> For example, product B is scheduled to be delivered on the 6th of April but the Security Lead Time is one day. In that case, the scheduled date for the delivery order is the 5th of April.

- Delivery serveral product: in other info tab of SO
  - When all products are ready
  - As soon as possible
- Supplier Lead Time: time needed for a product you purchased to be delivered. Config in product form, purchase tab
- Purchase Security Lead Time: it is the margin of error for your supplier to deliver your order. Activate in Inventory
- Manufacturing Lead Time: time needed to manufacture the product. Config in product form. When working with Manufacturing Lead Times, the Deadline Start of the MO is Commitment Date - Manufacturing Lead Time.

> For example, the MO’s deadline start date for an order having a commitment date on the 10th of July is June 27th. (14 days Manufacture Lead Time)

- Manufacturing Security Lead Time:
  - Config in Manufacture settings
  - allows generating manufacturing orders earlier to cope with the risk of manufacturing delays.

> For example, a customer orders B with a delivery date scheduled on the 20th of June. The Manufacturing Lead Time is 14 days and the Security Lead Time is 3 days, so the manufacturing of B needs to start at the latest on the 3rd of June, which is the MO’s planned date.

> It is possible to add different vendors and, thus, different lead times depending on the vendor.

### Example
Here is a configuration:
- 1 day of security lead time for Sales
- 2 days of security lead time for Manufacturing
- 3 days of manufacturing lead time
- 1 day of security lead time for Purchase
- 4 days of supplier lead time

Let’s say that a customer orders B on the 1st of September and the delivery date is planned to be within 20 days (September 20th). In such a scenario, here is when all the various steps are triggered.

- September 1st: the sales order is created
- September 10th: the deadline to order components from the supplier because of the manufacturing process (4 days of supplier lead time)
- September 13th: the reception of the product from the supplier (1 day of security lead time for Purchase)
- September 14th: the deadline start date for the manufacturing (19th - 3 days of manufacturing lead time - 2 days of security lead time for Manufacturing)
- September 19th: the expected date on the delivery order form (1 day of security lead time for sales)
### Configure and Run Scheduler
- The scheduler is the calculation engine that plans and prioritizes production and purchasing.
- By default, the scheduler is set to run once a day.
- Run manually: Inventory > Operations > Run Scheduler
- For advanced user: dev mode > scheduled actions

## Lot/Serial Number

### Serial
- Receipts:
  - manual assignation
  - multi-assignation: To do so, you have to enter the first serial number of your set and the number of products you have to assign a serial number to.
  - copy/paste from xls file
- manage lots for each operation type
- By default, the creation of new lots/SN is only allowed at product reception.
- If you have inter-warehouse transfers and track products by lots, it can be useful to allow using existing lot numbers in receipts too.
- Location and Tracibility button on SN form

### Lots
- Manual assignation
- copy/paste excel
- like above

### Expiration Date
- Activate in settings
- Now, you have the possibility to define different dates in the inventory tab of the product form
  - Product Use Time: it’s the number of days before the goods start deteriorating, without being dangerous yet. It will be computed using the lot/serial number;
  - Product Life Time: refers to the number of days before the goods may become dangerous and must not be consumed. It will be computed on the lot/serial number;
  - Product Removal Time: shows the number of days before the goods should be removed from the stock. It will be computed on the lot/serial number;
  - Product Alert Time: refers to the number of days before an alert should be raised on the lot/serial number.

## Valuation Methods

> The consignment feature allows you to set owners on your stock (discover more about the consignment feature). When you receive products that are owned by another company, they are not taken into account in your inventory valuation.

- When I’ll confirm the receipt of the products, the value of my inventory will be impacted. If I want to know what this impact is, I can click on the valuation stat button.

> You need access rights on the accounting module to see that button.

### Landed Cost
- Activate in Inventory Settings
- The landed cost feature in Odoo allows to include additional costs (shipment, insurance, customs duties, etc.) into the cost of the product.
- Landed costs can only be applied to products with a FIFO or AVCO costing method and an automated inventory valuation (which requires the accounting application to be installed).
> The landed cost product must be of type service.
- If this product is always a landed cost, you can also define it on the product and avoid having to tick the box on each vendor bill.
### Impact on AVCO valuation when returning goods
- When products leave the warehouse: the average cost does not change
- In case of a product returned to its supplier after reception, the inventory value is reduced using the average cost formulae (not at the initial price of these products!).

# Shipping

## Shipping Setup

- Delivery methods are handled by the `Delivery Costs` module
> If you want to integrate delivery methods in your e-commerce, you’ll have to install the eCommerce Delivery module.

- Add new Delivery Method in configuration
- You can integrate Odoo with external shippers in order to compute the real price and packagings, and handle the printing the shipping labels.
- You can now choose the Delivery Method on your sale order. If you want to invoice the price of the delivery charge on the sale order, click on Set price, it will add a line with the name of the delivery method as a product.
- add or change the delivery method on the delivery itself.
- Flag Shipping enabled when you are ready to use it.
- Uncheck Test Mode when you are done with the testings.
- If you split the delivery and make several ones, each delivery order will add a line to the sale order.

# Advanced Routes

## Using Routes and Pull/Push Rules

### Routes

> All theses transfers are pre-generated by Odoo, starting from the end and going backwards. While working, the operator process these transfers in the opposite order: first the picking, then the packing, then the delivery order.

> Push Rules can be triggered only if no Pull Rule pre-generated the upstream transfers.

> Routes are a collection of Push and Pull Rules

- Applicable On:
  - Route that is applicable on sales order lines: You have to choose the route yourself when creating a quotation. This is pretty useful if some products go through different routes.
  - Warehouse (config in warehouse form)
  - Product Categoriesn (config in product category)
  - Product (config in product form)

### Rules

- Actions
  - Pull From: is triggered by a need for the product in a specific stock location. When the need appears in the source location, Odoo generates a picking to fulfill this need
  - Push To: is triggered by the arrival of some products in the defined source location.In case you move products to the source location, Odoo generates a picking to move those products to the destination location.
  - Push & Pull: when products are required at a specific location, a transfer is created from the previous location to fulfill that need. Then, a need is created in the previous location and a rule is triggered to fulfill it. Once the second need fulfilled, the products are pushed to the first location and all the needs are fulfilled.
  - Buy: when products are needed at the source location, a request for quotation is created to fulfill the need.
  - Manufacture: when products are needed in the source location, a manufacturing order is created to fulfill the need.

- Supply Method: This operation allows defining which kind of picking is created from the rule.
  - Take From Stock:
  - Trigger Another Rule
  - Take From Stock, if Unavailable, Trigger Another Rule

> If the source document is the same sale order, the status is not the same. In fact, the status is Waiting Another Operation if the previous transfer in the list is not done yet.

## Inter-Warehouse transfers

## Organize a cross-dock in a warehouse
- Cross-docking is the process of sending products that are received directly to the customers, without making them enter the stock.
- Activate multi step route
- both Incoming and Outgoing shipments should be configured to work with 2 steps
- This modification will lead to the creation of a Cross-Docking route that can be found in Inventory ‣ Configuration ‣ Routes.
- Create the product that uses the Cross-Dock Route and then, in the inventory tab, select the routes Buy and Cross-Dock. Now, in the purchase tab, specify the vendor to who you buy the product and set a price for it.

## Taking stock from different warehouses
- the main stock locations of warehouse A and warehouse B are children locations of the main stock location of warehouse A + B (WHA+B is virtual WH).
- Let’s say you have two products, one stored in warehouse A and one stored in warehouse B. Now, you can create a new quotation for one of each product. Go to other information and choose Warehouse A+B in the shipping information.
- Once you have done it, you can convert it to a sales order. Then, a delivery order will be automatically generated, with a product reserved in warehouse A and one in warehouse B

## Putaways and Removal Strategies
- Putaway Rules:
  - Activate Multi Step Route
  > The putaway rules can be defined either per product or per product category.
  - Create a putaway rule
  - if I purchase apples and carrots to my supplier, they will be grouped in the same receipt but redirected to the right location automatically, thanks to putaway rules.
- Removal Strategies:
  - Activate Lot/SN + Storage Location + Multi-Step Routes (+Expiration Dates if using FEFO method)
  - Define Removal Strategies on Product Category
  - FEFO:
    - Lots are picked based on their removal date, from earliest to latest. Lots without a removal date defined are picked after lots with removal dates.
    - Other dates are for informational and reporting purposes only. If not removed from the stock, lots that are past the expiration dates may still be picked for delivery orders!
