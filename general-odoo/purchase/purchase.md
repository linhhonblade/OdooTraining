# Purchase
## Request for Quotations

- Enable Purchase Order Approval: Request managers to approve orders above a minimum amount
- Can add warning (like no delivery on weekends) for vendor in vendor form

## Lead Time

- Purchase Order Lead Time: #days from when we placing order to when those items arrive our stock
- Set Purchase Lead Time in Purchase tab
- Set Customer Lead Time in Inventory tab
- We can send RFQ to vendor by email or print RFQ and send
- Order date = Scheduled date: No lead day set on the product template for this vendor
- remove and add product again to RFQ to update lead time (if edit)

## Reordering Rule

- Reordering rule: when it is set, our company automatically generate RFQ when the rule is trigger (below a threshold)
- Can run scheduler manually from reordering rule form
- Can run scheduler for all product in Inventory / Operations / Run Scheduler
- There's a cron that runs once a day for reordering rule (automatically but not instant)
- Only Storable products have reordering rules


## Purchase Agreement

Activate Purchase Agreement in Purchase Settings
### Call for Tenders (TE)

> Allow choosing the vendor which offer better price for your RFQs

- Agreement selection type:
  - Select only one RFQ: once u confirm an RFQ to PO, Odoo will cancel all other RFQ related to this Call for Tender
  - Select multiple RFQ: even though I confirmed one PO, I still want the other to remain open
- Create Purchase Agreement, type Call for Tenders and confirm it
- From Purchase Agreement form, create multiple RFQ for different vendors and send by email (or print)
- If u don create any other RFQ for any vendor, validate the Purchase Agreement
- But you can still create new RFQ after validating the Purchase Agreement
- Update the price that the vendor offer u by editting the RFQ
- Select the RFQ u want and confirm
- Odoo automatically closes the Purchase Agreement when you confirm the PO (if choose Select only one RFQ)
- The RFQs or PO links to the Purchase Agreement via field `Source Document`

### Blanket Order (BO)

> Buying goods from a supplier at a negotiated price, on a recurring basis during a specific period of time

- Creating hundreds of PO is replaced by creating a blanket order and receive products in multiple deliveries
- Agreement selection type: Multiple RFQs

> You can still modify the qty if choosing Use qty of agreement

- Create new Purchase Agreement type Blanket Order
- The Vendor will be added to the Product Template (Purchase tab) when The Agreement is created


## 3-Way Matching

- Activate in Purchase Settings
- The qty in the bill reflects the qty u actually received
- If you create the bill for some products but not received any yet, the status Should be paid is False. True if the received qty = bill qty, Exception if received qty &lt; bill qty or u created two draft bills

## Purchase in different unit of measures than sales

- Enable in settings: UOM - Sell and purchase products in different units of measure (can create your own category and unit of measure if it is not standard in Odoo here or in Sale / Configuration)
- Specify sales and purchase unit of measures General Information tab of Product Template
- differents units of measures between sales and purchase necessarily need to share the same category. Categories include: Unit, weight, working time, volume, etc.

