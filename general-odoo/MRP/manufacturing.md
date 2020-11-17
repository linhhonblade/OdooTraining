# Manufacturing

## Manufacturing process overview

| Department                | Documents/Apps                    |
| ------------------------- | --------------------------------- |
| Engineering               | CAD & BOM                         |
| Manufacturing Engineering | Routings, Worksheets, Workcenters |
| Purchase/Procurement      | PO/RFQ                            |
| Inventory Operators       | Receipts/Barcode                  |
| Manufacturing Foreman     | MO/Planning                       |
| Manufacturing Operators   | WO (sometimes on Tablets)         |
| Inventory Operators       | Delivery                          |
| Quality                   | Alerts/Analysis                   |
| Quality (component issue) | Control points                    |
| ME (design issue)         | ECO -> New BOM                    |
| Maintenance               | Preventive/Corrective             |

1. Engineers design the final products. Then they create a BOM (Bill of Material)
2. Routings: Set of steps the product goes through for production. Worksheets are instructions for manufacturing operator. Workcenters are the places where the production is contructed
3. Buy the items required in manufacturing process (Purchase)
4. Once the items arrive at our plants, they will be receive by inventory team
5. Once we have all the items, start manufacturing process. Manufacturing Foreman creates a Manufacturing Order and manage the planning of manufacturing operators
6. Manufacturing Operators start production following work order (sometimes on Tablets)
7. After completion of products, the Inventory Team prepares the order for shipping
8. Once products are delivered, the customers may report an issue with it.
9. When a quality Alert is triggered, they Analysis is processed to figure out the cause of the issue
10. Corrective Maintenance: you will fix an alrd existing issue (fixing what broken). Preventive Maintenance: To prevent product broken in future

## Bill of Materials

- You can use BOM without routing
- BOM Type:
  - Manufature this product
  - Kit: If you want to assemble kits as they are ordered, managing stock of the kit components only, you will use a Kit BoM without a manufacturing step.
  - Subcontractor
- If only one variant &rarr; specify in `Product Variant` field
- If not, specify in `Apply on Variant`
- You can add serveral variants for each component
- Add routing to BOM when you need to define a series of operations required by your manufacturing process (enable in settings)
- Each BOM only one routing while each routing can be used multple times
- Produce residual product (A+B=C+D) by enable "By-products" in settings
- Can add add many by-products as u want but need to register which operation produces that by-product in field `Produced in Operation`

## Process Manufacturing

- One place, one person, one step &rarr; Manufacturing orders without routing (default in Odoo): Create MO &rarr; Record the production
- Manufacturing orders with work centers and routing:
  - Create MO
  - Schedule the associated work orders
  - Perform the scheduled works and record the production

## Sell sets of products as kits

> If you want to assemble kits as they are ordered, managing stock of the kit components only, you will use a Kit BoM without a manufacturing step.

### Sell as a kit product and deliver kit to customer
- A product using a Kit BoM will appear as a single line item on a quotation and sales order, but will generate a delivery order with one line item for each of the components of the kit.
- Kit product: route Manufacture only, product type Consumable, Cannot be purchased
- No particular configuration for component products required

### Assemble the kit befor deliver the kit product to customer
- Use BOM Type: Manufacturing
- Kit product: route Manufacture + Make to Order (MTO) (auto create MO when a sale order is confirmed)
- Product type: Storable

## Manage BOM for product variants

- One BOM for variants of same product (enable variant in settings)

## Semi-finished products

- multi-level BOM: a BOM that employs subassemblies
- For subassemblies: route Manufacture + Replenish on order (MTO)
- Create BOM for the subassemblies, BOM type Manufacture
- add subassemplies to component tab of top-level BOM (BOM type Manufacture)
- Now, each time you will plan a manufacturing order for the top-level product, a manufacturing order will be created for the subassembly one.

## Flexible components consumption

- Activate Quality in settings
- BOM consumption type: Flexible (in Miscellaneous tab)
- Create new quality control point (in Quality App) with type Register Consumed Material

## Plan work order

- Enable work orders in settings
- Access to the scheduled orders by going to Planning menu
- If you plan two work orders at the same hour, the second one will be scheduled after the first one if the jobs need to be done at the same work center. The start date will, then, be automatically updated considering the first free slot on the work center.

## Unbuild a product

- Unbuild Order: Select MO (if unbuild things u manufacture), Select Product (unbuild things u receive)

## Subcontractor

- Enable Subcontracting in settings
- Use BOM type: Subcontracting

![Subcontracting Flow](subcontracting_04.png)

- The PO is optional. If you create a receipt manually, with the right subcontractor, Odoo still performs all the moves. Useful if the subcontractor does not bill a fixed price per item, but rather the time and materials used.
- If managing the replenishment of raw materials B at your subcontractor’s location is not needed, simply include the cost of B in the subcontractor’s price s and remove the products B from the BoM.
- To manage resupply subcontractors by sending products from company locations

### Automate Replenishment of Subcontractors

- Activate Multi-locations in Inventory
- Resupply Subcontractor manually: Create delivery order with delivery address
- automate by re-ordering rule: define a re-ordering rule on the subcontracting location
- automate by replenish on order flow: select route Resupply Subcontractor on Order on the wanted component. the demand in the finished product (real demand or forecasted one through the Master Production Schedule) triggers the replenishment of the subcontractor.

### Replenishmen from another supplier

- activate dropshipping in purchase
- Set Deliver To Dropship, Dropship Address to Subcontractor Location
- it is still required to validate receipts for the subcontractor.

### Quality control

- Create a quality check at receipt because the manufacturing process is carried by external party &rarr; Creat a new Quality control point

## Set routings on kit BOM

### Finished Product & Kit Component have the same Routing

- Create Manufacture BOM including a Kit component
- set a routing on BOM
- Create kit BOM for the kit component with same routing
- define the opereation in which the kit component is used
- When create MO, 2 WO created

### Finished Product & Kit Component haven’t the same Routing

- Create Manufacture BOM including a Kit component
- set a routing on BOM
- 3 WOs created

### Master Production Schedule

- Demand Forecast: your estimation for the period
- Actual Demand: The confirmed sales
- can manually edit the To replenish quantity

- Green: quantity of products which should be replenished to reach the expected safety stock considering the demand forecast and the indirect demand forecast.
- Grey: replenishment order has already been generated, and its quantity still matches current data.
- Red: replenishment order has already been generated, and its quantity was too high considering current data.
- Orange: replenishment order has already been generated, and its quantity was too low considering current data.

- The products are ordered in the MPS based on their sequence. You can rearrange that sequence by going on the list of your products and reorganize them with drag and drop.
- you can decide which information you would like to show by clicking on rows

**What if I have underestimated the demand?**
You can still increase the demand forecast. It will impact the quantity to replenish. The cell will become orange, and you’ll be able to launch a new replenishment.

**What if I have overestimated the demand?**
You can decrease the demand forecast. The cell will become red to inform you that you’ve ordered more than planned.

You can easily remove a product from the MPS by clicking the small bin on the right of its name.
